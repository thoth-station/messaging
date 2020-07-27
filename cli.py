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

import json
from typing import Dict

from faust import cli

from thoth.messaging import ALL_MESSAGES
from thoth.messaging import message_factory
from thoth.messaging import MessageBase

app = MessageBase().app


## create cli
@app.command(
    cli.option(
        "--topic-name",
        "-n",
        envvar="THOTH_MESSAGING_TOPIC_NAME",
        required=True,
        type=str,
        help="Name of topic to send message to.",
    ),
    cli.option(
        "--create-if-not-exist",
        envvar="THOTH_MESSAGING_CREATE_IF_NOT_EXIST",
        is_flag=True,
        default=False,
        help="If topic doesn't already exist on Kafka then create it.",
    ),
    cli.option(
        "--message-contents",
        "-m",
        envvar="THOTH_MESSAGING_MESSAGE_CONTENTS",
        required=True,
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
)
async def messaging(
    ctx,
    topic_name: str,
    create_if_not_exist: bool,
    message_contents: str,
    partitions: int,
    replication: int,
    topic_retention_time: int,
):
    """Run messaging cli with the given arguments."""
    loaded_message = json.loads(message_contents)  # type: Dict[str, Dict[str, str]]
    if type(loaded_message) != dict:
        raise ValueError("Message must be in dict representation. {<name>: {value: <value>, type: <type>},...}")

    # get or create message type
    for message in ALL_MESSAGES:
        if topic_name == message.topic_name:
            topic = message(
                num_partitions=partitions,
                replication_factor=replication,
                topic_retention_time_second=topic_retention_time,
            )()
    else:
        if not create_if_not_exist:
            raise Exception("Topic name does not match messages and message should not be created.")
        message_types = [(i, loaded_message[i]["type"]) for i in loaded_message]
        topic = message_factory(
            t_name=topic_name,
            message_contents=message_types,
            replication_factor=replication,
            num_partitions=partitions,
            topic_retention_time_second=topic_retention_time,
        )()

    message_dict = {i: loaded_message[i]["value"] for i in loaded_message}
    message = topic.MessageContents(**message_dict)
    await topic.topic.maybe_declare()
    await topic.publish_to_topic(message)
