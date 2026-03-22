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

# ────────────────────────────────────────────────
#   NODE CLASS MAPPING - required by ComfyUI
# ────────────────────────────────────────────────
NODE_CLASS_MAPPINGS: Dict[str, Type[Any]] = {
    "IntToString": IntToString,
    "StringToInt": StringToInt,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "IntToString": "♻️ IntToString",
    "StringToInt": "♻️ StringToInt"
}


__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
