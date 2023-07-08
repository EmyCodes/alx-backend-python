#!/usr/bin/env python3
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns Function that multiplies a float"""
    def multiply_(value: float) -> float:
        """"Inner function multiplies outer"""
        return value * multiplier

    return multiply_
