"""Type stubs for postal.parser module."""

from typing import List, Optional, Union, Tuple

def parse_address(
    address: Union[str, bytes],
    language: Optional[str] = None,
    country: Optional[str] = None
) -> List[Tuple[str, str]]: ...