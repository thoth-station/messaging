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


"""This is Thoth Messaging module for KebechetTriggerMessage."""

import logging

from .base import BASE_DEFINITIONS, MessageBase

_LOGGER = logging.getLogger(__name__)

definitions = BASE_DEFINITIONS

definitions["kebechet_trigger"] = {
    "type": "object",
    "properties": {
        "webhook_payload": {"type": "object"},
        # Required ↑↑↑ | ↓↓↓ Optional
        "job_id": {"type": "string"},
    },
    "required": ["webhook_payload"],
}

jsonschema = {
    "allOf": [{"$ref": "#/definitions/base_message"}, {"$ref": "#/definitions/kebechet_trigger"},],
    "definitions": definitions,
}

kebechet_trigger_message = MessageBase(jsonschema=jsonschema, base_name="thoth.kebechet-trigger", version="v1")
