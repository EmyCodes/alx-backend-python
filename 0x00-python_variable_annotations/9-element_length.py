#!/usr/bin/python3
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence]]:
    """Assigned Variable annotation to the function"""
    return [(i, len(i)) for i in lst]
