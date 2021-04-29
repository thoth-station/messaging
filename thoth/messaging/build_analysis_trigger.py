#!/usr/bin/env python3
# thoth-messaging
# Copyright(C) 2021 Fridolin Pokorny
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


"""This is Thoth Messaging module for BuildAnalysisTriggerMessage."""

import logging

from typing import Optional

from pydantic import StrictStr, StrictBool

from .message_base import MessageBase, BaseMessageContents

_LOGGER = logging.getLogger(__name__)

base_name = "thoth.build-analysis-trigger"


class MessageContents(BaseMessageContents):
    """Class used to represent contents of a message Kafka topic."""

    base_image: Optional[StrictStr]
    base_image_analysis_id: Optional[StrictStr]
    buildlog_document_id: Optional[StrictStr]
    buildlog_parser_id: Optional[StrictStr]
    environment_type: Optional[StrictStr]
    debug: StrictBool = False
    job_id: Optional[StrictStr]
    origin: Optional[StrictStr]
    output_image: Optional[StrictStr]
    output_image_analysis_id: Optional[StrictStr]
    base_registry_password: Optional[StrictStr]
    base_registry_user: Optional[StrictStr]
    base_registry_verify_tls: StrictBool = True
    output_registry_password: Optional[StrictStr]
    output_registry_user: Optional[StrictStr]
    output_registry_verify_tls: StrictBool = True

    version: StrictStr = "v1"


build_analysis_trigger_message = MessageBase(base_name=base_name, model=MessageContents)
