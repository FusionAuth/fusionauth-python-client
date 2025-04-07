#  Copyright (c) 2025, FusionAuth, All Rights Reserved
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
#  either express or implied. See the License for the specific
#  language governing permissions and limitations under the License.

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="fusionauth-client",
    version="1.57.0",
    author="FusionAuth",
    author_email="dev@fusionauth.io",
    description="A client library for FusionAuth",
    license="Apache-2.0",
    license_files=("LICENSE",),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FusionAuth/fusionauth-python-client",
    packages=find_packages(where="src/main/python"),
    namespace_packages=["fusionauth"],
    package_dir={"": "src/main/python"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
    ],
    install_requires=[
        "deprecated",
        "requests",
    ],
)
