#!/bin/env python3

import argparse
from typing import List, Optional

from bcm_backend_interview.builders.hawes import build_hawes


def parse_ppp_params(params: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--from_date",
        type=str,
        default="01-01-2020",
        help="The start date for the search : MM-DD-YYYY",
    )

    parser.add_argument(
        "-t",
        "--to_date",
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
    response = build_hawes(args.from_date, args.to_date)
    print(response)
    return 0
