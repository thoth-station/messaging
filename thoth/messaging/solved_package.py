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


"""This is Thoth Messaging module for SolvedPackageMessage."""

from typing import TypedDict
import logging

from .base import BASE_DEFINITIONS, MessageBase, BaseMessageContents

_LOGGER = logging.getLogger(__name__)


definitions = BASE_DEFINITIONS

definitions["solved_package"] = {
    "type": "object",
    "properties": {
        "index_url": {"type": "string"},
        "package_name": {"type": "string"},
        "package_version": {"type": "string"},
        "solver": {"type": "string"},
        # Required ↑↑↑ | ↓↓↓ Optional
    },
    "required": ["index_url", "package_name", "package_version", "solver"],
}

jsonschema = {
    "allOf": [
        {"$ref": "#/definitions/base_message"},
        {"$ref": "#/definitions/solved_package"},
    ],
    "definitions": definitions,
}

message = MessageBase(jsonschema=jsonschema, base_name="thoth.solver.solved-package", version="v1")


class _Required(TypedDict, total=True):
    index_url: str
    package_name: str
    package_version: str
    solver: str


class _Optional(TypedDict, total=False):
    pass


class MessageContents(BaseMessageContents, _Required, _Optional):
    """Message contents for SolvedPackage messages as specified in _Required and _Optional."""

    pass
