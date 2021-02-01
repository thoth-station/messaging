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


"""This is Thoth Messaging module for ProvenanceCheckerTriggerMessage."""

from typing import TypedDict, List
import logging

from .base import BASE_DEFINITIONS, MessageBase, BaseMessageContents

_LOGGER = logging.getLogger(__name__)


definitions = BASE_DEFINITIONS

definitions["provenance_checker_trigger"] = {
    "type": "object",
    "properties": {
        "application_stack": {"type": "object"},
        "debug": {"type": "boolean"},
        # Required ↑↑↑ | ↓↓↓ Optional
        "job_id": {"type": "string"},
        "origin": {"type": "string"},
        "whitelisted_sources": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["application_stack", "debug"],
}

jsonschema = {
    "allOf": [
        {"$ref": "#/definitions/base_message"},
        {"$ref": "#/definitions/provenance_checker_trigger"},
    ],
    "definitions": definitions,
}

provenance_checker_trigger_message = MessageBase(
    jsonschema=jsonschema, base_name="thoth.provenance-checker-trigger", version="v1"
)


class _Required(TypedDict, total=True):
    application_stack: dict
    debug: bool


class _Optional(TypedDict, total=False):
    job_id: str
    origin: str
    whitelisted_sources: List[str]


class ProvenanceCheckerTriggerContents(BaseMessageContents, _Required, _Optional):
    """Message contents for ProvenanceCheckerTrigger messages as specified in _Required and _Optional."""

    pass
