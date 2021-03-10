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

from .message_base import MessageBase, BaseMessageContents

_LOGGER = logging.getLogger(__name__)

base_name = "thoth.build-analysis-trigger"


class MessageContents(BaseMessageContents):
    """Class used to represent contents of a message Kafka topic."""

    base_image: Optional[str]
    base_image_analysis_id: Optional[str]
    buildlog_document_id: Optional[str]
    buildlog_parser_id: Optional[str]
    environment_type: Optional[str]
    debug: bool = False
    job_id: Optional[str]
    origin: Optional[str]
    output_image: Optional[str]
    output_image_analysis_id: Optional[str]
    base_registry_password: Optional[str]
    base_registry_user: Optional[str]
    base_registry_verify_tls: bool = True
    output_registry_password: Optional[str]
    output_registry_user: Optional[str]
    output_registry_verify_tls: bool = True

    version: str = "v1"


build_analysis_trigger_message = MessageBase(base_name=base_name, model=MessageContents)
