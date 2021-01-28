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


"""This is Thoth Messaging module for AdviserReRunMessage."""

import logging

from .base import BASE_DEFINITIONS, MessageBase

_LOGGER = logging.getLogger(__name__)


definitions = BASE_DEFINITIONS

definitions["adviser_re_run"] = {
    "type": "object",
    "properties": {
        "re_run_adviser_id": {"type": "string"},
        "application_stack": {"type": "object"},
        "recommendation_type": {"type": "string"},
        # ↑↑↑ Required | Optional ↓↓↓
        "runtime_environment": {"type": "object"},
        "origin": {"type": "string"},
        "github_event_type": {"type": "string"},
        "github_check_run_id": {"type": "string"},
        "github_installation_id": {"type": "integer", "minimum": 0},
        "github_base_repo_url": {"type": "string"},
        "source_type": {"type": "string"},
    },
    "required": ["re_run_adviser_id", "application_stack", "recommendation_type",],
}

jsonschema = {
    "allOf": [{"$ref": "#/definitions/base_message"}, {"$ref": "#/definitions/adviser_re_run"},],
    "definitions": definitions,
}

adviser_re_run_message = MessageBase(jsonschema=jsonschema, base_name="thoth.investigator.adviser-re-run", version="v1")
