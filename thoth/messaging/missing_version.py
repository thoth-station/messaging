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


"""This is Thoth Messaging module for MissingVersionMessage."""


from .base import BASE_DEFINITIONS, MessageBase


definitions = BASE_DEFINITIONS

definitions["missing_version"] = {
    "type": "object",
    "properties": {
        "index_url": {"type": "string"},
        "package_name": {"type": "string"},
        "package_version": {"type": "string"},
        # Required ↑↑↑ | ↓↓↓ Optional
    },
    "required": ["index_url", "package_name", "package_version"],
}

jsonschema = {
    "allOf": [{"$ref": "#/definitions/base_message"}, {"$ref": "#/definitions/missing_version"},],
    "definitions": definitions,
}

missing_version_message = MessageBase(
    jsonschema=jsonschema, base_name="thoth.package-update.missing-package-version", version="v1"
)
