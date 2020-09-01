from io import StringIO
from typing import List, ByteString

import requests
from pandas import DataFrame, read_csv
from requests import Response


class BasePPBuilder:
    pp_url = ""
    output_format = "json"

    def __init__(self, from_date: str, to_date: str) -> None:
        self.from_date = from_date
        self.to_date = to_date

    def build(self) -> DataFrame:
        try:
            response = self._call_api()
            if self.output_format == "json":
                df = self._convert_list_to_df(response.json())
            else:
                df = self._convert_bytes_to_df(str(response.content, "utf-8"))
            return self._rename_attrs(df)
        except requests.RequestException as e:
            raise str(e)

    def _call_api(self) -> Response:
        return requests.get(f"{self.pp_url}?from={self.from_date}&to={self.to_date}")

    @staticmethod
    def _convert_list_to_df(response: List) -> DataFrame:
        return DataFrame(response)

    @staticmethod
    def _convert_bytes_to_df(response: str) -> DataFrame:
        return read_csv(StringIO(response))

    @staticmethod
    def _rename_attrs(df: DataFrame) -> DataFrame:
        return df
