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

"""This is Thoth Messaging module for UnrevsolvedPackageMessage."""

from typing import TypedDict
import logging

from .base import BASE_DEFINITIONS, MessageBase, BaseMessageContents

_LOGGER = logging.getLogger(__name__)


definitions = BASE_DEFINITIONS

definitions["unrevsolved_package"] = {
    "type": "object",
    "properties": {
        "package_name": {"type": "string"},
        "package_version": {"type": "string"},
        # Required ↑↑↑ | ↓↓↓ Optional
    },
    "required": ["package_name", "package_version"],
}

jsonschema = {
    "allOf": [
        {"$ref": "#/definitions/base_message"},
        {"$ref": "#/definitions/unrevsolved_package"},
    ],
    "definitions": definitions,
}

unrevsolved_package_message = MessageBase(
    jsonschema=jsonschema, base_name="thoth.investigator.unrevsolved-package", version="v1"
)


class _Required(TypedDict, total=True):
    package_name: str
    package_version: str


class _Optional(TypedDict, total=False):
    pass


class UnrevsolvedPackageContents(BaseMessageContents, _Required, _Optional):
    """Message contents for UnrevsolvedPackage messages as specified in _Required and _Optional."""

    pass
