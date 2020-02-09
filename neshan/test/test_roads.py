#
# Copyright 2015 Google Inc. All rights reserved.
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

"""Tests for the roads module."""


import responses

import neshan
import neshan.test as _test


class RoadsTest(_test.TestCase):

    def setUp(self):
        self.key = "service.8AwKYt4Tov5II9uvbK5BkiZZ1TMHAM4JnBtm4yft"
        self.client = neshan.Client(self.key)

    @responses.activate
    def test_snap(self):
        responses.add(responses.GET,
                      "https://api.neshan.org/v1/map-matching",
                      body='{"snappedPoints":["foo"]}',
                      status=200,
                      content_type="application/json")

        results = self.client.snap_to_roads((40.714728, -73.998672))
        self.assertEqual("foo", results[0])

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual("https://api.neshan.org/v1/map-matching?"
                            "path=40.714728%2C-73.998672",
                            responses.calls[0].request.url)

    # @responses.activate
    # def test_retry(self):
    #     class request_callback:
    #         def __init__(self):
    #             self.first_req = True

    #         def __call__(self, req):
    #             if self.first_req:
    #                 self.first_req = False
    #                 return (500, {}, 'Internal Server Error.')
    #             return (200, {}, '{"speedLimits":[]}')

    #     responses.add_callback(responses.GET,
    #             "https://roads.googleapis.com/v1/speedLimits",
    #             content_type="application/json",
    #             callback=request_callback())

    #     self.client.speed_limits([])

    #     self.assertEqual(2, len(responses.calls))
    #     self.assertEqual(responses.calls[0].request.url, responses.calls[1].request.url)
