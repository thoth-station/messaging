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


"""This is Thoth Messaging module for UpdateProvidesSourceDistroMessage."""

from typing import TypedDict
import logging

from .base import BASE_DEFINITIONS, MessageBase, BaseMessageContents

_LOGGER = logging.getLogger(__name__)

definitions = BASE_DEFINITIONS

definitions["update_provides_src_distro"] = {
    "type": "object",
    "properties": {
        "index_url": {"type": "string"},
        "package_name": {"type": "string"},
        "package_version": {"type": "string"},
        "value": {"type": "boolean"},
        # Required ↑↑↑ | ↓↓↓ Optional
    },
    "required": ["index_url", "package_name", "package_version", "value"],
}

jsonschema = {
    "allOf": [
        {"$ref": "#/definitions/base_message"},
        {"$ref": "#/definitions/update_provides_src_distro"},
    ],
    "definitions": definitions,
}

update_provides_src_distro_message = MessageBase(
    jsonschema=jsonschema, base_name="thoth.update-provides-source-distro", version="v1"
)


class _Required(TypedDict, total=True):
    index_url: str
    package_name: str
    package_version: str
    value: bool


class _Optional(TypedDict, total=False):
    pass


class UpdateProvidesSrcDistroContents(BaseMessageContents, _Required, _Optional):
    """Message contents for UpdateProvidesSrcDistroContents messages as specified in _Required and _Optional."""

    pass
