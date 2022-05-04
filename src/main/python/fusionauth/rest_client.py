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

import base64
import json

import requests


class RESTClient:
    """The RestClient used to build API calls to FusionAuth.

    Attributes:
        _headers: The headers
        _parameters: The parameters
        _url: The url
        _body_handler: A delegate to get the body of the request
        _certificate: The certificate
        _method: The method
    """

    def __init__(self):
        self._url = None
        self._parameters = {}
        self._proxy = {}
        self._headers = {}
        self._body_handler = None
        self._certificate = None
        self._connect_timeout = 1000
        self._error_response_handler = None
        self._error_type = None
        self._method = None
        self._success_response_handler = None

    def authorization(self, authorization):
        self._headers['Authorization'] = authorization
        return self

    def basic_authorization(self, username, password):
        if username and password:
            self.header('Authorization', 'Basic ' + base64.urlsafe_b64encode(username + ':' + password))
        return self

    def body_handler(self, handler):
        self._body_handler = handler
        return self

    def certificate(self, certificate):
        self._certificate = certificate
        return self

    def connect_timeout(self, connect_timeout):
        self._connect_timeout = connect_timeout
        return self

    def delete(self):
        self._method = 'DELETE'
        return self

    def error_response_handler(self, error_response_handler):
        self._error_response_handler = error_response_handler
        return self

    def get(self):
        self._method = 'GET'
        return self

    def patch(self):
        self._method = 'PATCH'
        return self

    def post(self):
        self._method = 'POST'
        return self

    def put(self):
        self._method = 'PUT'
        return self

    def go(self):
        if self._method is None:
            raise ValueError('The HTTP method must be set prior to calling go()')

        if self._url is None or len(self._url) == 0:
            raise ValueError('You must specify a URL')

        if self._body_handler is not None:
            self._body_handler.set_headers(self._headers)

        data = self._body_handler.get_body() if self._body_handler is not None else None

        return ClientResponse(
            requests.request(self._method, self._url, headers=self._headers, params=self._parameters, data=data, cert=self._certificate,
                             timeout=self._connect_timeout, proxies=self._proxy))

    def header(self, key, value):
        self._headers[key] = value
        return self

    def headers(self, headers):
        self._headers.update(headers)
        return self

    def success_response_handler(self, success_response_handler):
        self._success_response_handler = success_response_handler
        return self

    def uri(self, uri):
        if self._url is None:
            return self

        if self._url.endswith('/') and uri.startswith('/'):
            self._url += uri[1:]
        elif not self._url.endswith('/') and not uri.startswith('/'):
            self._url += "/" + uri
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
    """The ClientResponse returned from the the FusionAuth API.

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


class JSONBodyHandler:
    def __init__(self, body_object):
        self._body = json.dumps(body_object)

    def set_headers(self, headers):
        headers['Length'] = str(len(self._body.encode('utf-8')))
        headers['Content-Type'] = "application/json"

    def get_body(self):
        return self._body

class FormDataBodyHandler:
    def __init__(self, body_object):
        self._body = body_object

    def set_headers(self, headers):
        headers['Content-Type'] = "application/x-www-form-urlencoded"

    def get_body(self):
        return self._body
