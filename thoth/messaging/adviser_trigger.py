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

from pydantic import StrictStr, StrictInt, StrictBool

from .message_base import MessageBase, BaseMessageContents

_LOGGER = logging.getLogger(__name__)


base_name = "thoth.adviser-trigger"


class MessageContents(BaseMessageContents):  # type: ignore
    """Class used to represent contents of a message Kafka topic."""

    recommendation_type: StrictStr
    dev: StrictBool = False
    debug: StrictBool = False
    authenticated: StrictBool = False
    count: Optional[StrictInt]
    limit: Optional[StrictInt]
    origin: Optional[StrictStr]
    job_id: Optional[StrictStr]
    limit_latest_versions: Optional[StrictInt]
    re_run_adviser_id: Optional[StrictStr]
    source_type: Optional[StrictStr]
    kebechet_metadata: Optional[Dict[StrictStr, Any]]
    justification: Optional[List[Dict[StrictStr, Any]]]
    stack_info: Optional[List[Dict[StrictStr, Any]]]

    version: StrictStr = "v5"

    class Config:
        """Config for pydantic."""

        arbitrary_types_allowed = True  # allows for typing.Any


adviser_trigger_message = MessageBase(base_name=base_name, model=MessageContents)
