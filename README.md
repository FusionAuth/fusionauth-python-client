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

Here's an example which logs a user in:

```python
from fusionauth.fusionauth_client import FusionAuthClient
client = FusionAuthClient(API_KEY, 'http://localhost:9011')

data = {
    'loginId': loginId,
    'password': password,
    'applicationId': My_App_ID
}

print(client.login(data).success_response)
```

Each method in the client library includes documentation to describe the use and parameters. In addition to this resource, review the API documentation. https://fusionauth.io/docs/v1/tech/apis/

If you encounter a bug with this library, please open an issue.

## Questions and support

If you have a question or support issue regarding this client library, we'd love to hear from you.

If you have a paid edition with support included, please [open a ticket in your account portal](https://account.fusionauth.io/account/support/). Learn more about [paid editions here](https://fusionauth.io/pricing).

Otherwise, please [post your question in the community forum](https://fusionauth.io/community/forum/).

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/FusionAuth/fusionauth-python-client.

## License

This code is available as open source under the terms of the [Apache v2.0 License](https://opensource.org/licenses/Apache-2.0).
