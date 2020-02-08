# This Python file uses the following encoding: utf-8
#
# Copyright 2016 Google Inc. All rights reserved.
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

"""Tests for the places module."""

import uuid

from types import GeneratorType

import responses

import neshan
import neshan.test as _test


class PlacesTest(_test.TestCase):

    def setUp(self):
        self.key = 'service.8AwKYt4Tov5II9uvbK5BkiZZ1TMHAM4JnBtm4yft'
        self.client = neshan.Client(self.key)
        self.location = (36.268706, 59.610011)

    @responses.activate
    def test_places_text_search(self):
        url = 'https://api.neshan.org/v1/search'
        responses.add(responses.GET, url,
                      body='{"items": []}',
                      status=200, content_type='application/json;charset=UTF-8')

        self.client.places('رستوران', location=self.location)

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual('%s?lat=36.268706&lng=59.610011&term=رستوران'
                            % (url), responses.calls[0].request.url)
