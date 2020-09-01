from typing import List

import requests
from pandas import DataFrame


class HawesBuilder:
    pp_url = "https://interview.beta.bcmenergy.fr/hawes"

    def __init__(self, from_date: str, to_date: str) -> None:
        self.from_date = from_date
        self.to_date = to_date

    def build(self) -> DataFrame:
        try:
            response = self._call_api()
            return self._convert_to_df(response)
        except requests.RequestException as e:
            raise str(e)

    def _call_api(self) -> List:
        return requests.get(
            f"{self.pp_url}?from={self.from_date}&to={self.to_date}"
        ).json()

    @staticmethod
    def _convert_to_df(response: List) -> DataFrame:
        return DataFrame(response)


def build_hawes(from_date: str, to_date: str) -> DataFrame:
    return HawesBuilder(from_date, to_date).build()
