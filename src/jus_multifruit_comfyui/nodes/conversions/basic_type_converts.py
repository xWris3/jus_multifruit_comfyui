from __future__ import annotations
import logging
from typing import Any, Dict, List, Tuple, Union

# ────────────────────────────────────────────────
#   TYPE CONVERSION NODES
# ────────────────────────────────────────────────

#   Common category constants (helps with sorting)
CATEGORY = "_Jus Multifruit/Type conversions"

class IntToString:
    """
    Converts an Int to a String
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_INT": ("INT", {"default": 0}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output_string",)
    FUNCTION = "execute"
    CATEGORY = CATEGORY

    @staticmethod
    def execute(input_INT: int) -> Tuple[str]:
        return ( str(input_INT), )

class StringToInt:
    """
    Converts an String to an Int
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_STRING": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("output_INT",)
    FUNCTION = "execute"
    CATEGORY = CATEGORY

    @staticmethod
    def execute(input_STRING: str) -> Tuple[int]:
        try:
            r =  ( int(input_STRING), )
        except ValueError:
            logging.exception("cannot convert input value. returning 0.")
            r = ( 0, )
        return r

# More nodes can be added here...