from pandas import DataFrame
from pandas._testing import assert_frame_equal

from bcm_backend_interview.builders.barnsley import BarnsleyBuilder


class TestBarnsleyBuilder:
    def test_rename_attrs(self, barnsley_response):
        barnsley_df = BarnsleyBuilder._convert_to_df(barnsley_response)

        renamed_df = BarnsleyBuilder._rename_attrs(barnsley_df)

        expected_df = DataFrame(
            {
                "start": [1577833200, 1577834100, 1578177900],
                "end": [1577833200, 1577834101, 1578178283],
                "power": [774, 682, 622],
            }
        )
        assert_frame_equal(renamed_df, expected_df, check_like=True)
