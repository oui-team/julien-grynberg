from pandas import DataFrame

from bcm_backend_interview.builders.base import BasePPBuilder


class HawesBuilder(BasePPBuilder):
    pp_url = "https://interview.beta.bcmenergy.fr/hawes"


def build_hawes(from_date: str, to_date: str) -> DataFrame:
    return HawesBuilder(from_date, to_date).build()
