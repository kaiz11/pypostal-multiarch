"""Type stubs for postal.token_types module."""

from typing import Set
from postal.utils.enum import Enum, EnumValue

# Re-export constants from C extension
TOKEN_TYPE_WORD: int
TOKEN_TYPE_ABBREVIATION: int
TOKEN_TYPE_IDEOGRAPHIC_CHAR: int
TOKEN_TYPE_HANGUL_SYLLABLE: int
TOKEN_TYPE_ACRONYM: int
TOKEN_TYPE_EMAIL: int
TOKEN_TYPE_URL: int
TOKEN_TYPE_US_PHONE: int
TOKEN_TYPE_INTL_PHONE: int
TOKEN_TYPE_NUMERIC: int
TOKEN_TYPE_ORDINAL: int
TOKEN_TYPE_ROMAN_NUMERAL: int
TOKEN_TYPE_IDEOGRAPHIC_NUMBER: int
TOKEN_TYPE_PERIOD: int
TOKEN_TYPE_EXCLAMATION: int
TOKEN_TYPE_QUESTION_MARK: int
TOKEN_TYPE_COMMA: int
TOKEN_TYPE_COLON: int
TOKEN_TYPE_SEMICOLON: int
TOKEN_TYPE_PLUS: int
TOKEN_TYPE_AMPERSAND: int
TOKEN_TYPE_AT_SIGN: int
TOKEN_TYPE_POUND: int
TOKEN_TYPE_ELLIPSIS: int
TOKEN_TYPE_DASH: int
TOKEN_TYPE_BREAKING_DASH: int
TOKEN_TYPE_HYPHEN: int
TOKEN_TYPE_PUNCT_OPEN: int
TOKEN_TYPE_PUNCT_CLOSE: int
TOKEN_TYPE_DOUBLE_QUOTE: int
TOKEN_TYPE_SINGLE_QUOTE: int
TOKEN_TYPE_OPEN_QUOTE: int
TOKEN_TYPE_CLOSE_QUOTE: int
TOKEN_TYPE_SLASH: int
TOKEN_TYPE_BACKSLASH: int
TOKEN_TYPE_GREATER_THAN: int
TOKEN_TYPE_LESS_THAN: int
TOKEN_TYPE_OTHER: int
TOKEN_TYPE_WHITESPACE: int
TOKEN_TYPE_NEWLINE: int

class token_types(Enum):
    # Word types
    WORD: EnumValue
    ABBREVIATION: EnumValue
    IDEOGRAPHIC_CHAR: EnumValue
    HANGUL_SYLLABLE: EnumValue
    ACRONYM: EnumValue

    # Special tokens
    EMAIL: EnumValue
    URL: EnumValue
    US_PHONE: EnumValue
    INTL_PHONE: EnumValue

    # Numbers and numeric types
    NUMERIC: EnumValue
    ORDINAL: EnumValue
    ROMAN_NUMERAL: EnumValue
    IDEOGRAPHIC_NUMBER: EnumValue

    # Punctuation types
    PERIOD: EnumValue
    EXCLAMATION: EnumValue
    QUESTION_MARK: EnumValue
    COMMA: EnumValue
    COLON: EnumValue
    SEMICOLON: EnumValue
    PLUS: EnumValue
    AMPERSAND: EnumValue
    AT_SIGN: EnumValue
    POUND: EnumValue
    ELLIPSIS: EnumValue
    DASH: EnumValue
    BREAKING_DASH: EnumValue
    HYPHEN: EnumValue
    PUNCT_OPEN: EnumValue
    PUNCT_CLOSE: EnumValue
    DOUBLE_QUOTE: EnumValue
    SINGLE_QUOTE: EnumValue
    OPEN_QUOTE: EnumValue
    CLOSE_QUOTE: EnumValue
    SLASH: EnumValue
    BACKSLASH: EnumValue
    GREATER_THAN: EnumValue
    LESS_THAN: EnumValue

    # Non-letters and whitespace
    OTHER: EnumValue
    WHITESPACE: EnumValue
    NEWLINE: EnumValue

    # Phrase type
    PHRASE: int

    # Token type sets
    WORD_TOKEN_TYPES: Set[EnumValue]
    NUMERIC_TOKEN_TYPES: Set[EnumValue]
    PUNCTUATION_TOKEN_TYPES: Set[EnumValue]
    NON_ALPHANUMERIC_TOKEN_TYPES: Set[EnumValue]