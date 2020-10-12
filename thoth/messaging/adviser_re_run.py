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

from typing import Optional, Dict, Any

from .message_base import MessageBase, BaseMessageContents

_LOGGER = logging.getLogger(__name__)


class AdviserReRunMessage(MessageBase):
    """Class used for Adviser re run events on Kafka topic."""

    topic_name = "thoth.investigator.adviser-re-run"
    _message_version = 1  # update on schema change

    class MessageContents(BaseMessageContents, serializer="json"):  # type: ignore
        """Class used to represent contents of adviser re run message Kafka topic."""

        re_run_adviser_id: str

        application_stack: Dict[Any, Any]
        recommendation_type: str
        runtime_environment: Optional[Dict[Any, Any]] = None

        origin: Optional[str] = None
        github_event_type: Optional[str] = None
        github_check_run_id: Optional[int] = None
        github_installation_id: Optional[int] = None
        github_base_repo_url: Optional[str] = None

        source_type: Optional[str] = None

    def __init__(
        self,
        num_partitions: int = 1,
        replication_factor: int = 1,
        client_id: str = "thoth-messaging",
        bootstrap_server: str = "localhost:9092",
        topic_retention_time_second: int = 60 * 60 * 24 * 45,
        protocol: Optional[str] = None,
    ):
        """Initialize adviser-re-run topic."""
        super(AdviserReRunMessage, self).__init__(
            topic_name=self.topic_name,
            value_type=self.MessageContents,
            num_partitions=num_partitions,
            replication_factor=replication_factor,
            client_id=client_id,
            bootstrap_server=bootstrap_server,
            topic_retention_time_second=topic_retention_time_second,
            protocol=protocol,
            message_version=self._message_version,
        )
