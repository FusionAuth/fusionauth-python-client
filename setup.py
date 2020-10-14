from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="fusionauth-client",
    version="1.21.0",
    author="Tyler Scott",
    author_email="tyler@inversoft.com",
    description="A client library for FusionAuth",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FusionAuth/fusionauth-python-client",
    packages=find_packages(where='src/main/python'),
    namespace_packages=["fusionauth"],
    package_dir={'': 'src/main/python'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
    ],
    install_requires=[
        'deprecated', 'requests',
    ]
)
