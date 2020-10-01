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
import logging
import ssl
import asyncio

import faust
from faust.types.models import ModelArg
from typing import Optional

_LOGGER = logging.getLogger(__name__)


class BaseMessageContents(faust.Record, serializer="json"):  # type: ignore
    """Default params for message contents."""

    component_name: str  # what component sent the message?
    service_version: str  # what version was that component?


class MessageBase:
    """Class used for Package Release events on Kafka topic."""

    app = None  # type: Optional[faust.App]
    _base_version = 1  # update on schema change

    def __init__(
        self,
        *,
        topic_name: Optional[str] = None,
        value_type: Optional[ModelArg] = None,
        num_partitions: int = 1,
        replication_factor: int = 1,
        client_id: str = "thoth-messaging",
        ssl_auth: int = 1,
        bootstrap_server: str = "localhost:9092",
        topic_retention_time_second: int = 60 * 60 * 24 * 45,
        protocol: str = "SSL",
        message_version: int = 0,
    ):
        """Create general message."""
        topic_prefix = os.getenv("THOTH_DEPLOYMENT_NAME", None)
        self.topic_name = topic_name or "thoth.base-topic"
        if topic_prefix is not None:
            self.topic_name = f"{topic_prefix}.{self.topic_name}"
        self.version = f"{self._base_version}.{message_version}"
        self.value_type = value_type
        self.num_partitions = num_partitions
        self.replication_factor = replication_factor
        self.client_id = os.getenv("KAFKA_CLIENT_ID") or client_id
        self.ssl_auth = os.getenv("KAFKA_SSL_AUTH") or ssl_auth
        self.bootstrap_server = os.getenv("KAFKA_BOOTSTRAP_SERVERS") or bootstrap_server
        self.topic_retention_time_second = topic_retention_time_second
        self.protocol = os.getenv("KAFKA_PROTOCOL") or protocol

        if MessageBase.app is None:
            self.start_app()

        self.topic = MessageBase.app.topic(  # type: ignore
            self.topic_name,
            value_type=self.value_type,
            retention=self.topic_retention_time_second,
            partitions=self.num_partitions,
            internal=True,
        )

    def start_app(self):
        """Start Faust app."""
        self.ssl_context = None
        db_store = os.getenv("THOTH_MESSAGING_DB_LOCATION", None)
        if self.ssl_auth == 1:
            self.cafile = os.getenv("KAFKA_CAFILE") or "ca.crt"
            self.ssl_context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH, cafile=self.cafile)
        if db_store is None:
            app = faust.App(
                self.client_id, broker=self.bootstrap_server, value_serializer="json", ssl_context=self.ssl_context
            )
        else:
            app = faust.App(
                self.client_id,
                broker=self.bootstrap_server,
                value_serializer="json",
                ssl_context=self.ssl_context,
                store="rocksdb://",
                datadir=db_store,
            )
        MessageBase.app = app

    async def publish_to_topic(self, value):
        """Publish to this messages topic."""
        await self.topic.send(value=value)

    def sync_publish_to_topic(self, value):
        """Publish to topic synchronously."""
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.publish_to_topic(value=value))
