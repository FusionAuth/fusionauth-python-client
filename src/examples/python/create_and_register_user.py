import sys
from fusionauth.fusionauth_client import FusionAuthClient


# You must supply your API key and URL here
client = FusionAuthClient('api-key', 'http://localhost:9011')
# You must supply your Application Id here
application_id='application-id'

# Here we create a user and register them to our application in a single request
# This can alternatively be achieved in two steps, first creating the user, then registering them
user_registration_request = {
    'registration': {
        'applicationId': application_id,
        'roles': [
            'user',
            'community_helper'
        ]
    },
    'user': {
        'birthDate': '1976-05-30',
        'email': 'john@doe.io',
        'password': 'password',
        'firstName': 'John',
        'lastName': 'Doe',
        'twoFactorEnabled': False,
        'username': 'johnny123'
    },
    'sendSetPasswordEmail': False,
    'skipVerification': False
}

client_response = client.register(None, user_registration_request)
if client_response.was_successful():
    print(client_response.success_response)
else:
    sys.exit(client_response.error_response)
