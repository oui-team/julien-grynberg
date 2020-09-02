from pandas import DataFrame

from bcm_backend_interview.builders.hounslow import HounslowBuilder


class TestHounslow:
    def test_convert_bytes_to_df(self, hounslow_response):
        converted_response = HounslowBuilder._convert_bytes_to_df(hounslow_response)

        expected_df = DataFrame(
            {
                "debut": [1577833200, 1577834100, 1578175200],
                "fin": [1577833200, 1577834101, 1578175580],
                "valeur": [568, 770, 754],
            }
        )
