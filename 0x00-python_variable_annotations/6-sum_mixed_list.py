#!/usr/bin/env python3
from typing import Union


# def sum_mixed_list(mxd_lst: list[int | float]) -> float:
def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """Function takes in mixed list (int and float) as parameter to return float"""

    # returns the sum of the list
    sum_list = sum(mxd_lst)
    return sum_list
