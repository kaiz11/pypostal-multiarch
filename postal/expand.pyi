"""Type stubs for postal.expand module."""

from typing import List, Optional, Union, Sequence

def expand_address(
    address: Union[str, bytes],
    languages: Optional[Sequence[str]] = None,
    address_components: Optional[int] = None,
    latin_ascii: bool = True,
    transliterate: bool = True,
    strip_accents: bool = True,
    decompose: bool = True,
    lowercase: bool = True,
    trim_string: bool = True,
    replace_word_hyphens: bool = True,
    delete_word_hyphens: bool = True,
    replace_numeric_hyphens: bool = True,
    delete_numeric_hyphens: bool = True,
    split_alpha_from_numeric: bool = True,
    delete_final_periods: bool = True,
    delete_acronym_periods: bool = True,
    drop_english_possessives: bool = True,
    delete_apostrophes: bool = True,
    expand_numex: bool = True,
    roman_numerals: bool = True,
    **kw
) -> List[str]: ...

def expand_address_root(
    address: Union[str, bytes],
    languages: Optional[Sequence[str]] = None,
    **kw
) -> List[str]: ...

# Address component constants
ADDRESS_NONE: int
ADDRESS_ANY: int
ADDRESS_NAME: int
ADDRESS_HOUSE_NUMBER: int
ADDRESS_STREET: int
ADDRESS_UNIT: int
ADDRESS_LEVEL: int
ADDRESS_STAIRCASE: int
ADDRESS_ENTRANCE: int
ADDRESS_CATEGORY: int
ADDRESS_NEAR: int
ADDRESS_TOPONYM: int
ADDRESS_POSTAL_CODE: int
ADDRESS_PO_BOX: int
ADDRESS_ALL: int