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


"""Helper functions for using confluent kafka producer with thoth.messaging."""

from typing import Optional, Dict, Any, Union
from json import dumps
import logging

from .config import kafka_config_from_env
from .base import MessageBase, BaseMessageContents

from confluent_kafka import Producer

_LOGGER = logging.getLogger(__name__)


def create_producer(config: Optional[Dict[str, Any]] = None) -> Producer:
    """Create confluent kafka producer."""
    if config is not None:
        return Producer(config)
    return Producer(kafka_config_from_env())


def publish_to_topic(
    producer: Producer, message_type: MessageBase, message_contents: Union[Dict[str, Any], BaseMessageContents]
):
    """Publish to topic using message contents class."""
    producer.produce(
        message_type.topic_name,
        value=dumps(message_type._validate_and_append_version(message_contents)).encode("utf-8"),
    )
    _LOGGER.debug(
        "Sending the following message to topic %s.\n%s",
        message_type.topic_name,
        message_type._validate_and_append_version(message_contents),
    )
