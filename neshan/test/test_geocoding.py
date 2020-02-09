# This Python file uses the following encoding: utf-8
#
# Copyright 2014 Google Inc. All rights reserved.
#
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
#

"""Tests for the geocoding module."""

import datetime

import responses

import neshan
import neshan.test as _test


class GeocodingTest(_test.TestCase):

    def setUp(self):
        self.key = 'service.8AwKYt4Tov5II9uvbK5BkiZZ1TMHAM4JnBtm4yft'
        self.client = neshan.Client(self.key)

    # @responses.activate
    # def test_simple_geocode(self):
    #     responses.add(responses.GET,
    #                   'https://api.neshan.org/v2/reverse',
    #                   body='{"status":"OK","results":[]}',
    #                   status=200,
    #                   content_type='application/json')

    #     results = self.client.geocode('Sydney')

    #     self.assertEqual(1, len(responses.calls))
    #     self.assertURLEqual('https://api.neshan.org/v2/reverse?'
    #                         'key=%s&address=Sydney' % self.key,
    #                         responses.calls[0].request.url)

    @responses.activate
    def test_reverse_geocode(self):
        responses.add(responses.GET,
                      'https://api.neshan.org/v2/reverse',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        results = self.client.reverse_geocode((-33.8674869, 151.2069902))

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual('https://api.neshan.org/v2/reverse?'
                            'lat=-33.8674869&lng=151.2069902',
                            responses.calls[0].request.url)

    @responses.activate
    def test_simple_reverse_geocode(self):
        responses.add(responses.GET,
                      'https://api.neshan.org/v2/reverse',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        results = self.client.reverse_geocode((40.714224, -73.961452))

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual('https://api.neshan.org/v2/reverse?'
                            'lat=40.714224&lng=-73.961452',
                            responses.calls[0].request.url)
