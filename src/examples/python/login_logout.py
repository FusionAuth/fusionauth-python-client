import os
import json
from fusionauth.fusionauth_client import FusionAuthClient

api_key = "..."
app_id = "..."
host_ip = "localhost"

client = FusionAuthClient(api_key, "http://{}:9011".format(host_ip))

login_request = {
    'applicationId': app_id,
    'loginId': 'user@fusionauth.io',
    'password': 'password'
}

client_response = client.login(login_request)
if client_response.was_successful():
  print(client_response.success_response)
else:
  print(client_response.error_response)


client_response = client.logout("true", None)
if client_response.was_successful():
  print(client_response.success_response)
else:
  print(client_response.error_response)
