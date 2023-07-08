#!/usr/bin/env python3
from typing import Tuple, Union


# def sum_mixed_list(mxd_lst: list[int | float]) -> float:
def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function takes in mixed list (int and float)
    as parameter to return float"""
    
    return (k, pow(v, 2))
