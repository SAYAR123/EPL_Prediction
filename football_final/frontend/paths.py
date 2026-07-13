# paths.py
from pathlib import Path

# Root of the whole project, computed automatically, works on any machine/OS
BASE_DIR = Path(__file__).resolve().parent.parent   # frontend/ -> project root. One .parent reduced

FRONTEND_DIR = BASE_DIR / "frontend"
DATA_DIR = BASE_DIR / "data"
DUMPED_MODELS_DIR = BASE_DIR / "training" / "dumped_models_vars"
LOGOS_DIR = FRONTEND_DIR / "logos"

EPL_LOGO = FRONTEND_DIR / "EPL_logo.png"
EPL_CSV = DATA_DIR / "epl_final.csv"