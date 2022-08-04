#! /usr/bin/env python3

"""Installation script for this package."""

import os

from setuptools import setup

setup(
    name="drytils",
    version="0.1.1",
    description=(
        "Don't-Repeat-Yourself collection of utility functions using only the"
        "Python standard library as dependency."
    ),
    long_description=open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")
    ).read(),
    long_description_content_type="text/markdown",
    author="Dennis Hedback",
    packages=["drytils"],
    install_requires=[],
)
