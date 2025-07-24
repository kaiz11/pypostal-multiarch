"""Type stubs for postal package."""

# Main functionality - most commonly used
from postal.expand import expand_address, expand_address_root
from postal.parser import parse_address
from postal.normalize import normalize_string, normalized_tokens
from postal.tokenize import tokenize

# Additional modules available for import
from postal import dedupe, near_dupe, token_types, utils

__all__ = [
    "expand_address",
    "expand_address_root", 
    "parse_address",
    "normalize_string",
    "normalized_tokens",
    "tokenize",
    "dedupe",
    "near_dupe", 
    "token_types",
    "utils"
]