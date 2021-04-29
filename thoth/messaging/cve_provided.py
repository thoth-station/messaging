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


"""This is Thoth Messaging module for CVEProvidedMessage."""

from .message_base import MessageBase, BaseMessageContents

from pydantic import StrictStr

base_name = "thoth.cve-update.cve-provided"


class MessageContents(BaseMessageContents):
    """Class used to represent contents of a cve-provided message Kafka topic."""

    package_name: StrictStr
    package_version: StrictStr
    index_url: StrictStr
    version: StrictStr = "v1"


cve_provided_message = MessageBase(base_name=base_name, model=MessageContents)
