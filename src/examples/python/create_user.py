from fusionauth.fusionauth_client import FusionAuthClient


#  You must supply your API key and URL here
client = FusionAuthClient('api-key', 'http://localhost:9011')

user_request = {
    'sendSetPasswordEmail': False,
    'skipVerification': True,
    'user': {
        'email': 'art@vandaleyindustries.com',
        'password': 'password'
    }
}

client_response = client.create_user(None, user_request)

if client_response.was_successful():
    print(client_response.success_response)
else:
    print(client_response.error_response)
