"""
Configuration loader for portfolio_parser.
 
This module loads environment variables from .env, validates them, and exports
them as typed module-level constants. All other modules should import from here.
 
Example:
    from config import CACHE_PATH, FIGI_BATCH_SIZE
    cache = CACHE_PATH.read_text()
"""


from pathlib import Path
from dotenv import load_dotenv
import os

# Phase A: Locate & Load
# =======================
PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")


# Phase B: Read & Cast
# ====================
# Read paths as strings, then convert to Path
data_dir_str = os.environ.get("DATA_DIR", "data")
pdf_path_str = os.environ.get("PDF_PATH", "data/estratto.pdf")
cache_path_str = os.environ.get("CACHE_PATH", "data/isin_cache.json")
map_path_str = os.environ.get("MAP_PATH", "data/isin_map.json")

# Convert to Path objects (relative to PROJECT_ROOT)
DATA_DIR = PROJECT_ROOT / data_dir_str
PDF_PATH = PROJECT_ROOT / pdf_path_str
CACHE_PATH = PROJECT_ROOT / cache_path_str
MAP_PATH = PROJECT_ROOT / map_path_str

# Read numeric values and cast immediately
figi_batch_size_str = os.environ.get("FIGI_BATCH_SIZE", "10")
figi_sleep_sec_str = os.environ.get("FIGI_SLEEP_SEC", "2.5")
FIGI_BATCH_SIZE = int(figi_batch_size_str)
FIGI_SLEEP_SEC = float(figi_sleep_sec_str)

# Read string values directly
FIGI_URL = os.environ.get("FIGI_URL", "https://api.openfigi.com/v3/mapping")


# Phase C: Validate & Prepare
# =============================
# Validate numeric constraints
if FIGI_BATCH_SIZE <= 0:
    raise ValueError(
        f"FIGI_BATCH_SIZE must be > 0, got {FIGI_BATCH_SIZE}. "
        f"Check your .env file."
    )

if FIGI_SLEEP_SEC < 0:
    raise ValueError(
        f"FIGI_SLEEP_SEC must be >= 0, got {FIGI_SLEEP_SEC}. "
        f"Check your .env file."
    )

# Validate string constraints
if not FIGI_URL:
    raise ValueError(
        "FIGI_URL is empty. Check your .env file."
    )

# Create directories if they don't exist
try:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
except Exception as e:
    raise ValueError(
        f"Cannot create DATA_DIR at {DATA_DIR}: {e}"
    )

# Ensure parent directory for pdf exists
try:
    PDF_PATH.parent.mkdir(parents=True, exist_ok=True)
except Exception as e:
    raise ValueError(
        f"Cannot create parent directory for PDF_PATH: {e}"
    )

# Ensure parent directory for cache exists
try:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
except Exception as e:
    raise ValueError(
        f"Cannot create parent directory for CACHE_PATH: {e}"
    )

# Ensure parent directory for map exists
try:
    MAP_PATH.parent.mkdir(parents=True, exist_ok=True)
except Exception as e:
    raise ValueError(
        f"Cannot create parent directory for MAP_PATH: {e}"
    )

# Phase D: Export Interface
# ==========================
# All module-level constants are now exported with type hints.
# Other modules should only import from this list:
 
__all__ = [
    "PROJECT_ROOT",
    "DATA_DIR",
    "CACHE_PATH",
    "MAP_PATH",
    "FIGI_URL",
    "FIGI_BATCH_SIZE",
    "FIGI_SLEEP_SEC",
]