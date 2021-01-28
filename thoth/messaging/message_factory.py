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


"""This is Thoth Messaging module for message_factory."""

from .base import MessageBase, BASE_DEFINITIONS


def message_factory(
    b_name: str, jsonschema: dict,
):
    """Create new message types."""
    if "definitions" not in jsonschema:
        jsonschema["definitions"] = {}

    # copy base definitions so they can be used by a user defined schema
    for definition in BASE_DEFINITIONS:
        if definition not in jsonschema["definitions"]:
            jsonschema["definitions"][definition] = BASE_DEFINITIONS[definition]

    return MessageBase(jsonschema=jsonschema, base_name=b_name)
