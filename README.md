## FusionAuth Python Client ![semver 2.0.0 compliant](http://img.shields.io/badge/semver-2.0.0-brightgreen.svg?style=flat-square)
If you're integrating FusionAuth with a Python 3 application, this library will speed up your development time.

For additional information and documentation on FusionAuth refer to [https://fusionauth.io](https://fusionauth.io).

### Install
To install the FusionAuth Python Client package run:

```bash
pip install fusionauth-client
```

This library can be found on PyPI
* https://pypi.org/project/fusionauth-client/

### Coding
And then include the package in your code by using the following statement.

```python
from fusionauth.fusionauth_client import FusionAuthClient
```

Now you're ready to begin making requests to FusionAuth. You will need to supply an API key you created in FusionAuth, the folowing example assumes an API key of `6b87a398-39f2-4692-927b-13188a81a9a3`.

```python
client = FusionAuthClient('6b87a398-39f2-4692-927b-13188a81a9a3', 'http://localhost:9011')
```

Each method in the client library includes documentation to describe the use and parameters. In addition to this resource, review the API documentation. https://fusionauth.io/docs/v1/tech/apis/

If you encounter issues with this library, please open an issue.
