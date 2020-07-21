import click

import os
import json
import asyncio
from time import sleep

from faust import cli

from thoth.messaging.hash_mismatch import HashMismatchMessage
from thoth.messaging.message_base import MessageBase
from thoth.messaging.message_factory import message_factory
from thoth.messaging.missing_package import MissingPackageMessage
from thoth.messaging.missing_version import MissingVersionMessage
from thoth.messaging.package_releases import PackageReleaseMessage
from thoth.messaging.unresolved_package import UnresolvedPackageMessage

ALL_MESSAGES = [
    HashMismatchMessage,
    MissingVersionMessage,
    MissingPackageMessage,
    PackageReleaseMessage,
    UnresolvedPackageMessage,
]

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
        default=60*60*24*25,
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
    message_contents = json.loads(message_contents)

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
        message_types = [(i, eval(message_contents[i]["type"])) for i in message_contents]
        topic = message_factory(
            t_name=topic_name,
            message_contents=message_types,
            replication_factor=replication,
            num_partitions=partitions,
            topic_retention_time_second=topic_retention_time,
        )()

    message_dict = {i: message_contents[i]["value"] for i in message_contents}
    message = topic.MessageContents(**message_dict)
    await topic.publish_to_topic(message)
