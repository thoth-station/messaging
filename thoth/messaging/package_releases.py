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


"""This is Thoth Messaging module for PackageReleasedMessage."""

from typing import TypedDict

from .base import BASE_DEFINITIONS, MessageBase, BaseMessageContents


definitions = BASE_DEFINITIONS

definitions["package_release"] = {
    "type": "object",
    "properties": {
        "index_url": {"type": "string"},
        "package_name": {"type": "string"},
        "package_version": {"type": "string"},
        # Required ↑↑↑ | ↓↓↓ Optional
    },
    "required": ["index_url", "package_name", "package_version"],
}

jsonschema = {
    "allOf": [
        {"$ref": "#/definitions/base_message"},
        {"$ref": "#/definitions/package_release"},
    ],
    "definitions": definitions,
}

package_released_message = MessageBase(
    jsonschema=jsonschema, base_name="thoth.package-release.package-released", version="v1"
)


class _Required(TypedDict, total=True):
    index_url: str
    package_name: str
    package_version: str


class _Optional(TypedDict, total=False):
    pass


class PackageReleasedContents(BaseMessageContents, _Required, _Optional):
    """Message contents for PackageReleases messages as specified in _Required and _Optional."""

    pass
