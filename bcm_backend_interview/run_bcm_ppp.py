#!/bin/env python3

import argparse
from typing import List, Optional


def parse_ppp_params(params: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--from",
        type=str,
        default="01-01-2020",
        help="The start date for the search : MM-DD-YYYY",
    )

    parser.add_argument(
        "-t",
        "--to",
        type=str,
        default="05-01-2020",
        help="The end date for the search : MM-DD-YYYY",
    )

    parser.add_argument(
        "-o",
        "--format",
        type=str,
        default="json",
        help="The output format",
    )

    args = parser.parse_args(params)
    print(args)
    return 0
