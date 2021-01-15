#!/usr/bin/env python3
# thoth-messaging
# Copyright(C) 2020 Kevin Postlethwait, Francesco Murdaca
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
import logging
import attr
from typing import Any
from typing import Dict
from typing import Optional

_LOGGER = logging.getLogger(__name__)


@attr.s
class BaseMessageContents:
    """Default params for message contents."""

    component_name = attr.ib(type=str)  # what component sent the message?
    service_version = attr.ib(type=str)  # what version was that component?

    def dumps(self) -> Dict[str, Any]:
        """Serialize the message content."""
        return attr.asdict(self)


class MessageBase:
    """Class used for Package Release events on Kafka topic."""

    def __init__(
        self, *, base_name: Optional[str] = None, value_type: Optional[BaseMessageContents] = None,
    ):
        """Create general message."""
        self.base_name = base_name or "thoth.base-topic"
        self.value_type = value_type

    @property
    def topic_name(self):
        """Generate topic name."""
        prefix = os.getenv("THOTH_DEPLOYMENT_NAME", None)
        if prefix is not None:
            return f"{prefix}.{self.base_name}"
        return self.base_name
