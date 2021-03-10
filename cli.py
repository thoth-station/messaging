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

"""Messaging CLI to send single message to Kafka using Confluent Kafka."""

import click as cli
import json
from typing import Optional
import logging

from thoth.messaging import ALL_MESSAGES, BaseMessageContents
from thoth.messaging import message_factory
import thoth.messaging.admin_client as admin_client
import thoth.messaging.producer as producer
from thoth.common import init_logging
from thoth.messaging import __version__
from thoth.common import __version__ as __common__version__

_LOGGER = logging.getLogger("thoth.messaging")

__service_version__ = f"{__version__}+common.{__common__version__}"

_LOGGER.info("This is Thoth Messaging CLI v%s", __service_version__)

init_logging()


@cli.command()
@cli.option(
    "--partitions",
    default=1,
    envvar="THOTH_MESSAGING_PARTITIONS",
    type=int,
    help="Number of partitions for this topic.",
)
@cli.option(
    "--replication",
    default=1,
    envvar="THOTH_MESSAGING_REPLICATION",
    type=int,
    help="Replication factor for this topic.",
)
@cli.option(
    "--topic-name",
    "-n",
    envvar="THOTH_MESSAGING_TOPIC_NAME",
    type=str,
    help="Name of topic to send message to — excluding prefix.",
    required=False,
)
@cli.option(
    "--create-if-not-exist",
    envvar="THOTH_MESSAGING_CREATE_IF_NOT_EXIST",
    default=False,
    help="If topic doesn't already exist on Kafka then create it.",
    flag_value=True,
)
@cli.option(
    "--message-contents",
    "-m",
    envvar="THOTH_MESSAGING_MESSAGE_CONTENTS",
    type=str,
    help="JSON representation of message to send including typing hints.",
    required=False,
)  # {<name>: {"type":, "value":},...}
@cli.option(
    "--message-file",  # if present topic_name and message_contents will be ignored
    envvar="THOTH_MESSAGING_FROM_FILE",
    type=str,  # file path to file in json format [{"topic_name": <str>, "message_contents": <dict>}, ...]
    required=False,
)
def messaging(
    partitions: int,
    replication: int,
    topic_name: Optional[str],
    create_if_not_exist: bool,
    message_contents: Optional[str],
    message_file: Optional[str],
):
    """Run messaging cli with the given arguments."""
    admin = admin_client.create_admin_client()
    prod = producer.create_producer()
    if message_file:
        if topic_name or message_contents:
            _LOGGER.warning("Topic name and/or message contents are being ignored due to presence of message file.")
        with open(message_file, "r") as m_file:
            all_messages = json.load(m_file)

    else:
        if topic_name is None or message_contents is None:
            raise AttributeError("Both topic_name and message_contents must be set when not reading from file.")

        temp_message = {}
        temp_message["message_contents"] = json.loads(message_contents)
        temp_message["topic_name"] = topic_name
        all_messages = [temp_message]

    # NOTE: we don't need to check based on deployment because it is only prepended after we call __init__
    for m in all_messages:
        m_contents = m["message_contents"]
        if "component_name" not in m_contents:
            m_contents["component_name"] = "messaging-cli"
        if "service_version" not in m_contents:
            m_contents["service_version"] = __version__
        m_base_name = m["topic_name"]

        validate: bool
        # get or create message type
        for message in ALL_MESSAGES:
            if m_base_name == message.base_name:
                _LOGGER.info(f"Found message in registered list: {m_base_name}")
                topic = message
                validate = True
                break
        else:
            validate = False
            _LOGGER.info("Message not in the registered list checking topics on Kafka...")

            kafka_topic_list = admin.list_topics().topics
            topic = message_factory(b_name=m_base_name, message_model=BaseMessageContents)

            if topic.topic_name not in kafka_topic_list:
                if not create_if_not_exist:
                    raise Exception("Topic name does not match messages and message should not be created.")
                _LOGGER.info("Creating new topic.")
                admin_client.create_topic(admin, topic, partitions=partitions, replication_factor=replication)

        producer.publish_to_topic(prod, topic, m_contents, validate=validate)

        _LOGGER.info(f"Sent message {topic.topic_name} with content: {m_contents}")


if __name__ == "__main__":
    messaging()
