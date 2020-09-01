#!/bin/env python3

import argparse
from typing import List, Optional

from bcm_backend_interview.builders.barnsley import build_barnsley
from bcm_backend_interview.builders.hawes import build_hawes
from bcm_backend_interview.builders.hounslow import build_hounslow
from bcm_backend_interview.workers.production_sumer import sum_ppp


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
    hawes = build_hawes(args.from_date, args.to_date)
    barnsley = build_barnsley(args.from_date, args.to_date)
    hounslow = build_hounslow(args.from_date, args.to_date)
    data = sum_ppp([hawes, barnsley, hounslow])
    print(data)
    return 0
