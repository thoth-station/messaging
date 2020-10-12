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


"""This is Thoth Messaging module for PackageExtractTriggerMessage."""

import logging
import attr
from typing import Optional

from .message_base import MessageBase, BaseMessageContents

_LOGGER = logging.getLogger(__name__)


class PackageExtractTriggerMessage(MessageBase):
    """Class used for Package Extract events on Kafka topic."""

    base_name = "thoth.package-extract-trigger"

    @attr.s
    class MessageContents(BaseMessageContents):
        """Class used to represent contents of a message Kafka topic."""

        image = attr.ib(type=str)
        environment_type = attr.ib(type=str)
        is_external = attr.ib(type=bool, default=True)
        verify_tls = attr.ib(type=bool, default=True)
        debug = attr.ib(type=bool, default=False)
        job_id = attr.ib(type=Optional[str], default=None)
        origin = attr.ib(type=Optional[str], default=None)
        registry_user = attr.ib(type=Optional[str], default=None)
        registry_password = attr.ib(type=Optional[str], default=None)
        version = attr.ib(type=str, default="v1", init=False)

    def __init__(self):
        """Initialize advise-justification topic."""
        super(PackageExtractTriggerMessage, self).__init__(
            base_name=self.base_name, value_type=self.MessageContents,
        )
