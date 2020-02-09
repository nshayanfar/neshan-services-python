Python Client for Google Maps Services
====================================

[![Build Status](https://travis-ci.com/nshayanfar/neshan-services-python.svg?branch=master)](https://travis-ci.org/googlemaps/google-maps-services-python)
[![PyPI version](https://badge.fury.io/py/neshan.svg)](https://badge.fury.io/py/neshan.svg)

## Description

This library is a duplication of https://github.com/googlemaps/google-maps-services-python which is changed to work with Neshan APIs. Please open an issue if you have any questions.

The Python Client for Neshan Services is a Python Client library for the following Neshan
APIs:

 - Directions API
 - Distance Matrix API
 - Reverse Geocoding API
 - Map Matching API
 - Search API

## Requirements

 - Python 3.5 or later.
 - A Neshan API key.

## Installation

    $ pip install -U neshan

Note that you will need requests 2.4.0 or higher if you want to specify connect/read timeouts.

## Usage

This example uses the Geocoding API and the Directions API with an API key:

```python
import neshan
from datetime import datetime

nmaps = neshan.Client(key='Add Your Key here')

# Look up an address with reverse geocoding
reverse_geocode_result = nmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = nmaps.direction((36.268706, 59.610011),
                                    (36.287607, 59.599527),
                                    departure_time=now)
```

## Features

### Retry on Failure

Automatically retry when intermittent failures occur. That is, when any of the retriable 5xx errors
are returned from the API.


## Building the Project


    # Installing nox
    $ pip install nox

    # Running tests
    $ nox

    # Generating documentation
    $ nox -e docs

    # Copy docs to gh-pages
    $ nox -e docs && mv docs/_build/html generated_docs && git clean -Xdi && git checkout gh-pages

## Documentation & resources
### API docs
- [Get Started with Neshan Platform](https://developers.neshan.org/api/)
- [Directions API](https://developers.neshan.org/api/direction)
- [Distance Matrix API](https://developers.neshan.org/api/distance-matrix)
- [Reverse Geocoding API](https://developers.neshan.org/api/reverse-geocoding)
- [Map Matching API](https://developers.neshan.org/api/map-matching)
- [Search API](https://developers.neshan.org/api/search/)

### Support
- [Report an issue](https://github.com/nshayanfar/neshan-services-python/issues)
- [Contribute](https://github.com/nshayanfar/neshan-services-python/blob/master/CONTRIB.md)
