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

"""Performs requests to the Neshan Geocoding API."""
from neshan import convert


# def geocode(client, address=None, components=None, bounds=None, region=None,
#             language=None):
#     """
#     Geocoding is the process of converting addresses
#     (like ``"1600 Amphitheatre Parkway, Mountain View, CA"``) into geographic
#     coordinates (like latitude 37.423021 and longitude -122.083739), which you
#     can use to place markers or position the map.

#     :param address: The address to geocode.
#     :type address: string

#     :param components: A component filter for which you wish to obtain a
#         geocode, for example: ``{'administrative_area': 'TX','country': 'US'}``
#     :type components: dict

#     :param bounds: The bounding box of the viewport within which to bias geocode
#         results more prominently.
#     :type bounds: string or dict with northeast and southwest keys.

#     :param region: The region code, specified as a ccTLD ("top-level domain")
#         two-character value.
#     :type region: string

#     :param language: The language in which to return results.
#     :type language: string

#     :rtype: list of geocoding results.
#     """

#     params = {}

#     if address:
#         params["address"] = address

#     if components:
#         params["components"] = convert.components(components)

#     if bounds:
#         params["bounds"] = convert.bounds(bounds)

#     if region:
#         params["region"] = region

#     if language:
#         params["language"] = language

#     return client._request("/maps/api/geocode/json", params).get("results", [])


def reverse_geocode(client, latlng):
    """
    Reverse geocoding is the process of converting geographic coordinates into a
    human-readable address.

    :param latlng: The latitude/longitude value for which you wish
        to obtain the closest, human-readable address.
    :type latlng: dict, list, or tuple

    :rtype: list of reverse geocoding results.
    """
    latlng = convert.normalize_lat_lng(latlng)
    params = {
        "lat": latlng[0],
        "lng": latlng[1],
    }

    return client._request("/v2/reverse", params)
