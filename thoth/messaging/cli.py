import click

import os
import json

from hash_mismatch import HashMismatchMessage
from message_base import MessageBase
from message_factory import message_factory
from missing_package import MissingPackageMessage
from missing_version import MissingVersionMessage
from package_releases import PackageReleaseMessage
from unresolved_package import UnresolvedPackageMessage

ALL_MESSAGES = [
    HashMismatchMessage,
    MissingVersionMessage,
    MissingPackageMessage,
    PackageReleaseMessage,
    UnresolvedPackageMessage,
]

## create cli
@click.command()
@click.pass_context
@click.argument(
    "--topic-name",
    "-n",
    envvar="THOTH_MESSAGING_TOPIC_NAME",
    help="Name of topic to send message to."
    required=True,
    type=str,
)
@click.argument(
    "--create-if-not-exist",
    envvar="THOTH_MESSAGING_CREATE_IF_NOT_EXIST",
    is_flag=True,
    default=False,
    help="If topic doesn't already exist on Kafka then create it.",
)
@click.argument(
    "message-contents",
    "-m",
    envvar="THOTH_MESSAGING_MESSAGE_CONTENTS",
    help="JSON representation of message to send including typing hints."
    required=True,
    type=str,
)  # {<name>: {"type":, "value":},...}
@click.argument(
    "--kafka_bootstrap",
    "-b",
    default="localhost:9092",
    envvar="KAFKA_BOOTSTRAP_SERVERS",
    help="Address of Kafka bootstrap servers."
    required=True,
    type=str,
)
@click.argument(
    "--kafka-ssl",
    default=0,
    envvar="KAFKA_SSL_AUTH",
    help="Set to 0 if auth type is not SSL.",
    required=True,
    type=int,
)
@click.argument(
    "--partitions",
    default=1,
    envvar="THOTH_MESSAGING_PARTITIONS",
    help="Number of partitions for this topic."
    required=True,
    type=int
)
@click.argument(
    "--replication",
    default=1,
    envvar="THOTH_MESSAGING_REPLICATION"
    help="Replication factor of this topic."
    required=True,
    type=int,
)
@click.argument(
    "--client-id",
    default="thoth-messaging",
    envvar="KAFKA_CLIENT_ID",
    help="Kafka client id."
    required=True,
    type=str,
)
@click.argument(
    "--topic-retention-time",
    default=60*60*24*25,
    envvar="THOTH_MESSAGING_TOPIC_RETENTION_TIME",
    help="How many seconds a message for this topic should persist after being created.",
    required=True,
    type=int,
)
def cli(
    topic_name: str,
    create_if_not_exist: bool,
    message_contents: str,
    kafka_ssl: bool,
    kafka_bootstrap: str,
    partitions: int,
    replication: int,
    client_id: str,
    topic_retention_time: int,
):
    if kafka_ssl:
        os.environ["KAFKA_CAFILE"] = 1

    message_contents = json.loads(message_contents)

    # get or create message type
    for message in ALL_MESSAGES:
        if topic_name == message.topic_name:
            topic = message(
                num_partitions=partitions,
                replication_factor=replication,
                client_id=client_id,
                ssl_auth=int(kafka_ssl),
                bootstrap_server=kafka_bootstrap,
                topic_retention_time_second=topic_retention_time,
            )
    else:
        if not create_if_not_exist:
            raise Exception("Topic name does not match messages and message should not be created.")
        message_types = [(i, eval(message_contents[i]["type"]) for i in message_contents]
        topic = message_factory(
            t_name=topic_name,
            message_contents=message_types,
            replication_factor=replication,
            num_partitions=partitions,
            client_id=client_id,
            ssl_auth=int(kafka_ssl),
            bootstrap_server=bootstrap_server=,
            topic_retention_time_second=topic_retention_time,
        )

    message_dict = {i: message_contents[i]["value"] for i in message_contents} 

    app = topic.start_app()
    topic.create_topic(app=app)
    message = topic.MessageContents(**message_dict)
    topic.publish_to_topic(message)
