"""Type stubs for postal.tokenize module."""

from typing import List, Tuple, Union

def tokenize(s: Union[str, bytes], whitespace: bool = False) -> List[Tuple[str, str]]: ...