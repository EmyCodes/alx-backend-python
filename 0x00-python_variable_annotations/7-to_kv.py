#!/usr/bin/env python3
from typing import Tuple, Union


# def sum_mixed_list(mxd_lst: list[int | float]) -> float:
def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Type-annotated function  that takes a string k and an int OR
    float v as arguments and returns a tuple."""

    return (k, pow(v, 2))
