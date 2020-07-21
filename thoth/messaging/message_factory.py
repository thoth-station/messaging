#!/usr/bin/env python3
# thoth-messaging
# Copyright(C) 2020 Kevin Postlethwait
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


"""This is Thoth Messaging module for message_factory."""

import faust
from typing import Union, Tuple, Any, GenericMeta
from .message_base import MessageBase


def message_factory(
    t_name: str,
    message_contents: Tuple[str, str],
    num_partitions: int = 1,
    replication_factor: int = 1,
    client_id: str = "thoth-messaging",
    ssl_auth: int = 1,
    bootstrap_server: str = "localhost:9092",
    topic_retention_time_second: int = 60 * 60 * 24 * 45,
    protocol: str = "SSL",
):
    """Create new message types dynamically."""

    class NewMessage(MessageBase):
        """Class used for any events on Kafka topic."""

        topic_name = t_name

        class MessageContents(faust.Record, serializer="json"):
            """Class used to represent a contents of a faust message Kafka topic."""
            for name, t in message_contents:
                exec(f"{name}: {t}")

            def __init__(self, **kwargs):
                for k, v in message_contents:
                    if kwargs.get(k) is None:
                        raise RuntimeError(f"{k} was not supplied or the wrong type was passed.")
                    setattr(self, k, kwargs.get(k))

        def __init__(self):
            """Initialize arbitrary topic."""
            super(NewMessage, self).__init__(
                topic_name=self.topic_name,
                value_type=self.MessageContents,
                num_partitions=num_partitions,
                replication_factor=replication_factor,
                client_id=client_id,
                ssl_auth=ssl_auth,
                bootstrap_server=bootstrap_server,
                topic_retention_time_second=topic_retention_time_second,
                protocol=protocol,
            )

    return NewMessage
