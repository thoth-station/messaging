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


"""This is Thoth Messaging module for UpdateProvidesSourceDistroMessage."""

from typing import Optional

from .message_base import MessageBase, BaseMessageContents


class UpdateProvidesSourceDistroMessage(MessageBase):
    """Class used for updating python package version provides_source_distro flag."""

    topic_name = "thoth.update-provides-source-distro"

    class MessageContents(BaseMessageContents, serializer="json"):  # type: ignore
        """Class used to represent a contents of a update-provides-source-distro message."""

        package_name: str
        package_version: str
        index_url: str
        value: bool
        version: str = "v1"

    def __init__(
        self,
        num_partitions: int = 1,
        replication_factor: int = 1,
        client_id: str = "thoth-messaging",
        bootstrap_server: str = "localhost:9092",
        topic_retention_time_second: int = 60 * 60 * 24 * 45,
        protocol: Optional[str] = None,
    ):
        """Initialize missing package topic."""
        super(UpdateProvidesSourceDistroMessage, self).__init__(
            topic_name=self.topic_name,
            value_type=self.MessageContents,
            num_partitions=num_partitions,
            replication_factor=replication_factor,
            client_id=client_id,
            bootstrap_server=bootstrap_server,
            topic_retention_time_second=topic_retention_time_second,
            protocol=protocol,
        )
