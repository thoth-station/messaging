#!/usr/bin/env python3
# thoth-messaging
# Copyright(C) 2021 Fridolin Pokorny
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


"""This is Thoth Messaging module for BuildAnalysisTriggerMessage."""

import logging
from typing import TypedDict

from .base import BASE_DEFINITIONS, MessageBase, BaseMessageContents

_LOGGER = logging.getLogger(__name__)


definitions = BASE_DEFINITIONS

definitions["build_analysis_trigger"] = {
    "type": "object",
    "properties": {
        "base_registry_verify_tls": {"type": "boolean"},
        "debug": {"type": "boolean"},
        "output_registry_verify_tls": {"type": "boolean"},
        # Required ↑↑↑ | ↓↓↓ Optional
        "base_image": {"type": "string"},
        "base_image_analysis_id": {"type": "string"},
        "base_registry_password": {"type": "string"},
        "base_registry_user": {"type": "string"},
        "buildlog_document_id": {"type": "string"},
        "buildlog_parser_id": {"type": "string"},
        "environment_type": {"type": "string"},
        "job_id": {"type": "string"},
        "origin": {"type": "string"},
        "output_image": {"type": "string"},
        "output_image_analysis_id": {"type": "string"},
        "output_registry_password": {"type": "string"},
        "output_registry_user": {"type": "string"},
    },
    "required": ["base_registry_verify_tls", "debug", "output_registry_verify_tls"],
}

jsonschema = {
    "allOf": [
        {"$ref": "#/definitions/base_message"},
        {"$ref": "#/definitions/build_analysis_trigger"},
    ],
    "definitions": definitions,
}

build_analysis_trigger_message = MessageBase(
    jsonschema=jsonschema, base_name="thoth.build-analysis-trigger", version="v1"
)


class _Required(TypedDict, total=True):
    base_registry_verify_tls: bool
    debug: bool
    output_registry_verify_tls: bool


class _Optional(TypedDict, total=False):
    base_image: str
    base_image_analysis_id: str
    base_registry_password: str
    base_registry_user: str
    buildlog_document_id: str
    buildlog_parser_id: str
    environment_type: str
    job_id: str
    origin: str
    output_image: str
    output_image_analysis_id: str
    output_registry_password: str
    output_registry_user: str


class BuildAnalysisTriggerContents(BaseMessageContents, _Required, _Optional):
    """Message contents for BuildAnalysisTrigger messages as specified in _Required and _Optional."""

    pass
