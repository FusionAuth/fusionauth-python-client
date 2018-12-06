import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fusionauth-client",
    version="1.3.0",
    author="Tyler Scott",
    author_email="tyler@inversoft.com",
    description="A client library for FusionAuth",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FusionAuth/fusionauth-python-client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries"
    ]
)