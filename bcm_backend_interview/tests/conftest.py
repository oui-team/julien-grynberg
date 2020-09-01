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


@pytest.fixture()
def barnsley_response() -> List:
    return [
        {"start_time": 1577833200, "end_time": 1577833200, "value": 774},
        {"start_time": 1577834100, "end_time": 1577834101, "value": 682},
        {"start_time": 1578177900, "end_time": 1578178283, "value": 622},
    ]


@pytest.fixture()
def hounslow_response() -> str:
    return (
        "debut,fin,valeur\n1577833200,1577833200,568\n"
        "1577834100,1577834101,770\n1578175200,1578175580,754"
    )
