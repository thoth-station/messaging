#!/usr/bin/env python3
# thoth-messaging
# Copyright(C) 2019, 2020 Red Hat, Inc.
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

"""This is Thoth Messaging module."""

from .base import MessageBase, BaseMessageContents
from .message_factory import message_factory

import advise_justification
import adviser_re_run
import adviser_trigger
import build_analysis_trigger
import cve_provided
import hash_mismatch
import inspection_complete
import kebechet_run_url
import kebechet_trigger
import missing_package
import missing_version
import package_extract_trigger
import package_releases
import provenance_checker_trigger
import qebhwt_trigger
import si_unanalyzed_package
import solved_package
import unresolved_package
import unrevsolved_package
import update_provides_src_distro

ALL_MESSAGES = [
    advise_justification.message,
    adviser_re_run.message,
    adviser_trigger.message,
    build_analysis_trigger.message,
    cve_provided.message,
    hash_mismatch.message,
    inspection_complete.message,
    kebechet_run_url.message,
    kebechet_trigger.message,
    missing_package.message,
    missing_version.message,
    package_extract_trigger.message,
    package_releases.message,
    provenance_checker_trigger.message,
    qebhwt_trigger.message,
    si_unanalyzed_package.message,
    solved_package.message,
    unresolved_package.message,
    unrevsolved_package.message,
    update_provides_src_distro.message,
]


__all__ = [
    "MessageBase",
    "BaseMessageContents",
    "message_factory",
]

__name__ = "thoth-messaging"
__version__ = "0.10.3"
