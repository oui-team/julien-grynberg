from typing import List

from pandas import DataFrame

from bcm_backend_interview.builders.base import BasePPBuilder


class HounslowBuilder(BasePPBuilder):
    pp_url = "https://interview.beta.bcmenergy.fr/hounslow"
    output_format = "csv"

    @staticmethod
    def _rename_attrs(df: DataFrame) -> DataFrame:
        return df.rename(columns={"debut": "start", "fin": "end", "valeur": "power"})


def build_hounslow(from_date: str, to_date: str) -> DataFrame:
    return HounslowBuilder(from_date, to_date).build()
