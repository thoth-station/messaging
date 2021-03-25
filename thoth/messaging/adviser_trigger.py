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


"""This is Thoth Messaging module for AdviseTriggerMessage."""

import logging
import attr
from typing import Optional, Dict, List, Any

from .message_base import MessageBase, BaseMessageContents

_LOGGER = logging.getLogger(__name__)


class AdviserTriggerMessage(MessageBase):
    """Class used for Advise events on Kafka topic."""

    base_name = "thoth.adviser-trigger"

    @attr.s
    class MessageContents(BaseMessageContents):  # type: ignore
        """Class used to represent contents of a message Kafka topic."""

        recommendation_type = attr.ib(type=str)
        dev = attr.ib(type=bool, default=False)
        debug = attr.ib(type=bool, default=False)
        count = attr.ib(type=Optional[int], default=None)
        limit = attr.ib(type=Optional[int], default=None)
        origin = attr.ib(type=Optional[str], default=None)
        job_id = attr.ib(type=Optional[str], default=None)
        limit_latest_versions = attr.ib(type=Optional[int], default=None)
        github_event_type = attr.ib(type=Optional[str], default=None)
        github_check_run_id = attr.ib(type=Optional[int], default=None)
        github_installation_id = attr.ib(type=Optional[int], default=None)
        github_base_repo_url = attr.ib(type=Optional[str], default=None)
        re_run_adviser_id = attr.ib(type=Optional[str], default=None)
        source_type = attr.ib(type=Optional[str], default=None)
        kebechet_metadata = attr.ib(type=Optional[Dict[str, Any]], default=None)
        justification = attr.ib(type=Optional[List[Dict[str, Any]]], default=None)
        stack_info = attr.ib(type=Optional[List[Dict[str, Any]]], default=None)
        version = attr.ib(type=str, default="v3", init=False)

    def __init__(self,):
        """Initialize advise-justification topic."""
        super(AdviserTriggerMessage, self).__init__(
            base_name=self.base_name, value_type=self.MessageContents,
        )
