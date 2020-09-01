from typing import List

import pytest


@pytest.fixture
def hawes_response() -> List:
    return [
        {"start": 1577833200, "end": 1577833200, "power": 710},
        {"start": 1577834100, "end": 1577834101, "power": 627},
        {"start": 1577884500, "end": 1577884557, "power": 518},
        {"start": 1578177900, "end": 1578178283, "power": 750},
    ]
