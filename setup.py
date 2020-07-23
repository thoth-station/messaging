"""Setup for messaging module."""

import os
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand  # noqa: N812
from pathlib import Path


def get_install_requires():
    """Get requirements from requirements.txt."""
    with open("requirements.txt", "r") as requirements_file:
        # TODO: respect hashes in requirements.txt file
        res = requirements_file.readlines()
        return [req.split(" ", maxsplit=1)[0] for req in res if req]


def get_test_requires():
    """Get requirements for running tests."""
    with open("requirements-test.txt", "r") as requirements_file:
        res = requirements_file.readlines()
        return [req.split(" ", maxsplit=1)[0] for req in res if req]


def get_version():
    """Get package version."""
    with open(os.path.join("thoth", "messaging", "__init__.py")) as f:
        content = f.readlines()

    for line in content:
        if line.startswith("__version__ ="):
            # dirty, remove trailing and leading chars
            return line.split(" = ")[1][1:-2]
    raise ValueError("No version identifier found")


class Test(TestCommand):
    """Introduce test command to run testsuite using pytest."""

    _IMPLICIT_PYTEST_ARGS = ["tests/", "--timeout=2", "--capture=no", "--verbose", "-l", "-s", "-vv"]

    user_options = [("pytest-args=", "a", "Arguments to pass into py.test")]

    def initialize_options(self):
        """Initialize test cli options."""
        super().initialize_options()
        self.pytest_args = None

    def finalize_options(self):
        """Finalize test cli options."""
        super().finalize_options()
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        """Run pytests."""
        import pytest

        passed_args = list(self._IMPLICIT_PYTEST_ARGS)

        if self.pytest_args:
            self.pytest_args = [arg for arg in self.pytest_args.split() if arg]
            passed_args.extend(self.pytest_args)

        sys.exit(pytest.main(passed_args))


VERSION = get_version()
setup(
    name="thoth-messaging",
    version=VERSION,
    description="Messaging module of Project Thoth",
    long_description=Path("README.rst").read_text(),
    author="Christoph Görn",
    author_email="goern@redhat.com",
    license="GPLv3+",
    packages=["thoth.messaging"],
    zip_safe=False,
    install_requires=get_install_requires(),
    tests_require=get_test_requires(),
    cmdclass={"test": Test},
    command_options={"build_sphinx": {"version": ("setup.py", VERSION), "release": ("setup.py", VERSION)}},
)
