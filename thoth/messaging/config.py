import os

# For more configuration options go to https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
# and add them to these dictionaries

confluent_config = {
    "bootstrap.servers": ("KAFKA_BOOTSTRAP_SERVERS", str),
    "client.id": ("KAFKA_CLIENT_ID", str),
    "message.max.bytes": ("KAFKA_MESSAGE_MAX_BYTES", int),
    "receive.message.max.bytes": ("KAFKA_RECEIVE_MESSAGE_MAX_BYTES", int),
    "security.protocol": ("KAFKA_SECURITY_PROTOCOL", str),
    "ssl.certificate.location": ("KAFKA_SSL_CERTIFICATE_LOCATION", str),
    "ssl.endpoint.identification.algorithm": ("KAFKA_SSL_ENDPOINT_IDENTIFICATION_ALGORITHM", str),
    "sasl.mechanism": ("KAFKA_SASL_MECHANISM", str),
    "sasl.username": ("KAFKA_SASL_USERNAME", str),
    "sasl.password": ("KAFKA_SASL_PASSWORD", str),
    "group.id": ("KAFKA_CONSUMER_GROUP_ID", str),
    "group.instance.id": ("KAFKA_CONSUMER_GROUP_INSTANCE_ID", str),
    "max.poll.interval.ms": ("KAFKA_CONSUMER_MAX_POLL_INTERVAL_MS", float),
    "enable.auto.commit": ("KAFKA_CONSUMER_ENABLE_AUTO_COMMIT", bool),
}

topic_config = {
    "compression.type": ("KAFKA_TOPIC_PRODUCER_COMPRESSION_TYPE", str),
    "compression.level": ("KAFKA_TOPIC_PRODUCER_COMPRESSION_LEVEL", int),
    "enable.auto.commit": ("KAFKA_TOPIC_CONSUMER_ENABLE_AUTO_COMMIT", bool),
}


def kafka_config_from_env():
    config = dict()
    for k in confluent_config:
        value = os.getenv(confluent_config[k][0], None)
        if value:
            if confluent_config[k][1] is bool:
                config[k] = value.title() != "False"
            else:
                config[k] = confluent_config[k][1](value)
    return config


def topic_config_from_env():
    config = dict()
    for k in topic_config:
        value = os.getenv(topic_config[k][0], None)
        if value:
            if topic_config[k][1] is bool:
                config[k] = value.title() != "False"
            else:
                config[k] = topic_config[k][1](value)
    return config
