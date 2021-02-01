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


"""Helper functions for using confluent kafka admin client with thoth.messaging."""

from typing import Optional, Dict
import logging

from .config import kafka_config_from_env, topic_config_from_env
from . import ALL_MESSAGES
from . import MessageBase

from confluent_kafka.admin import AdminClient, NewTopic


_LOGGER = logging.Logger(__name__)


def create_admin_client(config: Optional[Dict[str, str]] = None) -> AdminClient:
    """Create admin client."""
    if config:
        return AdminClient(config)
    return AdminClient(kafka_config_from_env())


def create_all_topics(admin: AdminClient, partitions: int = 1, replication_factor: int = 1):
    """Create admin client for all topics in thoth messaging with equal replication and partitions."""
    # NOTE: topics are only created if they don't exist
    topics = admin.list_topics().topics
    for i in ALL_MESSAGES:
        t_name = i.topic_name
        if t_name in topics:
            continue
        admin.create_topics(
            [
                NewTopic(
                    t_name,
                    partitions,
                    replication_factor=replication_factor,
                    config=topic_config_from_env(),
                )
            ]
        )


def create_topic(admin: AdminClient, message: MessageBase, partitions: int = 1, replication_factor: int = 1):
    """Create single topic."""
    # NOTE: we assume `message` is initialized
    topics = admin.list_topics().topics
    t_name = message.topic_name

    if t_name in topics:
        _LOGGER.warn("Topic %s already exists on Kafka cluster.", t_name)
        return

    admin.create_topics(
        [
            NewTopic(
                message.topic_name,
                partitions,
                replication_factor=replication_factor,
                config=topic_config_from_env(),
            )
        ]
    )
