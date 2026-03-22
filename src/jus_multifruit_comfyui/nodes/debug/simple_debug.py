from __future__ import annotations
import logging
from typing import Any, Dict, List, Tuple, Union

# ────────────────────────────────────────────────
#   TYPE CONVERSION NODES
# ────────────────────────────────────────────────

#   Common category constants (helps with sorting)
CATEGORY = "_Jus Multifruit/Debug"

class DebugPythonTypesToConsole:
    """
    Allows all the different "Python datatypes" in, and print it out in the console.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_INT": ("INT", {"default": 0}),
                "input_FLOAT": ("FLOAT", {"default": 0.0}),
                "input_STRING": ("STRING", {"default": ""}),
                "input_BOOLEAN": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ()
    FUNCTION = "execute"
    CATEGORY = CATEGORY

    @staticmethod
    def execute(input_INT: int, input_FLOAT: float, input_STRING: str, input_BOOLEAN: bool) -> str:
        formatted_output = (
            "DebugPythonTypesToConsole Output:\n"
            f"  - input_INT: {input_INT}\n"
            f"  - input_FLOAT: {input_FLOAT}\n"
            f"  - input_STRING: '{input_STRING}'\n"
            f"  - input_BOOLEAN: {input_BOOLEAN}\n"
        )
        print(formatted_output)
        return ()
    

# More nodes can be added here...