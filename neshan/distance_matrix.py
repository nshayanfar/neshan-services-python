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

"""Performs requests to the Google Maps Distance Matrix API."""

from neshan import convert


def distance_matrix(client, origins, destinations):
    """ Gets travel distance and time for a matrix of origins and destinations.

    :param origins: One or more locations and/or latitude/longitude values,
        from which to calculate distance and time. If you pass an address as
        a string, the service will geocode the string and convert it to a
        latitude/longitude coordinate to calculate directions.
    :type origins: a single location, or a list of locations, where a
        location is a string, dict, list, or tuple

    :param destinations: One or more addresses and/or lat/lng values, to
        which to calculate distance and time. If you pass an address as a
        string, the service will geocode the string and convert it to a
        latitude/longitude coordinate to calculate directions.
    :type destinations: a single location, or a list of locations, where a
        location is a string, dict, list, or tuple

    :rtype: matrix of distances. Results are returned in rows, each row
        containing one origin paired with each destination.
    """

    params = {
        "origins": convert.location_list(origins),
        "destinations": convert.location_list(destinations)
    }

    return client._request("/v1/distance-matrix", params)
