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

"""Performs requests to the Google Maps Directions API."""

from neshan import convert


def directions(client, origin, destination,
               waypoints=None, avoidTrafficZone=False, avoidOddEvenZone=False,
               alternatives=False):
    """Get directions between an origin point and a destination point.

    :param origin: The address or latitude/longitude value from which you wish
        to calculate directions.
    :type origin: string, dict, list, or tuple

    :param destination: The address or latitude/longitude value from which
        you wish to calculate directions.
    :type destination: string, dict, list, or tuple

    :param waypoints: Specifies an array of waypoints. Waypoints alter a
        route by routing it through the specified location(s).
    :type waypoints: a single location, or a list of locations, where a
        location is a string, dict, list, or tuple

    :param alternatives: If True, more than one route may be returned in the
        response.
    :type alternatives: bool

    :rtype: list of routes
    """

    params = {
        "origin": convert.latlng(origin),
        "destination": convert.latlng(destination)
    }

    if waypoints:
        waypoints = convert.location_list(waypoints)
        params["waypoints"] = waypoints

    if avoidTrafficZone:
        params['avoidTrafficZone'] = 'true'

    if avoidOddEvenZone:
        params['avoidOddEvenZone'] = 'true'

    if alternatives:
        params["alternative"] = "true"

    return client._request("/v2/direction", params).get("routes", [])
