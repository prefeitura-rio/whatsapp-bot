"""
Helper functions for the handler API.
"""

from typing import Any


_no_default = object()

def get_key(dictionary: dict, key: Any, default: Any=_no_default) -> Any:
    """
    Tries to get a key from a dictionary. If the key is not found,
    returns the default value. If the default value is not specified,
    raises a KeyError.
    """
    if key in dictionary:
        return dictionary[key]
    if default is not _no_default:
        return default
    raise KeyError(key)
