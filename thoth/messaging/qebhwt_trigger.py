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


"""This is Thoth Messaging module for QebHwtTriggerMessage."""

import logging

from .base import BASE_DEFINITIONS, MessageBase

_LOGGER = logging.getLogger(__name__)

definitions = BASE_DEFINITIONS

definitions["qebhwt_trigger"] = {
    "type": "object",
    "properties": {
        "github_base_repo_url": {"type": "string"},
        "github_check_run_id": {"type": "integer", "minimum": 0},
        "github_event_type": {"type": "string"},
        "github_head_repo_url": {"type": "string"},
        "github_installation_id": {"type": "integer", "minimum": 0},
        "host": {"type": "string"},
        "origin": {"type": "string"},
        "revision": {"type": "string"},
        # Required ↑↑↑ | ↓↓↓ Optional
        "job_id": {"type": "string"},
    },
    "required": [
        "github_base_repo_url",
        "github_check_run_id",
        "github_event_type",
        "github_head_repo_url",
        "github_installation_id",
        "host" "origin",
        "revision",
    ],
}

jsonschema = {
    "allOf": [{"$ref": "#/definitions/base_message"}, {"$ref": "#/definitions/qebhwt_trigger"},],
    "definitions": definitions,
}

qebhwt_trigger_message = MessageBase(jsonschema=jsonschema, base_name="thoth.qebhwt-trigger", version="v1")
