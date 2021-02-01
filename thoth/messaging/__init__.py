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

from .advise_justification import advise_justification_message, AdviseJustificationContents
from .adviser_re_run import adviser_re_run_message, AdviserReRunContents
from .adviser_trigger import adviser_trigger_message, AdviserTriggerContents
from .build_analysis_trigger import build_analysis_trigger_message, BuildAnalysisTriggerContents
from .cve_provided import cve_provided_message, CVEProvidedContents
from .hash_mismatch import hash_mismatch_message, HashMismatchContents
from .inspection_complete import inspection_complete_message, InspectionCompleteContents
from .kebechet_run_url import kebechet_run_url_trigger_message, KebechetRunUrlTriggerContents
from .kebechet_trigger import kebechet_trigger_message, KebechetTriggerContents
from .missing_package import missing_package_message, MissingPackageContents
from .missing_version import missing_version_message, MissingVersionContents
from .package_extract_trigger import package_extract_trigger_message, PackageExtractTriggerContents
from .package_releases import package_released_message, PackageReleasedContents
from .provenance_checker_trigger import provenance_checker_trigger_message, ProvenanceCheckerTriggerContents
from .qebhwt_trigger import qebhwt_trigger_message, QebHwtTriggerContents
from .si_unanalyzed_package import si_unanalyzed_package_message, SIUnanalyzedPackageContents
from .solved_package import solved_package_message, SolvedPackageContents
from .unresolved_package import unresolved_package_message, UnresolvedPackageContents
from .unrevsolved_package import unrevsolved_package_message, UnrevsolvedPackageContents
from .update_provides_src_distro import update_provides_src_distro_message, UpdateProvidesSrcDistroContents

ALL_MESSAGES = [
    advise_justification_message,
    adviser_re_run_message,
    adviser_trigger_message,
    build_analysis_trigger_message,
    cve_provided_message,
    hash_mismatch_message,
    inspection_complete_message,
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
    update_provides_src_distro_message,
]


__all__ = [
    "advise_justification_message",
    "AdviseJustificationContents",
    "adviser_re_run_message",
    "AdviserReRunContents",
    "adviser_trigger_message",
    "AdviserTriggerContents",
    "build_analysis_trigger_message",
    "BuildAnalysisTriggerContents",
    "cve_provided_message",
    "CVEProvidedContents",
    "hash_mismatch_message",
    "HashMismatchContents",
    "inspection_complete_message",
    "InspectionCompleteContents",
    "kebechet_run_url_trigger_message",
    "KebechetRunUrlTriggerContents",
    "kebechet_trigger_message",
    "KebechetTriggerContents",
    "missing_package_message",
    "MissingPackageContents",
    "missing_version_message",
    "MissingVersionContents",
    "package_extract_trigger_message",
    "PackageExtractTriggerContents",
    "package_released_message",
    "PackageReleasedContents",
    "provenance_checker_trigger_message",
    "ProvenanceCheckerTriggerContents",
    "qebhwt_trigger_message",
    "QebHwtTriggerContents",
    "si_unanalyzed_package_message",
    "SIUnanalyzedPackageContents",
    "solved_package_message",
    "SolvedPackageContents",
    "unresolved_package_message",
    "UnresolvedPackageContents",
    "unrevsolved_package_message",
    "UnrevsolvedPackageContents",
    "update_provides_src_distro_message",
    "UpdateProvidesSrcDistroContents",
    "MessageBase",
    "BaseMessageContents",
    "message_factory",
]

__name__ = "thoth-messaging"
__version__ = "0.10.2"
