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
from .hash_mismatch import HashMismatchMessage
from .missing_package import MissingPackageMessage
from .missing_version import MissingVersionMessage
from .package_releases import PackageReleaseMessage
from .advise_justification import AdviseJustificationMessage
from .unresolved_package import UnresolvedPackageMessage
from .message_factory import message_factory

ALL_MESSAGES = [
    HashMismatchMessage,
    MissingVersionMessage,
    MissingPackageMessage,
    PackageReleaseMessage,
    UnresolvedPackageMessage,
]


__name__ = "thoth-messaging"
__version__ = "0.5.0"
