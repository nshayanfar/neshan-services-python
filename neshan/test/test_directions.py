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

"""Tests for the directions module."""

from datetime import datetime
from datetime import timedelta
import time

import responses

import neshan
import neshan.test as _test


class DirectionsTest(_test.TestCase):

    def setUp(self):
        self.key = 'service.8AwKYt4Tov5II9uvbK5BkiZZ1TMHAM4JnBtm4yft'
        self.client = neshan.Client(self.key)

    @responses.activate
    def test_simple_directions(self):
        responses.add(responses.GET,
                      'https://api.neshan.org/v2/direction',
                      body='{"routes":[]}',
                      status=200,
                      content_type='application/json;charset=UTF-8')

        # Simplest directions request. Driving directions by default.
        routes = self.client.directions(
            (36.268706, 59.610011), (36.287607, 59.599527))

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual('https://api.neshan.org/v2/direction'
                            '?origin=36.268706,59.610011&destination=36.287607,59.599527',
                            responses.calls[0].request.url)

    @responses.activate
    def test_zero_results_returns_response(self):
        responses.add(responses.GET,
                      'https://api.neshan.org/v2/direction',
                      body='{"status":"ZERO_RESULTS","routes":[]}',
                      status=200,
                      content_type='application/json;charset=UTF-8')

        routes = self.client.directions("Toledo", "Madrid")
        self.assertIsNotNone(routes)
        self.assertEqual(0, len(routes))

    @responses.activate
    def test_alternatives(self):
        responses.add(responses.GET,
                      'https://api.neshan.org/v2/direction',
                      body='{"status":"OK","routes":[]}',
                      status=200,
                      content_type='application/json;charset=UTF-8')

        routes = self.client.directions((36.268706, 59.610011),
                                        (36.287607, 59.599527),
                                        alternatives=True)

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual('https://api.neshan.org/v2/direction?'
                            'origin=36.268706,59.610011&destination=36.287607,59.599527&'
                            'alternative=true',
                            responses.calls[0].request.url)
