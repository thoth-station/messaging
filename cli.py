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

"""Messaging CLI to send single message to Kafka using Faust."""

import asyncio
import json
from typing import Optional
import logging

from faust import cli

from thoth.messaging import ALL_MESSAGES
from thoth.messaging import message_factory
from thoth.messaging import MessageBase
from thoth.common import init_logging
from thoth.messaging import __version__
from thoth.common import __version__ as __common__version__

app = MessageBase().app
init_logging()

_LOGGER = logging.getLogger("thoth.messaging")

__service_version__ = f"{__version__}+common.{__common__version__}"

_LOGGER.info("This is Thoth Messaging CLI v%s", __service_version__)


## create cli
@app.command(
    cli.option(
        "--topic-name", "-n", envvar="THOTH_MESSAGING_TOPIC_NAME", type=str, help="Name of topic to send message to.",
    ),
    cli.option(
        "--create-if-not-exist",
        envvar="THOTH_MESSAGING_CREATE_IF_NOT_EXIST",
        default=False,
        help="If topic doesn't already exist on Kafka then create it.",
    ),
    cli.option(
        "--message-contents",
        "-m",
        envvar="THOTH_MESSAGING_MESSAGE_CONTENTS",
        type=str,
        help="JSON representation of message to send including typing hints.",
    ),  # {<name>: {"type":, "value":},...}
    cli.option(
        "--partitions",
        default=1,
        envvar="THOTH_MESSAGING_PARTITIONS",
        type=int,
        help="Number of partitions for this topic.",
    ),
    cli.option(
        "--replication",
        default=1,
        envvar="THOTH_MESSAGING_REPLICATION",
        type=int,
        help="Replication factor of this topic.",
    ),
    cli.option(
        "--topic-retention-time",
        default=60 * 60 * 24 * 25,
        envvar="THOTH_MESSAGING_TOPIC_RETENTION_TIME",
        type=int,
        help="How many seconds a message for this topic should persist after being created.",
    ),
    cli.option(
        "--message-file",  # if present topic_name and message_contents will be ignored
        envvar="THOTH_MESSAGING_FROM_FILE",
        type=str,  # file path to file in json format [{"topic_name": <str>, "message_contents": <dict>}, ...]
    ),
)
async def messaging(
    ctx,
    topic_name: Optional[str],
    create_if_not_exist: bool,
    message_contents: Optional[str],
    partitions: int,
    replication: int,
    topic_retention_time: int,
    message_file: Optional[str],
):
    """Run messaging cli with the given arguments."""
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

    tasks = []

    # NOTE: we don't need to check based on deployment because it is only prepended after we call __init__
    async for m in all_messages:
        m_contents = m["message_contents"]
        m_topic_name = m["topic_name"]
        # get or create message type
        for message in ALL_MESSAGES:
            if m_topic_name == message.topic_name:
                topic = message(
                    num_partitions=partitions,
                    replication_factor=replication,
                    topic_retention_time_second=topic_retention_time,
                )
        else:
            if not create_if_not_exist:
                raise Exception("Topic name does not match messages and message should not be created.")
            message_types = [(i, m_contents[i]["type"]) for i in m_contents]
            topic = message_factory(
                t_name=m_topic_name,
                message_contents=message_types,
                replication_factor=replication,
                num_partitions=partitions,
                topic_retention_time_second=topic_retention_time,
            )()

        message_dict = {i: m_contents[i]["value"] for i in m_contents}
        message = topic.MessageContents(**message_dict)
        await topic.topic.maybe_declare()
        tasks.append(topic.publish_to_topic(message))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()
