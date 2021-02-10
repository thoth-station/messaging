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


"""This is Thoth Messaging module for AdviseTriggerMessage."""

import logging
from typing import TypedDict

from .base import BASE_DEFINITIONS, MessageBase, BaseMessageContents

_LOGGER = logging.getLogger(__name__)

definitions = BASE_DEFINITIONS

definitions["adviser_trigger"] = {
    "type": "object",
    "properties": {
        "application_stack": {"type": "object"},
        "recommendation_type": {"type": "string"},
        "dev": {"type": "boolean"},
        "debug": {"type": "boolean"},
        # ↑↑↑ Required | Optional ↓↓↓
        "count": {"type": "integer", "minimum": 0},
        "limit": {"type": "integer", "minimum": 0},
        "runtime_environment": {"type": "object"},
        "library_usage": {"type": "object"},
        "origin": {"type": "string"},
        "job_id": {"type": "string"},
        "limit_latest_versions": {"type": "integer", "minimum": 0},
        "github_event_type": {"type": "string"},
        "github_check_run_id": {"type": "string"},
        "github_installation_id": {"type": "integer", "minimum": 0},
        "github_base_repo_url": {"type": "string"},
        "re_run_adviser_id": {"type": "string"},
        "source_type": {"type": "string"},
    },
    "required": [
        "application_stack",
        "recommendation_type",
        "dev",
        "debug",
    ],
}

jsonschema = {
    "allOf": [
        {"$ref": "#/definitions/base_message"},
        {"$ref": "#/definitions/adviser_trigger"},
    ],
    "definitions": definitions,
}

message = MessageBase(jsonschema=jsonschema, base_name="thoth.adviser-trigger", version="v1")


class _Required(TypedDict, total=True):
    application_stack: dict
    recommendation_type: str
    dev: bool
    debug: bool


class _Optional(TypedDict, total=False):
    count: int
    limit: int
    runtime_environment: dict
    library_usage: dict
    origin: str
    job_id: str
    limit_latest_versions: int
    github_event_type: str
    github_check_run_id: str
    github_installation_id: int
    github_base_repo_url: str
    re_run_adviser_id: str
    source_type: str


class MessageContents(BaseMessageContents, _Required, _Optional):
    """Adviser trigger contents, as specified in _Required and _Optional."""

    pass
