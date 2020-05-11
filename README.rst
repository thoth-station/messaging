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

```
message_factory(t_name=<str>, message_contents=<dict<str, type>>, [num_partitions=<int>], [replication_factor=<int>])
```
bracketed arguments are optional.