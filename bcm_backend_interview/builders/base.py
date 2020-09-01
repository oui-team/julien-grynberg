from typing import List

import requests
from pandas import DataFrame


class BasePPBuilder:
    pp_url = ""

    def __init__(self, from_date: str, to_date: str) -> None:
        self.from_date = from_date
        self.to_date = to_date

    def build(self) -> DataFrame:
        try:
            response = self._call_api()
            df = self._convert_to_df(response)
            return self._rename_attrs(df)
        except requests.RequestException as e:
            raise str(e)

    def _call_api(self) -> List:
        return requests.get(
            f"{self.pp_url}?from={self.from_date}&to={self.to_date}"
        ).json()

    @staticmethod
    def _convert_to_df(response: List) -> DataFrame:
        return DataFrame(response)

    @staticmethod
    def _rename_attrs(df: DataFrame) -> DataFrame:
        return df
