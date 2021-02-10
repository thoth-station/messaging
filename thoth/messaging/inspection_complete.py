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


"""This is Thoth Messaging module for InspectionCompleteMessage."""

from typing import TypedDict

from .base import BASE_DEFINITIONS, MessageBase, BaseMessageContents

definitions = BASE_DEFINITIONS

definitions["inspection_completed"] = {
    "type": "object",
    "properties": {
        "force_sync": {"type": "boolean"},
        "inspection_id": {"type": "string"},
        # Required ↑↑↑ | ↓↓↓ Optional
    },
    "required": [
        "force_sync",
        "inspection_id",
    ],
}

jsonschema = {
    "allOf": [
        {"$ref": "#/definitions/base_message"},
        {"$ref": "#/definitions/inspection_completed"},
    ],
    "definitions": definitions,
}

message = MessageBase(jsonschema=jsonschema, base_name="thoth.inspection-completed", version="v1")


class _Required(TypedDict, total=True):
    force_sync: bool
    inspection_id: str


class _Optional(TypedDict, total=False):
    pass


class MessageContents(BaseMessageContents, _Required, _Optional):
    """Message contents for InspectionComplete messages as specified in _Required and _Optional."""

    pass
