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

from .base import BASE_DEFINITIONS, MessageBase

_LOGGER = logging.getLogger(__name__)

definitions = BASE_DEFINITIONS

definitions["package_extract_trigger"] = {
    "type": "object",
    "properties": {
        "debug": {"type": "boolean"},
        "environment_type": {"type": "string"},
        "image": {"type": "string"},
        "is_external": {"type": "boolean"},
        "verify_tls": {"type": "boolean"},
        # Required ↑↑↑ | ↓↓↓ Optional
        "job_id": {"type": "string"},
        "origin": {"type": "string"},
        "registry_user": {"type": "string"},
        "registry_password": {"type": "string"},
    },
    "required": ["debug", "environment_type", "image", "is_external", "verify_tls",],
}

jsonschema = {
    "allOf": [{"$ref": "#/definitions/base_message"}, {"$ref": "#/definitions/package_extract_trigger"},],
    "definitions": definitions,
}

package_extract_trigger_message = MessageBase(
    jsonschema=jsonschema, base_name="thoth.package-extract-trigger", version="v1"
)
