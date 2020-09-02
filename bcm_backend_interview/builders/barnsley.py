from pandas import DataFrame

from bcm_backend_interview.builders.base import BasePPBuilder


class BarnsleyBuilder(BasePPBuilder):
    pp_url = "https://interview.beta.bcmenergy.fr/barnsley"

    @staticmethod
    def _rename_attrs(df: DataFrame) -> DataFrame:
        return df.rename(
            columns={"start_time": "start", "end_time": "end", "value": "power"}
        )


def build_barnsley(from_date: str, to_date: str) -> DataFrame:
    return BarnsleyBuilder(from_date, to_date).build()
