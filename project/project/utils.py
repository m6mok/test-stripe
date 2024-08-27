from os import getenv as os_getenv
from typing import TypeVar


T = TypeVar('T')


def getenv(
    key: str,
    *,
    blank=False,
    default: T = None
) -> T:
    '''
    Raises error if key is not in environ.
    Makes type-checking by default value.
    '''
    value = os_getenv(key, default)
    if not blank and value is None:
        raise ValueError(
            'Environment variables are not detected: %s',
            key
        )
    return value
