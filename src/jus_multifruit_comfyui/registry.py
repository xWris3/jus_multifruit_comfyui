"""
ComfyUI node registry.
"""

from __future__ import annotations

from typing import Dict, Type, Any

# ────────────────────────────────────────────────
#   NODE CLASS IMPORTS
# ────────────────────────────────────────────────
from jus_multifruit_comfyui.nodes.conversions.basic_type_converts import IntToString
from jus_multifruit_comfyui.nodes.conversions.basic_type_converts import StringToInt

from jus_multifruit_comfyui.nodes.debug.simple_debug import DebugPythonTypesToConsole

# ────────────────────────────────────────────────
#   NODE CLASS MAPPING - required by ComfyUI
# ────────────────────────────────────────────────
NODE_CLASS_MAPPINGS: Dict[str, Type[Any]] = {
    "IntToString": IntToString,
    "StringToInt": StringToInt,

    "DebugPythonTypesToConsole": DebugPythonTypesToConsole,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "IntToString": "♻️ IntToString",
    "StringToInt": "♻️ StringToInt",

    "DebugPythonTypesToConsole": "👷 DebugPythonTypesToConsole",
}


__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
