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
import attr

from typing import Optional, Dict, Any

from .message_base import MessageBase, BaseMessageContents

_LOGGER = logging.getLogger(__name__)


class AdviserReRunMessage(MessageBase):
    """Class used for Adviser re run events on Kafka topic."""

    base_name = "thoth.investigator.adviser-re-run"

    @attr.s
    class MessageContents(BaseMessageContents):
        """Class used to represent contents of adviser re run message Kafka topic."""

        re_run_adviser_id = attr.ib(type=str)

        application_stack = attr.ib(type=Dict[Any, Any])
        recommendation_type = attr.ib(type=str)
        runtime_environment = attr.ib(type=Optional[Dict[Any, Any]], default=None)

        origin: Optional[str] = None
        github_event_type: Optional[str] = None
        github_check_run_id: Optional[int] = None
        github_installation_id: Optional[int] = None
        github_base_repo_url: Optional[str] = None

        source_type: Optional[str] = None
        version: str = "v1"

    def __init__(self):
        """Initialize adviser-re-run topic."""
        super(AdviserReRunMessage, self).__init__(
            base_name=self.base_name, value_type=self.MessageContents,
        )
