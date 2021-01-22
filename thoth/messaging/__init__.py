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

from .advise_justification import AdviseJustificationMessage
from .adviser_re_run import AdviserReRunMessage
from .adviser_trigger import AdviserTriggerMessage
from .build_analysis_trigger import BuildAnalysisTriggerMessage
from .cve_provided import CVEProvidedMessage
from .hash_mismatch import HashMismatchMessage
from .inspection_complete import InspectionCompletedMessage
from .kebechet_run_url import KebechetRunUrlTriggerMessage
from .kebechet_trigger import KebechetTriggerMessage
from .missing_package import MissingPackageMessage
from .missing_version import MissingVersionMessage
from .package_extract_trigger import PackageExtractTriggerMessage
from .package_releases import PackageReleasedMessage
from .provenance_checker_trigger import ProvenanceCheckerTriggerMessage
from .qebhwt_trigger import QebHwtTriggerMessage
from .si_unanalyzed_package import SIUnanalyzedPackageMessage
from .solved_package import SolvedPackageMessage
from .unresolved_package import UnresolvedPackageMessage
from .unrevsolved_package import UnrevsolvedPackageMessage
from .update_provides_src_distro import UpdateProvidesSourceDistroMessage

ALL_MESSAGES = [
    AdviseJustificationMessage,
    AdviserReRunMessage,
    AdviserTriggerMessage,
    BuildAnalysisTriggerMessage,
    CVEProvidedMessage,
    HashMismatchMessage,
    InspectionCompletedMessage,
    KebechetRunUrlTriggerMessage,
    KebechetTriggerMessage,
    MissingVersionMessage,
    MissingPackageMessage,
    PackageExtractTriggerMessage,
    PackageReleasedMessage,
    ProvenanceCheckerTriggerMessage,
    QebHwtTriggerMessage,
    SIUnanalyzedPackageMessage,
    SolvedPackageMessage,
    UnresolvedPackageMessage,
    UnrevsolvedPackageMessage,
    UpdateProvidesSourceDistroMessage,
]

__all__ = [msg_cls.__name__ for msg_cls in ALL_MESSAGES] + ["MessageBase", "message_factory", "BaseMessageContents"]


__name__ = "thoth-messaging"
__version__ = "0.10.1"
