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


"""This is Thoth Messaging module for QebHwtTriggerMessage."""

import attr
import logging
from typing import Optional

from .message_base import MessageBase, BaseMessageContents

_LOGGER = logging.getLogger(__name__)


class QebHwtTriggerMessage(MessageBase):
    """Class used for QebHwt events on Kafka topic."""

    base_name = "thoth.qebhwt-trigger"

    @attr.s
    class MessageContents(BaseMessageContents):
        """Class used to represent contents of a message Kafka topic."""

        github_event_type = attr.ib(type=str)
        github_check_run_id = attr.ib(type=int)
        github_installation_id = attr.ib(type=int)
        github_base_repo_url = attr.ib(type=str)
        github_head_repo_url = attr.ib(type=str)
        origin = attr.ib(type=str)
        revision = attr.ib(type=str)
        host = attr.ib(type=str)
        job_id = attr.ib(type=Optional[str], default=None)
        version = attr.ib(type=str, default="v1", init=False)

    def __init__(self):
        """Initialize advise-justification topic."""
        super(QebHwtTriggerMessage, self).__init__(
            base_name=self.base_name, value_type=self.MessageContents,
        )
