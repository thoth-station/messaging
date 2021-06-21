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


"""This is Thoth Messaging module for ProvenanceCheckerTriggerMessage."""

import logging
from typing import Optional, List, Dict, Any

from pydantic import StrictBool, StrictStr

from .message_base import MessageBase, BaseMessageContents

_LOGGER = logging.getLogger(__name__)


base_name = "thoth.provenance-checker-trigger"


class MessageContents(BaseMessageContents):
    """Class used to represent contents of a message Kafka topic."""

    debug: StrictBool = False
    authenticated: StrictBool = False
    origin: Optional[StrictStr]
    whitelisted_sources: Optional[List[StrictStr]]
    job_id: Optional[StrictStr]
    kebechet_metadata: Optional[Dict[StrictStr, Any]]
    justification: Optional[List[Dict[StrictStr, Any]]]
    stack_info: Optional[List[Dict[StrictStr, Any]]]

    version: StrictStr = "v4"

    class Config:
        """Config for pydantic."""

        arbitrary_types_allowed = True  # allow for typing.Any


provenance_checker_trigger_message = MessageBase(base_name=base_name, model=MessageContents)
