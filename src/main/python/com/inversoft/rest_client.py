#
# Copyright (c) 2016, Inversoft Inc., All Rights Reserved
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

import requests

class RESTClient:
    """The RestClient used to build API calls to CleanSpeak.

    Attributes:
        _headers: The headers
        _method: The method
        _request: The request body
        _url: The url

    """

    def __init__(self):
        self._headers = {}
        self._method = None
        self._parameters = {}
        self._request = None
        self._request_file = None
        self._stream_response = False
        self._url = None

    def authorization(self, key):
        self._headers['Authorization'] = key
        return self

    def content_type(self, content_type):
        self._headers['Content-Type'] = content_type
        return self

    def delete(self):
        self._method = 'DELETE'
        return self

    def get(self):
        self._method = 'GET'
        return self

    def go(self):
        if self._method == 'DELETE':
            return ClientResponse(requests.delete(self._url, headers=self._headers, params=self._parameters))
        elif self._method == 'GET' and self._stream_response:
            return ClientResponse(requests.get(self._url, headers=self._headers, params=self._parameters, stream=True), True)
        elif self._method == 'GET':
            return ClientResponse(requests.get(self._url, headers=self._headers, params=self._parameters, stream=False))
        elif self._method == 'POST' and self._headers['Content-Type'] == 'application/json':
            return ClientResponse(requests.post(self._url, data=None, json=self._request, headers=self._headers, params=self._parameters))
        elif self._method == 'PUT' and self._headers['Content-Type'] == 'application/json':
            return ClientResponse(requests.put(self._url, data=None, json=self._request, headers=self._headers, params=self._parameters))
        elif self._method == 'POST' and self._request_file is not None:
            with open(self._request_file, 'rb') as f:
                return ClientResponse(requests.post(self._url, data=f, headers=self._headers, params=self._parameters))
        elif self._method == 'PUT' and self._request_file is not None:
            with open(self._request_file, 'rb') as f:
                return ClientResponse(requests.put(self._url, data=f, headers=self._headers, params=self._parameters))
        else:
            raise ValueError('The HTTP method must be set to POST, PUT, GET or DELETE prior to calling go()')

    def post(self):
        self._method = 'POST'
        return self

    def put(self):
        self._method = 'PUT'
        return self

    def request(self, request):
        self.content_type('application/json')
        self._request = request
        return self

    def request_from_file(self, file):
        self._request_file = file
        return self

    def stream_response(self):
        self._stream_response = True
        return self

    def uri(self, uri):
        if self._url is None:
            return self

        if self._url.endswith('/') and uri.startswith('/'):
            self._url += uri[:1]
        else:
            self._url += uri

        return self

    def url(self, url):
        self._url = url
        return self

    def url_parameter(self, name, value):
        if value is None:
            return self

        values = self._parameters.get(name)
        if values is None:
            values = []
            self._parameters[name] = values

        values.append(value)
        return self

    def url_segment(self, segment):
        if segment is not None:
            if not self._url.endswith('/'):
                self._url += '/'

            self._url += segment if type(segment) is str else str(segment)

        return self


class ClientResponse:
    """The ClientResponse returned from the the CleanSpeak API.

    Attributes:
        error_response:
        exception:
        response: The full response object
        success_response:
        status:
    """

    def __init__(self, response, streaming=False):
        self.error_response = None
        self.exception = None
        self.response = response
        self.success_response = None
        self.status = response.status_code

        if self.status < 200 or self.status > 299:
            if self.response.content is not None and self.status != 404:
                if self.status == 400:
                    self.error_response = self.response.json()
                else:
                    self.error_response = self.response
        elif not streaming:
            try:
                self.success_response = self.response.json()
            except ValueError:
                self.success_response = None

    def was_successful(self):
        return 200 <= self.status <= 299 and self.exception is None

    def write_response_to_file(self, file):
        with open(file, 'wb') as f:
            for chunk in self.response:
                f.write(chunk)