"""Top-level package for jus multifruit nodes."""

import os
import sys
import pkgutil

# ComfyUI import "/nodes"
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(THIS_DIR, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

__path__ = pkgutil.extend_path(__path__, __name__)  # type: ignore[name-defined]

NODES_PKG_DIR = os.path.join(SRC_DIR, "jus_multifruit_comfyui")
if os.path.isdir(NODES_PKG_DIR) and NODES_PKG_DIR not in __path__:
    __path__.append(NODES_PKG_DIR)

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]

__author__ = "POUET POUET"

try:
    from jus_multifruit_comfyui.registry import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
except Exception as e:
    print("Failed to import registry:", repr(e))
    NODE_CLASS_MAPPINGS = {}
    NODE_DISPLAY_NAME_MAPPINGS = {}
