#!/usr/bin/env python3
# thoth-messaging
# Copyright(C) 2020 Kevin Postlethwait, Francesco Murdaca
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
from typing import Optional, Any

_LOGGER = logging.getLogger(__name__)


class MessageBase:
    """Class used for Package Release events on Kafka topic."""

    def __init__(
        self,
        topic_name: Optional[str] = None,
        num_partitions: int = 1,
        replication_factor: int = 1,
        client_id: str = "thoth-messaging",
        ssl_auth: Optional[int] = 1,
        bootstrap_server: str = "localhost:9092",
        topic_retention_time_second: int = 60 * 60 * 24 * 45,
        protocol: str = "SSL",
    ):
        """Create general message."""
        self.topic_name = topic_name or "thoth.base-topic"
        self.num_partitions = num_partitions
        self.replication_factor = replication_factor
        self.client_id = os.getenv("KAFKA_CLIENT_ID") or client_id
        self.ssl_auth = os.getenv("KAFKA_SSL_AUTH") or ssl_auth
        self.bootstrap_server = os.getenv("KAFKA_BOOTSTRAP_SERVERS") or bootstrap_server
        self.topic_retention_time_second = topic_retention_time_second
        self.protocol = os.getenv("KAFKA_PROTOCOL") or protocol
        self.ssl_context = None

        if self.ssl_auth:
            self.cafile = os.getenv("KAFKA_CAFILE") "ca.crt"
            self.ssl_context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH, cafile=self.cafile)

        self.app = faust.App(
            self.client_id, broker=self.bootstrap_server, value_serializer="json", ssl_context=self.ssl_context
        )

        self.topic = self.app.topic(
            self.topic_name,
            value_type=None,
            retention=self.bootstrap_server,
            partitions=self.num_partitions,
            internal=True,
        )

    async def publish_to_topic(self, value):
        """Publish to this messages topic."""
        await self.topic.send(value=value)
