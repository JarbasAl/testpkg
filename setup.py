#!/usr/bin/env python3
from os.path import join, dirname

from setuptools import setup


def get_version():
    """ Find the version of this skill"""
    version_file = join(dirname(__file__), 'version.py')
    major, minor, build, alpha = (None, None, None, None)
    with open(version_file) as f:
        for line in f:
            if 'VERSION_MAJOR' in line:
                major = line.split('=')[1].strip()
            elif 'VERSION_MINOR' in line:
                minor = line.split('=')[1].strip()
            elif 'VERSION_BUILD' in line:
                build = line.split('=')[1].strip()
            elif 'VERSION_ALPHA' in line:
                alpha = line.split('=')[1].strip()

            if ((major and minor and build and alpha) or
                    '# END_VERSION_BLOCK' in line):
                break
    version = f"{major}.{minor}.{build}"
    if int(alpha):
        version += f"a{alpha}"
    return version


SKILL_PKG = "test_pkg"

setup(
    name=SKILL_PKG,
    version=get_version(),
    package_dir={SKILL_PKG: ""},
    packages=[SKILL_PKG],
    include_package_data=True
)
