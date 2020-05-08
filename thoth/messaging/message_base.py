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


"""This is Thoth Messaging module."""


import os
import json
import logging
import ssl

import faust

_LOGGER = logging.getLogger(__name__)


KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
KAFKA_CAFILE = os.getenv("KAFKA_CAFILE", "ca.crt")
KAFKA_CLIENT_ID = os.getenv("KAFKA_CLIENT_ID", "thoth-messaging")
KAFKA_PROTOCOL = os.getenv("KAFKA_PROTOCOL", "SSL")
KAFKA_TOPIC_RETENTION_TIME_SECONDS = 60 * 60 * 24 * 45
KAFKA_SSL_AUTH = int(os.getenv("KAFKA_SSL_AUTH", 1))
MESSAGE_BASE_TOPIC = "thoth.base-topic"


class MessageBase:
    """Class used for Package Release events on Kafka topic."""

    if KAFKA_SSL_AUTH:
        ssl_context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH, cafile=KAFKA_CAFILE)
        app = faust.App(
            KAFKA_CLIENT_ID,
            broker=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer="json",
            ssl_context=ssl_context,
        )
    else:
        app = faust.App(
            "thoth-messaging",
            broker=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer="json",
        )

    def __init__(
        self,
        topic_name: str = MESSAGE_BASE_TOPIC,
        value_type=None,
        num_partitions: int = 1,
        replication_factor: int = 1,
    ):
        """Create general message."""
        self.topic = self.app.topic(
            topic_name, value_type=value_type, retention=KAFKA_TOPIC_RETENTION_TIME_SECONDS, partitions=1, internal=True
        )

    async def publish_to_topic(self, value):
        """Publish to this messages topic."""
        await self.topic.send(value=value)
