import json

from com.inversoft.passport_client import PassportClient


#  You must supply your API key and URL here
client = PassportClient('your-api-key', 'https://your-passport.inversoft.io')

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
    print json.dumps(client_response.success_response)
else:
    print json.dumps(client_response.error_response)
