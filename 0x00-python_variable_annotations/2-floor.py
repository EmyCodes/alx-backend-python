#!/usr/bin/env python3
def floor(n: float) -> int:
    """Using VAriable Annotation,
    Function takes in a float parameter and return the floor of the float
    """
    n_str = str(n)
    n = n_str.split(".")
    return int(n[0])
