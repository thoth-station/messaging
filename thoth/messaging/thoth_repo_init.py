#!/usr/bin/env python3
# thoth-messaging
# Copyright(C) 2021 Kevin Postlethwait
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


"""This is Thoth Messaging module for repo init messages."""

from .message_base import MessageBase, BaseMessageContents
from typing import Optional

from pydantic import StrictStr

base_name = "thoth.repo-init"


class MessageContents(BaseMessageContents):
    """Class used to represent a trigger for thoth repo initialization."""

    project_url: StrictStr
    job_id: Optional[StrictStr]
    version: StrictStr = "v1"


thoth_repo_init_message = MessageBase(base_name=base_name, model=MessageContents)
