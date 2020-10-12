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


"""This is Thoth Messaging module for message_factory."""

import attr
from typing import Tuple
from typing import Dict  # noqa
from typing import List
from typing import Set  # noqa
from keyword import iskeyword

from .message_base import MessageBase, BaseMessageContents

TYPE_SET = {
    "str",
    "int",
    "float",
    "bool",
    "complex",
    "bytes",
    "bytearray",
    "Tuple",
    "Dict",
    "List",
    "Set",
}


def message_factory(
    t_name: str,
    message_contents: List[Tuple[str, str]],
    num_partitions: int = 1,
    replication_factor: int = 1,
    client_id: str = "thoth-messaging",
    ssl_auth: int = 1,
    bootstrap_server: str = "localhost:9092",
    topic_retention_time_second: int = 60 * 60 * 24 * 45,
    protocol: str = "SSL",
):
    """Create new message types dynamically."""
    for i in message_contents:
        if not i[0].isidentifier() or iskeyword(i[0]) or i[0].startswith("__") or not i[1] in TYPE_SET:
            raise ValueError('Message contents are illformed and may be malicious. ("%r", "%r")', i[0], i[1])

    class NewMessage(MessageBase):
        """Class used for any events on Kafka topic."""

        base_name = t_name
        # we cannot have a message version for message factory so it will just default to v{message_base}.0

        class MessageContents(BaseMessageContents):
            """Class used to represent a contents of a faust message Kafka topic."""

            for item in message_contents:
                exec(f"{item[0]} = attr.ib(type={item[1]})")

            def __init__(self, **kwargs):
                # Go through attributes provided by message contents and if it is passed to __init__ set attribute to
                # the value that was passed
                for k, _ in message_contents:
                    if kwargs.get(k) is None:
                        raise RuntimeError(f"{k} was not supplied or the wrong type was passed.")
                    setattr(self, k, kwargs.get(k))

        def __init__(self):
            """Initialize arbitrary topic."""
            super(NewMessage, self).__init__(
                base_name=self.base_name, value_type=self.MessageContents,
            )

    return NewMessage
