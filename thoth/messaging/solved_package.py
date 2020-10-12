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

import attr
import logging

from .message_base import MessageBase, BaseMessageContents

_LOGGER = logging.getLogger(__name__)


class SolvedPackageMessage(MessageBase):
    """Class used for Solved Package events on Kafka topic."""

    base_name = "thoth.solver.solved-package"

    @attr.s
    class MessageContents(BaseMessageContents):
        """Class used to represent contents of a solved package message Kafka topic."""

        package_name = attr.ib(type=str)
        package_version = attr.ib(type=str)
        index_url = attr.ib(type=str)
        solver = attr.ib(type=str)
        version = attr.ib(type=str, default="v1", init=False)

    def __init__(self):
        """Initialize solved package topic."""
        super(SolvedPackageMessage, self).__init__(
            base_name=self.base_name, value_type=self.MessageContents,
        )
