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
from typing import Optional

from jsonschema import validate

_LOGGER = logging.getLogger(__name__)


BASE_DEFINITIONS = {
    "base_message": {
        "type": "object",
        "properties": {"component_name": {"type": "string"}, "service_version": {"type": "string"},},
        "required": ["component_name", "service_version"],
    }
}


class MessageBase:
    """Class used for Package Release events on Kafka topic."""

    def __init__(self, *, jsonschema: dict, base_name: Optional[str] = None, version: str = "v0"):
        """Create general message."""
        self.base_name = base_name or "thoth.base-topic"
        self.version = version
        self.jsonschema = jsonschema

    @property
    def topic_name(self):
        """Generate topic name."""
        prefix = os.getenv("THOTH_DEPLOYMENT_NAME", None)
        if prefix is not None:
            return f"{prefix}.{self.base_name}"
        return self.base_name

    def _validate_and_append_version(self, message_contents: dict) -> dict:
        validate(message_contents, self.jsonschema)
        to_ret = message_contents
        to_ret["version"] = self.version
        return to_ret
