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

"""Tests for the distance matrix module."""

from datetime import datetime
import time

import responses

import neshan
import neshan.test as _test


class DistanceMatrixTest(_test.TestCase):

    def setUp(self):
        self.key = 'service.8AwKYt4Tov5II9uvbK5BkiZZ1TMHAM4JnBtm4yft'
        self.client = neshan.Client(self.key)

    @responses.activate
    def test_basic_params(self):
        responses.add(responses.GET,
                      'https://api.neshan.org/v1/distance-matrix',
                      body='{"status":"OK","rows":[]}',
                      status=200,
                      content_type='application/json')

        origins = ['36.316551,59.585658', '35.691080,51.299734']
        destinations = ['32.633881,51.681525','31.876915,54.344318']

        matrix = self.client.distance_matrix(origins, destinations)

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual('https://api.neshan.org/v1/distance-matrix?'
                            'origins=36.316551,59.585658|35.691080,51.299734&'
                            'destinations=32.633881,51.681525|31.876915,54.344318',
                            responses.calls[0].request.url)
