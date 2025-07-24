"""Type stubs for postal.near_dupe module."""

from typing import List, Optional, Sequence, Union

def name_hashes(
    name: Union[str, bytes],
    languages: Optional[Sequence[str]] = None,
    **kw
) -> List[str]: ...

def near_dupe_hashes(  
    labels: Sequence[str],
    values: Sequence[str],
    languages: Optional[Sequence[str]] = None,
    with_name: bool = True,
    with_address: bool = True,
    with_unit: bool = True,
    with_city_or_equivalent: bool = True,
    with_small_containing_boundaries: bool = True,
    with_postal_code: bool = True,    
    with_latlon: bool = False,
    latitude: Optional[float] = None,
    longitude: Optional[float] = None,
    geohash_precision: int = 6,
    name_and_address_keys: bool = True,
    name_only_keys: bool = True,
    address_only_keys: bool = True,
    **kw
) -> List[str]: ...