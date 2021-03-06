# -*- coding: utf-8 -*-
"""setuptools control."""

import re

from setuptools import setup


def get_version():
    """Return __version__ value from main source file."""
    with open("epoc_harvester_simulator/__init__.py") as source:
        version = re.search(r"^__version__\s*=\s*'(.*)'",
                            source.read(),
                            re.M).group(1)
    return version


def get_description():
    """Return long description from README."""
    with open("README.md", "rb") as readme:
        long_description = readme.read().decode("utf-8")
    return long_description


setup(
    name="epoc_harvester_simulator",
    packages=["epoc_harvester_simulator"],
    package_data={'epoc_harvester_simulator': ['data/*.json']},
    test_suite="tests",
    entry_points={
        "console_scripts": [
            "epoc_harvester_simulator = epoc_harvester_simulator.__main__:main"
        ]
    },
    version=get_version(),
    description="Application that simmulates data send from native epoc_harvester application.",
    long_description=get_description(),
    author="Egor Artemov",
    author_email="egor.artemov@gmail.com",
    url="https://gitlab.com/souryogurt/epoc_harvester_simulator",
    install_requires=["future", "websockets"],
    setup_requires=[]
)
