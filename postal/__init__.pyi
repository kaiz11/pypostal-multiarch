"""Type stubs for postal package."""

# Re-export main functionality for convenience
from postal.expand import expand_address, expand_address_root
from postal.parser import parse_address
from postal.normalize import normalize_string, normalized_tokens
from postal.tokenize import tokenize

__all__ = [
    "expand_address",
    "expand_address_root", 
    "parse_address",
    "normalize_string",
    "normalized_tokens",
    "tokenize"
]