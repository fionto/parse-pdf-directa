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
PROJECT_ROOT: Path = Path(__file__).resolve().parents[2]
env_file = PROJECT_ROOT / ".env"

# Fail if .env doesn't exist
if not env_file.exists():
    raise FileNotFoundError(
        f".env file not found at {env_file}\n"
    )
# python-dotenv library is used to load into the environment
load_dotenv(env_file)


# Phase B: Read & Cast
# ====================
# Helper function for path validation
def _resolve_path(env_var: str, default: str) -> Path:
    """Resolve a path from env var: absolute paths pass through, relative paths join to PROJECT_ROOT."""
    raw = os.environ.get(env_var, default)
    p = Path(raw)
    return p if p.is_absolute() else PROJECT_ROOT / p

# Convert to Path objects
DATA_DIR : Path = _resolve_path("DATA_DIR", "data")
PDF_PATH : Path = _resolve_path("PDF_PATH", "data/estratto.pdf")
CACHE_PATH : Path = _resolve_path("CACHE_PATH", "data/isin_cache.json")
MAP_PATH : Path = _resolve_path("MAP_PATH", "data/isin_map.json")

# Read numeric values and cast immediately
_figi_batch_size_str = os.environ.get("FIGI_BATCH_SIZE", "10")
_figi_sleep_sec_str = os.environ.get("FIGI_SLEEP_SEC", "2.5")
FIGI_BATCH_SIZE : int = int(_figi_batch_size_str)
FIGI_SLEEP_SEC : float = float(_figi_sleep_sec_str)

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
except PermissionError as e:
    raise ValueError(
        f"Permission denied: Cannot create DATA_DIR at {DATA_DIR}. "
        f"Check that you have write permission."
    ) from e
except NotADirectoryError as e:
    raise ValueError(
        f"Path error: A parent of DATA_DIR exists but is not a directory: {DATA_DIR}. "
        f"Check your DATA_DIR path in .env."
    ) from e
except OSError as e:
    # Catches other OS errors: symlink loops, disk full, etc.
    raise ValueError(
        f"OS error creating DATA_DIR at {DATA_DIR}: {e}"
    ) from e

# Ensure parent directory for pdf exists
try:
    PDF_PATH.parent.mkdir(parents=True, exist_ok=True)
except PermissionError as e:
    raise ValueError(
        f"Permission denied: Cannot create parent directory for PDF_PATH"
        f"Check that you have write permission to {PDF_PATH.parent.parent}"
    ) from e
except NotADirectoryError as e:
    raise ValueError(
        f"Path error: A parent of PDF_PATH exists but is not a directory. "
        f"Check your PDF_PATH path in .env."
    ) from e
except OSError as e:
    raise ValueError(
        f"OS error creating PDF_PATH parent directory: {e}"
    ) from e

# Ensure parent directory for cache exists
try:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
except PermissionError as e:
    raise ValueError(
        f"Permission denied: Cannot create parent directory for CACHE_PATH. "
        f"Check that you have write permission to {CACHE_PATH.parent.parent}."
    ) from e
except NotADirectoryError as e:
    raise ValueError(
        f"Path error: A parent of CACHE_PATH exists but is not a directory. "
        f"Check your CACHE_PATH path in .env."
    ) from e
except OSError as e:
    raise ValueError(
        f"OS error creating CACHE_PATH parent directory: {e}"
    ) from e

try:
    MAP_PATH.parent.mkdir(parents=True, exist_ok=True)
except PermissionError as e:
    raise ValueError(
        f"Permission denied: Cannot create parent directory for MAP_PATH. "
        f"Check that you have write permission to {MAP_PATH.parent.parent}."
    ) from e
except NotADirectoryError as e:
    raise ValueError(
        f"Path error: A parent of MAP_PATH exists but is not a directory. "
        f"Check your MAP_PATH path in .env."
    ) from e
except OSError as e:
    raise ValueError(
        f"OS error creating MAP_PATH parent directory: {e}"
    ) from e


# Phase D: Export Interface
# ==========================
# All module-level constants are now exported with type hints.
# Other modules should only import from this list:
 
__all__ = [
    "PROJECT_ROOT",
    "DATA_DIR",
    "PDF_PATH",
    "CACHE_PATH",
    "MAP_PATH",
    "FIGI_URL",
    "FIGI_BATCH_SIZE",
    "FIGI_SLEEP_SEC",
]