#!?usr/bin/env python3
from typing import Mapping, Any, Union
from typing import TypeVar


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[TypeVar, None]) -> Union[Any, TypeVar]:
    if key in dct:
        return dct[key]
    else:
        return default
