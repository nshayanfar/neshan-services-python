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

"""Performs requests to the Neshan Static API."""

from neshan import convert


MAPS_MAP_TYPES = set(
    ['osm-bright', 'neshan', 'standard-day', 'standard-night']
)

MAPS_MARKER_TYPES = set(
    ['none', 'red', 'green', 'blue', 'violet']
)


def static_map(client, center,
               zoom, width, height,
               mapType='neshan', marker='none'):
    """
    Downloads a map image from the Maps Static API.

    See https://developers.neshan.org/static-map/getting-started/
    for more info, including more detail for each parameter below.

    :param center: Defines the center of the map, equidistant from all edges
        of the map.
    :type center: dict or list or string

    :param zoom: Defines the zoom level of the map, which determines the
        magnification level of the map.
    :type zoom: int

    :param width: Width of returned image in pixels.
    :type width: int

    :param height: Height of returned image in pixels.
    :type height: int

    :param mapType: defines the type of map to construct. There are several
        possible type values, including osm-bright, neshan, standard-day
        and standard-night.
    :type mapType: string

    :param marker: define the color of maker.
    :type marker: string

    :rtype: iterator containing the raw image data, which typically can be
        used to save an image file locally. For example:

        ```
        f = open(local_filename, 'wb')
        for chunk in client.static_map(size=(400, 400),
                                       center=(52.520103, 13.404871),
                                       zoom=15):
            if chunk:
                f.write(chunk)
        f.close()
        ```
    """

    params = {
        'width': width,
        'height': height
    }

    params["center"] = convert.latlng(center)

    params["zoom"] = zoom

    if mapType not in MAPS_MAP_TYPES:
        raise ValueError("Invalid mapType")
    params["type"] = mapType

    if marker not in MAPS_MARKER_TYPES:
        raise ValueError('Invalid maker')
    params["marker"] = marker

    response = client._request(
        "/v2/static",
        params,
        extract_body=lambda response: response,
        requests_kwargs={"stream": True},
    )
    return response.iter_content()
