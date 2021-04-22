Thoth Messaging
---------------

This provides a library called `thoth-messaging
<https://pypi.org/project/thoth-messaging>`_ used in project `Thoth
<https://thoth-station.ninja>`_.  It is a basic module to encapsule all messaging (here it is Kafka via Faust) primitives.

Type Hinting With MyPy
######################
This module uses pydantic for type hinting and enforcing a regular schema in messaging.  If you are using mypy to check
your code please add the following to your mypy configuration file:

.. code-block:: toml
  [mypy]
  plugins = pydantic.mypy

If you are creating an instance of a pydantic model in your own module you should directly use the `MessageContents`
class within the associate message file. Using ``foo_bar_message.model`` will only type hint for `BaseMessageContents`.

Development and Testing
#######################
For development and testing it is very useful to have a local instance of Kafka running on your machine

We provide a ``docker-compose`` file to get you up and running quickly with a basic Kafka server; this file is based on
`Single Zookeeper/Multiple Kafka <https://github.com/simplesteph/kafka-stack-docker-compose#single-zookeeper--multiple-kafka>`__.

In order to start Zookeeper as well as the Kafka Servers simply run `$ podman-compose up` or `$ docker-compose up`,
choose the appropriate option based on the system which you are using.

Once you have Kafka up and running you should be ready to begin coding your own messaging producers and consumers.  The
interface between `Kafka` and `Python` is handled by a library called `Confluent Kafka <https://docs.confluent.io/current/clients/python.html>`__.
Faust's documentation will be extremely helpful to you when you are developing your own applications. If you would like
examples of producers and consumers from Team Thoth, look at the following two repositories,
`investigator <https://github.com/thoth-station/investigator>`__ and `package-update <https://github.com/thoth-station/package-update-job>`__.

You may find it useful to use console producers and consumers while testing your, to create one simply attach a bash shell
to one of your Kafka Servers by running: `$ podman exec -it messaging_kafka1_1 bash`, your container names should be
the same as given here, if not, run `$ podman ps` and choose the correct container.  These containers have all Kafka
binaries in appropriate places so you can simply run `$ kafka-console-consumer`, `$ kafka-console-producer`, or any other
kafka command that you may find useful.

*example:*

.. code-block:: console

  kafka-console-consumer --bootstrap-server localhost:9092 --topic test --from-beginning

You can test sending a message via the CLI using a file as -

*example:*

.. code-block:: console

  pipenv shell
  python cli.py --message-file messages_to_be_sent.json

*Note*
Data is not persistent. Once pods are deleted so is the data associated with them.

Pitfalls
########

Some schemas in this library are defined as `Dict[str, Any]`.  This usually does not accurately reflect the actual
schema required. These schemas can be purposefully vague because they are defined elsewhere and importing them from
the requisite libraries couples `thoth-messaging` version too closely to other components in the best case, and
introduces circular dependencies in the worst case.  In short, `thoth-messaging` is naive and can only enforce schemas
which it has defined.
