Thoth Messaging
---------------

This provides a library called `thoth-messaging
<https://pypi.org/project/thoth-messaging>`_ used in project `Thoth
<https://thoth-station.ninja>`_.  It is a basic module to encapsule all messaging (here it is Kafka via Faust) primitives.

Message Factory
###############
For the purposes of `Thoth` we have a few of our custom messages defined within the messaging module.  However, we
wanted to allow individuals to be able to use our module without having to add their own messages first.  For testing
and development purposes you can use `message_factory(...)` which allows you to create arbitrary messages using
`thoth-messaging` using the following syntax:

.. code-block:: python

    message_factory(t_name=<str>, message_contents=<Tuple[str, str]>, [num_partitions=<int>], [replication_factor=<int>])

bracketed arguments are optional.

Development and Testing
#######################
For development and testing it is very useful to have a local instance of Kafka running on your machine

We provide a docker-compose file to get you up and running quickly with a basic Kafka server; this file is based on
`Single Zookeeper/Multiple Kafka <https://github.com/simplesteph/kafka-stack-docker-compose#single-zookeeper--multiple-kafka>`__.

In order to start Zookeeper as well as the Kafka Servers simply run `$ podman-compose up` or `$ docker-compose up`,
choose the appropriate option based on the system which you are using.

Once you have Kafka up and running you should be ready to begin coding your own messaging producers and consumers.  The
interface between `Kafka` and `Python` is handled by a library called `Faust <https://faust.readthedocs.io/en/latest/>`__.
Faust's documentation will be extremely helpful to you when you are developing your own applications. If you would like
examples of producers and consumers from Team Thoth, look at the following two repositories,
`investigator <https://github.com/thoth-station/investigator>`__ and `package-update <https://github.com/thoth-station/package-update-job>`__.

You may find it useful to use console producers and consumers while testing your, to create one simply attach a bash shell
to one of your Kafka Servers by running: `$ podman exec -it messaging_kafka1_1 bash`, your container names should be
the same as given here, if not, run `$ podman ps` and choose the correct container.  These containers have all Kafka
binaries in appropriate places so you can simply run `$ kafka-console-consumer`, `$ kafka-console-producer`, or any other
kafka command that you may find useful.

example:
```
$ kafka-console-consumer --bootstrap-server localhost:9092 --topic test --from-beginning
```

*Note*
Data is not persistent. Once pods are deleted so is the data associated with them.

*Note*
Faust producers and consumers can't be run by calling `$ python producer.py`, instead they are Faust specific applications,
in order to run them you need to call `faust -A <filename> <function> [options]`
