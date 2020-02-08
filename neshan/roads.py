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

import neshan
from neshan import convert


def snap_to_roads(client, path):
    """Snaps a path to the most likely roads travelled.

    Takes points collected along a route, and returns a similar
    set of data with the points snapped to the most likely roads the vehicle
    was traveling along.

    :param path: The path to be snapped.
    :type path: a single location, or a list of locations, where a
        location is a string, dict, list, or tuple

    :rtype: A list of snapped points.
    """

    params = {"path": convert.location_list(path)}

    return client._request("/v1/map-matching", params).get("snappedPoints", [])
