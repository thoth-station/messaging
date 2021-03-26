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
from typing import Optional, Dict, List, Any

from .message_base import MessageBase, BaseMessageContents

_LOGGER = logging.getLogger(__name__)


base_name = "thoth.adviser-trigger"


class MessageContents(BaseMessageContents):  # type: ignore
    """Class used to represent contents of a message Kafka topic."""

    recommendation_type: str
    dev: bool = False
    debug: bool = False
    count: Optional[int]
    limit: Optional[int]
    origin: Optional[str]
    job_id: Optional[str]
    limit_latest_versions: Optional[int]
    github_event_type: Optional[str]
    github_check_run_id: Optional[int]
    github_installation_id: Optional[int]
    github_base_repo_url: Optional[str]
    re_run_adviser_id: Optional[str]
    source_type: Optional[str]
    kebechet_metadata: Optional[Dict[str, Any]]
    justification: Optional[List[Dict[str, Any]]]
    stack_info = Optional[List[Dict[str, Any]]]

    version: str = "v3"


adviser_trigger_message = MessageBase(base_name=base_name, model=MessageContents)
