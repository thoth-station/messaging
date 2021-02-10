#!/usr/bin/env python3
# thoth-messaging
# Copyright(C) 2020 Sai Sankar Gochhayat
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


"""This is Thoth Messaging module for KebechetRunUrlTriggerMessage."""

from typing import TypedDict
import logging

from .base import BASE_DEFINITIONS, MessageBase, BaseMessageContents

_LOGGER = logging.getLogger(__name__)

definitions = BASE_DEFINITIONS

definitions["metadata"] = {
    "type": "object",
    "properties": {
        "justification": {"type": "integer", "minimum": 0},
    },
}

definitions["kebechet_run_url"] = {
    "type": "object",
    "properties": {
        # Required ↑↑↑ | ↓↓↓ Optional
        "installation_id": {"type": "string"},
        "job_id": {"type": "string"},
        "metadata": {"$ref": "#definitions/metadata"},
        "service_name": {"type": "string"},
        "url": {"type": "string"},
    },
}


jsonschema = {
    "allOf": [
        {"$ref": "#/definitions/base_message"},
        {"$ref": "#/definitions/kebechet_run_url"},
    ],
    "definitions": definitions,
}

message = MessageBase(jsonschema=jsonschema, base_name="thoth.kebechet-run-url-trigger", version="v2")


class _Metadata(TypedDict, total=False):
    justification: int


class _Required(TypedDict, total=True):
    pass


class _Optional(TypedDict, total=False):
    installation_id: str
    job_id: str
    metadata: _Metadata
    service_name: str
    url: str


class MessageContents(BaseMessageContents, _Required, _Optional):
    """Message contents for KebechetRunUrl messages as specified in _Required and _Optional."""

    pass
