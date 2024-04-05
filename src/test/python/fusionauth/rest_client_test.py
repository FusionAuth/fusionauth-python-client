#
# Copyright (c) 2016-2024, FusionAuth, All Rights Reserved
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
import os
import uuid

import unittest

from fusionauth.rest_client import RESTClient


def print_json(parsed_json):
    print(json.dumps(parsed_json, indent=2, sort_keys=True))


class RestClientTest(unittest.TestCase):
    def setUp(self):
        pass

    def runTest(self):
        pass

    def test_uri_with_path_with_slash_prefix(self):
        client = RESTClient()
        client.url('http://example.com')
        self.assertEqual(client.uri('/example/path')._url, 'http://example.com/example/path')

    def test_uri_with_path_with_no_slash_prefix(self):
        client = RESTClient()
        client.url('http://example.com')
        self.assertEqual(client.uri('example/path')._url, 'http://example.com/example/path')

    def test_uri_with_slash_suffix_with_path_with_slash_prefix(self):
        client = RESTClient()
        client.url('http://example.com/')
        self.assertEqual(client.uri('/example/path')._url, 'http://example.com/example/path')

    def test_uri_with_slash_suffix_with_path_with_no_slash_prefix(self):
        client = RESTClient()
        client.url('http://example.com/')
        self.assertEqual(client.uri('example/path')._url, 'http://example.com/example/path')


if __name__ == '__main__':
    unittest.main()
