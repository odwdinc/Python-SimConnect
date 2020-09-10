#!/usr/bin/env python
from setuptools import setup
import distutils.sysconfig

with open("requirements.txt") as f:
	install_requires = f.read()[1:].splitlines()[1:]

with open("requirements_dev.txt") as f:
	tests_require = f.read().splitlines()[1:]

setup(
	install_requires=install_requires,
	tests_require=tests_require,
	package_data={"": ["*.dll"]}
)