"""Type stubs for postal.normalize module."""

from typing import List, Optional, Tuple, Union, Sequence
from postal.utils.enum import EnumValue

# String options constants
NORMALIZE_STRING_LATIN_ASCII: int
NORMALIZE_STRING_TRANSLITERATE: int
NORMALIZE_STRING_STRIP_ACCENTS: int
NORMALIZE_STRING_DECOMPOSE: int
NORMALIZE_STRING_LOWERCASE: int
NORMALIZE_STRING_TRIM: int
NORMALIZE_STRING_REPLACE_HYPHENS: int
NORMALIZE_STRING_SIMPLE_LATIN_ASCII: int
NORMALIZE_STRING_REPLACE_NUMEX: int

DEFAULT_STRING_OPTIONS: int
STRING_OPTIONS_NUMEX: int

# Token options constants
NORMALIZE_TOKEN_REPLACE_HYPHENS: int
NORMALIZE_TOKEN_DELETE_HYPHENS: int
NORMALIZE_TOKEN_DELETE_FINAL_PERIOD: int
NORMALIZE_TOKEN_DELETE_ACRONYM_PERIODS: int
NORMALIZE_TOKEN_DROP_ENGLISH_POSSESSIVES: int
NORMALIZE_TOKEN_DELETE_OTHER_APOSTROPHE: int
NORMALIZE_TOKEN_SPLIT_ALPHA_FROM_NUMERIC: int
NORMALIZE_TOKEN_REPLACE_DIGITS: int

DEFAULT_TOKEN_OPTIONS: int
TOKEN_OPTIONS_DROP_PERIODS: int
DEFAULT_TOKEN_OPTIONS_NUMERIC: int

def remove_parens(tokens: List[Tuple[str, int]]) -> List[Tuple[str, int]]: ...

def normalize_string(
    s: Union[str, bytes],
    string_options: int = DEFAULT_STRING_OPTIONS,
    languages: Optional[Sequence[str]] = None
) -> str: ...

def normalized_tokens(
    s: Union[str, bytes],
    string_options: int = DEFAULT_STRING_OPTIONS,
    token_options: int = DEFAULT_TOKEN_OPTIONS,
    strip_parentheticals: bool = True,
    whitespace: bool = False,
    languages: Optional[Sequence[str]] = None
) -> List[Tuple[str, EnumValue]]: ...