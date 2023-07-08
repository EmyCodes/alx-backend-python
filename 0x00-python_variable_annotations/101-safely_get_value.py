#!/usr/bin/env python3
from typing import Mapping, Any, Union, TypeVar

def safely_get_value(dct: Mapping, key: Any,
                     default: Union[TypeVar, None]) -> Union[Any, TypeVar]:
    """Worked on thi codebase"""
    if key in dct:
        return dct[key]
    else:
        return default
