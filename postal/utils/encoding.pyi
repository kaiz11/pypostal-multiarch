"""Type stubs for postal.utils.encoding module."""

from typing import Union

# Type aliases from six
text_type: type
string_types: tuple
binary_type: type

def safe_decode(
    value: Union[str, bytes], 
    encoding: str = 'utf-8', 
    errors: str = 'strict'
) -> str: ...

def safe_encode(
    value: Union[str, bytes],
    incoming: Union[str, None] = None,
    encoding: str = 'utf-8', 
    errors: str = 'strict'
) -> bytes: ...