from pandas import DataFrame
from pandas._testing import assert_frame_equal

from bcm_backend_interview.builders.hawes import HawesBuilder


class TestHawesBuilder:
    def test_convert_to_df(self, hawes_response):
        expected_result = DataFrame(
            {
                "start": [1577833200, 1577834100, 1577884500, 1578177900],
                "end": [1577833200, 1577834101, 1577884557, 1578178283],
                "power": [710, 627, 518, 750],
            }
        )

        converted_result = HawesBuilder._convert_to_df(hawes_response)

        assert_frame_equal(expected_result, converted_result, check_like=True)
