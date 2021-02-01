#!/usr/bin/env python3
# thoth-messaging
# Copyright(C) 2020 Francesco Murdaca
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


"""This is Thoth Messaging module for AdviseJustificationMessage."""

import logging
from typing import TypedDict

from .base import BASE_DEFINITIONS, MessageBase, BaseMessageContents

_LOGGER = logging.getLogger(__name__)

definitions = BASE_DEFINITIONS

definitions["advise_justification"] = {
    "type": "object",
    "properties": {
        "message": {"type": "string"},
        "justification_type": {"type": "string"},
        "count": {"type": "integer", "minimum": 0},
        "adviser_version": {"type": "string"},
    },
    "required": ["message", "justification", "count", "adviser_version"],
}

jsonschema = {
    "allOf": [
        {"$ref": "#/definitions/base_message"},
        {"$ref": "#/definitions/advise_justification"},
    ],
    "definitions": definitions,
}

advise_justification_message = MessageBase(
    jsonschema=jsonschema, base_name="thoth.advise-reporter.advise-justification", version="v1"
)


class _Required(TypedDict, total=True):
    message: str
    justification_type: str
    count: int
    adviser_version: str


class _Optional(TypedDict, total=False):
    pass


class AdviseJustificationContents(BaseMessageContents, _Required, _Optional):
    """Message contents for AdviseJustification messages as specified in _Required and _Optional."""

    pass
