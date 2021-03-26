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

from .message_base import MessageBase
from .message_base import BaseMessageContents
from .message_factory import message_factory

from .advise_justification import advise_justification_message
from .adviser_re_run import adviser_rerun_message
from .adviser_trigger import adviser_trigger_message
from .build_analysis_trigger import build_analysis_trigger_message
from .cve_provided import cve_provided_message
from .hash_mismatch import hash_mismatch_message
from .inspection_complete import inspection_completed_message
from .kebechet_run_url import kebechet_run_url_trigger_message
from .kebechet_trigger import kebechet_trigger_message
from .missing_package import missing_package_message
from .missing_version import missing_version_message
from .package_extract_trigger import package_extract_trigger_message
from .package_releases import package_released_message
from .provenance_checker_trigger import provenance_checker_trigger_message
from .qebhwt_trigger import qebhwt_trigger_message
from .si_unanalyzed_package import si_unanalyzed_package_message
from .solved_package import solved_package_message
from .unresolved_package import unresolved_package_message
from .unrevsolved_package import unrevsolved_package_message
from .update_provides_src_distro import update_provides_source_distro_message

ALL_MESSAGES = [
    advise_justification_message,
    adviser_rerun_message,
    adviser_trigger_message,
    build_analysis_trigger_message,
    cve_provided_message,
    hash_mismatch_message,
    inspection_completed_message,
    kebechet_run_url_trigger_message,
    kebechet_trigger_message,
    missing_package_message,
    missing_version_message,
    package_extract_trigger_message,
    package_released_message,
    provenance_checker_trigger_message,
    qebhwt_trigger_message,
    si_unanalyzed_package_message,
    solved_package_message,
    unresolved_package_message,
    unrevsolved_package_message,
    update_provides_source_distro_message,
]

__all__ = [
    "advise_justification_message",
    "adviser_rerun_message",
    "adviser_trigger_message",
    "build_analysis_trigger_message",
    "cve_provided_message",
    "hash_mismatch_message",
    "inspection_completed_message",
    "kebechet_run_url_trigger_message",
    "kebechet_trigger_message",
    "missing_package_message",
    "missing_version_message",
    "package_extract_trigger_message",
    "package_released_message",
    "provenance_checker_trigger_message",
    "qebhwt_trigger_message",
    "si_unanalyzed_package_message",
    "solved_package_message",
    "unresolved_package_message",
    "unrevsolved_package_message",
    "update_provides_source_distro_message",
    "MessageBase",
    "message_factory",
    "BaseMessageContents",
]


__name__ = "thoth-messaging"
__version__ = "0.12.0"
