# FusionAuth Python Client ![semver 2.0.0 compliant](http://img.shields.io/badge/semver-2.0.0-brightgreen.svg?style=flat-square)

## Intro

<!--
tag::forDocSite[]
-->

If you're integrating FusionAuth with a Python 3 application, this library will speed up your development time. Please also make sure to check our [SDK Usage Suggestions page](https://fusionauth.io/docs/sdks/#usage-suggestions).

For additional information and documentation on FusionAuth refer to [https://fusionauth.io](https://fusionauth.io).

## Install
To install the FusionAuth Python Client package run:

```bash
pip install fusionauth-client
```

This library can be found on PyPI at https://pypi.org/project/fusionauth-client/.

## Examples

### Set Up

First, you have to make sure you have a running FusionAuth instance. If you don't have one already, the easiest way to install FusionAuth is [via Docker](https://fusionauth.io/docs/get-started/download-and-install/docker), but there are [other ways](https://fusionauth.io/docs/get-started/download-and-install). By default, it'll be running on `localhost:9011`.

Then, you have to [create an API Key](https://fusionauth.io/docs/apis/authentication#managing-api-keys) in the admin UI to allow calling API endpoints.

You are now ready to use this library.

### Create the Client

Include the package in your code by using the following statement.

```python
from fusionauth.fusionauth_client import FusionAuthClient
```

Now you're ready to begin making requests to FusionAuth. You will need to supply an API key you created in FusionAuth, the following example assumes an API key of `6b87a398-39f2-4692-927b-13188a81a9a3`.

```python
client = FusionAuthClient('6b87a398-39f2-4692-927b-13188a81a9a3', 'http://localhost:9011')
```

### Error Handling

After every request is made, you need to check for any errors and handle them. To avoid cluttering things up, we'll omit the error handling in the next examples, but you should do something like the following.


### Create an Application

To create an [Application](https://fusionauth.io/docs/get-started/core-concepts/applications), use the `create_application()` method.

```python
data = {
    'application': {
        'name': 'ChangeBank'
    }
}

result = client.create_application(data)

# Handle errors as shown in the beginning of the Examples section

# Otherwise parse the successful response
print(result.success_response)
```

[Check the API docs for this endpoint](https://fusionauth.io/docs/apis/applications#create-an-application)

### Adding Roles to an Existing Application

To add [roles to an Application](https://fusionauth.io/docs/get-started/core-concepts/applications#roles), use `create_application_role()`.  

```python
data = {
    'role': {
        'name': 'customer',
        'description': 'Default role for regular customers',
        'isDefault': 1
    }
}

result = client.create_application_role(
    application_id='5a89377e-a250-4b15-b766-377ecc9b9fc9',
    request=data
)

# Handle errors as shown in the beginning of the Examples section

# Otherwise parse the successful response
print(result.success_response)
```

[Check the API docs for this endpoint](https://fusionauth.io/docs/apis/applications#create-an-application-role)

### Retrieve Application Details

To fetch details about an [Application](https://fusionauth.io/docs/get-started/core-concepts/applications), use `retrieve_application()`. 

```python
result = client.retrieve_application(
    application_id='5a89377e-a250-4b15-b766-377ecc9b9fc9'
)
print(result.success_response)
```

[Check the API docs for this endpoint](https://fusionauth.io/docs/apis/applications#retrieve-an-application)

### Delete an Application

To delete an [Application](https://fusionauth.io/docs/get-started/core-concepts/applications), use `delete_application()`.

```python
client.delete_application(
    application_id='5a89377e-a250-4b15-b766-377ecc9b9fc9'
)
```

[Check the API docs for this endpoint](https://fusionauth.io/docs/apis/applications#delete-an-application)

### Lock a User

To [prevent a User from logging in](https://fusionauth.io/docs/get-started/core-concepts/users), use `deactivate_user()`. 

```python
client.deactivate_user(
    user_id='231b982c-9304-4642-9bac-492d6917f5aa'
)
```


[Check the API docs for this endpoint](https://fusionauth.io/docs/apis/users#delete-a-user)

### Registering a User

To [register a User in an Application](https://fusionauth.io/docs/get-started/core-concepts/users#registrations), use `register()`.

The code below also adds a `customer` role and a custom `appBackgroundColor` property to the User Registration.

```python
result = client.register(
    user_id='231b982c-9304-4642-9bac-492d6917f5aa',
    request={
        'registration': {
            'applicationId': '5a89377e-a250-4b15-b766-377ecc9b9fc9',
            'roles': [
                'customer'
            ],
            'data': {
                'appBackgroundColor': '#096324'
            }
        }
    }
)
print(result.success_response)
```

[Check the API docs for this endpoint](https://fusionauth.io/docs/apis/registrations#create-a-user-registration-for-an-existing-user)

<!--
end::forDocSite[]
-->



## Questions and support

If you find any bugs in this library, [please open an issue](https://github.com/FusionAuth/fusionauth-python-client/issues). Note that changes to the `FusionAuthClient` class have to be done on the [FusionAuth Client Builder repository](https://github.com/FusionAuth/fusionauth-client-builder/blob/master/src/main/client/python.client.ftl), which is responsible for generating that file.

But if you have a question or support issue, we'd love to hear from you.

If you have a paid plan with support included, please [open a ticket in your account portal](https://account.fusionauth.io/account/support/). Learn more about [paid plan here](https://fusionauth.io/pricing).

Otherwise, please [post your question in the community forum](https://fusionauth.io/community/forum/).

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/FusionAuth/fusionauth-python-client.

Note: if you want to change the `FusionAuthClient` class, you have to do it on the [FusionAuth Client Builder repository](https://github.com/FusionAuth/fusionauth-client-builder/blob/master/src/main/client/python.client.ftl), which is responsible for generating all client libraries we support.

## License

This code is available as open source under the terms of the [Apache v2.0 License](https://opensource.org/license/apache-2-0).

## Upgrade Policy

This library is built automatically to keep track of the FusionAuth API, and may also receive updates with bug fixes, security patches, tests, code samples, or documentation changes.

These releases may also update dependencies, language engines, and operating systems, as we\'ll follow the deprecation and sunsetting policies of the underlying technologies that it uses.

This means that after a dependency (e.g. language, framework, or operating system) is deprecated by its maintainer, this library will also be deprecated by us, and will eventually be updated to use a newer version.
