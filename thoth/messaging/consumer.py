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


"""Helper functions for using confluent kafka consumer with thoth.messaging."""

from typing import Optional, Dict

from .config import kafka_config_from_env
from .message_base import MessageBase
from . import ALL_MESSAGES

from confluent_kafka import Consumer


def create_consumer(config: Optional[Dict[str, str]] = None) -> Consumer:
    """Initialize consumer."""
    if config:
        return Consumer(config)
    return Consumer(kafka_config_from_env())


def subscribe_to_all(consumer: Consumer):
    """Subscribe to all topics defined in messaging."""
    to_subscribe = []
    for i in ALL_MESSAGES:
        to_subscribe.append(i.topic_name)

    consumer.subscribe(to_subscribe)


def subscribe_to_message(consumer: Consumer, message_type: MessageBase):
    """Subscribe to specific message by passing message class."""
    # NOTE: be sure to initialize message_type before passing
    to_subscribe = consumer.list_topics().topics
    if message_type.topic_name not in to_subscribe:
        to_subscribe.append(message_type.topic_name)
    consumer.subscribe(to_subscribe)  # subscribe overrides all current subscriptions so to maintain previous
    # subscriptions they need to be added to the function call
