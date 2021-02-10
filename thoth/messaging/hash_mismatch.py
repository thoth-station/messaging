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


"""This is Thoth Messaging module for HashMismatchMessage."""

import logging
from typing import TypedDict, List

from .base import BASE_DEFINITIONS, MessageBase, BaseMessageContents

_LOGGER = logging.getLogger(__name__)

definitions = BASE_DEFINITIONS

definitions["hash_mismatch"] = {
    "type": "object",
    "properties": {
        "index_url": {"type": "string"},
        "missing_from_database": {"type": "array", "items": {"type": "string"}},
        "missing_from_source": {"type": "array", "items": {"type": "string"}},
        "package_name": {"type": "string"},
        "package_version": {"type": "string"},
        # Required ↑↑↑ | ↓↓↓ Optional
    },
    "required": [
        "index_url",
        "missing_from_source",
        "missing_from_database",
        "package_name",
        "package_version",
    ],
}

jsonschema = {
    "allOf": [
        {"$ref": "#/definitions/base_message"},
        {"$ref": "#/definitions/hash_mismatch"},
    ],
    "definitions": definitions,
}

message = MessageBase(jsonschema=jsonschema, base_name="thoth.package-update.hash-mismatch", version="v1")


class _Required(TypedDict, total=True):
    index_url: str
    missing_from_database: List[str]
    missing_from_source: List[str]
    package_name: str
    package_version: str


class _Optional(TypedDict, total=False):
    pass


class MessageContents(BaseMessageContents, _Required, _Optional):
    """Message contents for HashMismatch messages as specified in _Required and _Optional."""

    pass
