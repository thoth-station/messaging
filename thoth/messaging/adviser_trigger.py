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
from typing import Any
from typing import Optional
from typing import Dict

from .message_base import MessageBase, BaseMessageContents

_LOGGER = logging.getLogger(__name__)


class AdviserTriggerMessage(MessageBase):
    """Class used for Advise events on Kafka topic."""

    base_name = "thoth.adviser-trigger"

    class MessageContents(BaseMessageContents):  # type: ignore
        """Class used to represent contents of a message Kafka topic."""

        application_stack: Dict[Any, Any]
        recommendation_type: str
        dev: bool = False
        debug: bool = False
        count: Optional[int] = None
        limit: Optional[int] = None
        runtime_environment: Optional[Dict[Any, Any]] = None
        library_usage: Optional[Dict[Any, Any]] = None
        origin: Optional[str] = None
        job_id: Optional[str] = None
        limit_latest_versions: Optional[int] = None
        github_event_type: Optional[str] = None
        github_check_run_id: Optional[int] = None
        github_installation_id: Optional[int] = None
        github_base_repo_url: Optional[str] = None
        re_run_adviser_id: Optional[str] = None
        source_type: Optional[str] = None
        version: str = "v1"

    def __init__(self,):
        """Initialize advise-justification topic."""
        super(AdviserTriggerMessage, self).__init__(
            base_name=self.base_name, value_type=self.MessageContents,
        )
