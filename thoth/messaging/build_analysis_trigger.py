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
import attr

from typing import Optional

from .message_base import MessageBase, BaseMessageContents

_LOGGER = logging.getLogger(__name__)


class BuildAnalysisTriggerMessage(MessageBase):
    """Class used for build analysis events on Kafka topic."""

    base_name = "thoth.build-analysis-trigger"

    @attr.s
    class MessageContents(BaseMessageContents):  # type: ignore
        """Class used to represent contents of a message Kafka topic."""

        base_image = attr.ib(type=Optional[str], default=None)
        base_image_analysis_id = attr.ib(type=Optional[str], default=None)
        buildlog_document_id = attr.ib(type=Optional[str], default=None)
        buildlog_parser_id = attr.ib(type=Optional[str], default=None)
        environment_type = attr.ib(type=Optional[str], default=None)
        debug = attr.ib(type=bool, default=False)
        job_id = attr.ib(type=Optional[str], default=None)
        origin = attr.ib(type=Optional[str], default=None)
        output_image = attr.ib(type=Optional[str], default=None)
        output_image_analysis_id = attr.ib(type=Optional[str], default=None)
        base_registry_password = attr.ib(type=Optional[str], default=None)
        base_registry_user = attr.ib(type=Optional[str], default=None)
        base_registry_verify_tls = attr.ib(type=bool, default=True)
        output_registry_password = attr.ib(type=Optional[str], default=None)
        output_registry_user = attr.ib(type=Optional[str], default=None)
        output_registry_verify_tls = attr.ib(type=bool, default=True)
        version = attr.ib(type=str, default="v1", init=False)

    def __init__(self,):
        """Initialize build analysis topic."""
        super(BuildAnalysisTriggerMessage, self).__init__(
            base_name=self.base_name, value_type=self.MessageContents,
        )
