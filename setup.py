from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ts_002/__init__.py
from ts_002 import __version__ as version

setup(
	name="ts_002",
	version=version,
	description="TS 002",
	author="Kataba",
	author_email="aulia@kataba.id",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
