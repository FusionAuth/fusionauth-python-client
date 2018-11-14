#
# Copyright (c) 2016-2018, FusionAuth, All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#

import json
import uuid

import unittest2

from fusionauth.fusionauth_client import FusionAuthClient


def print_json(parsed_json):
    print(json.dumps(parsed_json, indent=2, sort_keys=True))


class FusionAuthClientTest(unittest2.TestCase):
    def setUp(self):
        self.client = FusionAuthClient('bf69486b-4733-4470-a592-f1bfce7af580', 'http://localhost:9011')

    def runTest(self):
        pass

    def test_retrieve_applications(self):
        client_response = self.client.retrieve_applications()
        self.assertEqual(client_response.status, 200)
        self.assertEqual(len(client_response.success_response['applications']), 1)

    def test_create_user_retrieve_user(self):
        # Check if the user already exists.
        get_user_response = self.client.retrieve_user_by_email('art@vandaleyindustries.com')
        if get_user_response.status is 200:
            delete_user_response = self.client.delete_user(get_user_response.success_response['user']['id'])
            self.assertEqual(delete_user_response.status, 200, delete_user_response.error_response)
        else:
            self.assertEqual(get_user_response.status, 404, get_user_response.error_response)

        # Create a new registration for this user.
        user_request = {
            'sendSetPasswordEmail': False,
            'skipVerification': True,
            'user': {
                'email': 'art@vandaleyindustries.com',
                'password': 'password'
            }
        }
        create_user_response = self.client.create_user(None, user_request)
        self.assertEqual(create_user_response.status, 200, create_user_response.error_response)

        # Retrieve the user
        user_id = create_user_response.success_response['user']['id']
        get_user_response = self.client.retrieve_user(user_id)
        self.assertEqual(get_user_response.status, 200)
        self.assertIsNotNone(get_user_response.success_response)
        self.assertIsNone(get_user_response.error_response)
        self.assertEquals(get_user_response.success_response['user']['email'], 'art@vandaleyindustries.com')
        self.assertFalse('password' in get_user_response.success_response['user'])
        self.assertFalse('salt' in get_user_response.success_response['user'])

    def test_retrieve_user_missing(self):
        user_id = uuid.uuid4()
        client_response = self.client.retrieve_user(user_id)
        self.assertEqual(client_response.status, 404)
        self.assertIsNone(client_response.success_response)
        self.assertIsNone(client_response.error_response)


if __name__ == '__main__':
    unittest2.main()
