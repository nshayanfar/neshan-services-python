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

"""Tests for the maps module."""

from types import GeneratorType

import responses

import neshan
import neshan.test as _test


class MapsTest(_test.TestCase):

    def setUp(self):
        self.key = 'service.8AwKYt4Tov5II9uvbK5BkiZZ1TMHAM4JnBtm4yft'
        self.client = neshan.Client(self.key)

    @responses.activate
    def test_download(self):
        url = 'https://api.neshan.org/v2/static'
        responses.add(responses.GET, url, status=200)

        response = self.client.static_map(
            width=400, height=400, zoom=6,
            center=(63.259591, -144.667969)
        )

        self.assertTrue(isinstance(response, GeneratorType))
        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual(
            '%s?center=63.259591%%2C-144.667969&height=400&marker=none&type=neshan&width=400&zoom=6'
            % (url), responses.calls[0].request.url)

        with self.assertRaises(ValueError):
            self.client.static_map(width=400, height=400, center=(63.259591, -144.667969),
                                   zoom=6, marker='test')

        with self.assertRaises(ValueError):
            self.client.static_map(width=400, height=400, center=(63.259591, -144.667969),
                                   zoom=6, mapType='test')
