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
import logging

from .config import kafka_config_from_env
from .message_base import MessageBase, BaseMessageContents

from confluent_kafka import Producer

_LOGGER = logging.getLogger(__name__)


def create_producer(config: Optional[Dict[str, Any]] = None) -> Producer:
    """Create confluent kafka producer."""
    if config is not None:
        return Producer(config)
    return Producer(kafka_config_from_env())


def publish_to_topic(
    producer: Producer, message_type: MessageBase, message_contents: Union[BaseMessageContents, Dict[str, Any]],
):
    """
    Publish to topic using message contents class.

    Parameters
    ----------
    producer : Producer
        Instance of confluent Kafka producer which handles sending the message to Kafka instance
    message_type : MessageBase
        Message type which determines the schema of the message as well as the topic name to produce to
    message_contents : Union[BaseMessageContents, Dict[str, Any]]
        Message to be sent. A dict is parsed on messaging side to `message_type.model`.

    Returns
    -------
    None

    Raises
    ------
    ValidationError
        When pydantic detects ill formed message
    """
    if type(message_contents) == dict:
        contents = message_type.model.parse_obj(message_contents)
    elif issubclass(type(message_contents), BaseMessageContents):
        message_type.model.validate(message_contents)
        contents = message_contents  # type: ignore

    producer.produce(message_type.topic_name, value=contents.json().encode("utf-8"))
    _LOGGER.debug("Sending the following message to topic %s.\n%s", message_type.topic_name, contents.dict())
