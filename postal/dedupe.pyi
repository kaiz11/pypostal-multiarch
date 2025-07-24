"""Type stubs for postal.dedupe module."""

from typing import List, Optional, Sequence, Tuple, Union
from postal.utils.enum import EnumValue

class duplicate_status:
    NULL_DUPLICATE: EnumValue
    NON_DUPLICATE: EnumValue  
    NEEDS_REVIEW: EnumValue
    LIKELY_DUPLICATE: EnumValue
    EXACT_DUPLICATE: EnumValue
    
    @classmethod
    def from_id(cls, status_id: int) -> EnumValue: ...

def place_languages(labels: Sequence[str], values: Sequence[str]) -> List[str]: ...

def is_name_duplicate(
    value1: Union[str, bytes],
    value2: Union[str, bytes], 
    languages: Optional[Sequence[str]] = None
) -> EnumValue: ...

def is_street_duplicate(
    value1: Union[str, bytes],
    value2: Union[str, bytes],
    languages: Optional[Sequence[str]] = None
) -> EnumValue: ...

def is_house_number_duplicate(
    value1: Union[str, bytes],
    value2: Union[str, bytes],
    languages: Optional[Sequence[str]] = None
) -> EnumValue: ...

def is_po_box_duplicate(
    value1: Union[str, bytes],
    value2: Union[str, bytes],
    languages: Optional[Sequence[str]] = None
) -> EnumValue: ...

def is_unit_duplicate(
    value1: Union[str, bytes],
    value2: Union[str, bytes],
    languages: Optional[Sequence[str]] = None
) -> EnumValue: ...

def is_floor_duplicate(
    value1: Union[str, bytes],
    value2: Union[str, bytes],
    languages: Optional[Sequence[str]] = None
) -> EnumValue: ...

def is_postal_code_duplicate(
    value1: Union[str, bytes],
    value2: Union[str, bytes],
    languages: Optional[Sequence[str]] = None
) -> EnumValue: ...

def is_toponym_duplicate(
    labels1: Sequence[str],
    values1: Sequence[str],
    labels2: Sequence[str], 
    values2: Sequence[str],
    languages: Optional[Sequence[str]] = None
) -> EnumValue: ...

def is_name_duplicate_fuzzy(
    tokens1: Sequence[str],
    scores1: Sequence[float],
    tokens2: Sequence[str],
    scores2: Sequence[float],
    languages: Optional[Sequence[str]] = None,
    **kw
) -> Tuple[EnumValue, float]: ...

def is_street_duplicate_fuzzy(
    tokens1: Sequence[str],
    scores1: Sequence[float],
    tokens2: Sequence[str],
    scores2: Sequence[float],
    languages: Optional[Sequence[str]] = None,
    **kw
) -> Tuple[EnumValue, float]: ...