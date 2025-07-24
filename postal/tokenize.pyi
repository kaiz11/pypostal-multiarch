"""Type stubs for postal.tokenize module."""

from typing import List, Tuple, Union
from postal.utils.enum import EnumValue

def tokenize(s: Union[str, bytes], whitespace: bool = False) -> List[Tuple[str, EnumValue]]: ...