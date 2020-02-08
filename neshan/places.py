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

"""Performs requests to the Neshan API."""
import warnings

from neshan import convert


def places(
    client,
    term,
    location=None,
):
    """
    Places search.

    :param term: The text string on which to search, for example: "restaurant".
    :type term: string

    :param location: The latitude/longitude value for which you wish to obtain the
        closest, human-readable address.
    :type location: dict, list, or tuple

    :rtype: result dict with the following keys:
        count: number of returned results
        items: array of places
    """
    params = {}
    if location:
        latlng = convert.normalize_lat_lng(location)
        params['lat'] = latlng[0]
        params['lng'] = latlng[1]
    if term:
        params['term'] = term

    url = '/v1/search'
    return client._request(url, params)
