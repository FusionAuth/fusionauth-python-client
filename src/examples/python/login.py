from fusionauth.fusionauth_client import FusionAuthClient

client = FusionAuthClient('APIKEY', 'http://localhost:9011')

application_id = '20ce6dac-b985-4c77-bb59-6369249f884b'

# Authenticate a user
response = client.login({
    'loginId': 'python@example.com',
    'password': 'password',
    'applicationId': application_id
})

if response.success_response:
  user = response.success_response['user']
  print(user['id'])
else:
  print(response.error_response)
