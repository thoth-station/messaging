#!/usr/bin/env python3
# thoth-messaging
# Copyright(C) 2019, 2020 Red Hat, Inc.
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
import json
import logging

import kafka

from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic


_LOGGER = logging.getLogger(__name__)


KAFAK_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
KAFKA_CAFILE = os.getenv("KAFKA_CAFILE", "ca.crt")


def create_topic(topic: str, num_partitions: int = 1, replication_factor: int = 1):
    """Create the topic on our Kafka broker."""
    topic_list = []

    topic_list.append(NewTopic(name=topic, num_partitions=num_partitions, replication_factor=replication_factor))

    # TODO some error handling would be nice

    admin_client = KafkaAdminClient(
        bootstrap_servers=KAFAK_BOOTSTRAP_SERVERS,
        client_id="thoth_messaging",
        security_protocol="SSL",
        ssl_cafile=KAFKA_CAFILE,
    )
    admin_client.create_topics(new_topics=topic_list, validate_only=False)


def publish_to_topic(topic: str, payload: dict):
    """Publish the given dict to a Kafka topic."""
    producer = None

    if producer is None:
        _LOGGER.debug("KafkaProducer was not connected, trying to reconnect...")
        try:
            producer = KafkaProducer(
                bootstrap_servers=KAFAK_BOOTSTRAP_SERVERS,
                acks=0,  # Wait for leader to write the record to its local log only.
                compression_type="gzip",
                value_serializer=lambda v: json.dumps(v).encode("utf-8"),
                security_protocol="SSL",
                ssl_cafile=KAFKA_CAFILE,
            )
        except kafka.errors.NoBrokersAvailable as excptn:
            _LOGGER.exception("while trying to reconnect KafkaProducer: we failed...")

    try:
        future = producer.send(topic, payload)
        result = future.get(timeout=6)
        _LOGGER.debug(result)
    except AttributeError as excptn:
        _LOGGER.debug(excptn)
    except (kafka.errors.NotLeaderForPartitionError, kafka.errors.KafkaTimeoutError) as excptn:
        producer.close()
        producer = None
        _LOGGER.exception(excptn)
