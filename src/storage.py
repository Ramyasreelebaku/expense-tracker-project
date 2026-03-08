import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"
DATA_FILE = DATA_DIR / "expenses.json"


def _ensure_data_file() -> None:
    """Create data folder and empty JSON file if missing."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    if not DATA_FILE.exists():
        DATA_FILE.write_text(json.dumps([]), encoding="utf-8")


def load_expenses() -> list[dict]:
    """Load expenses list from JSON file."""
    _ensure_data_file()
    
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, FileNotFoundError):
        print("Warning: Could not load expenses. Starting fresh.")
        return []


def save_expenses(expenses: list[dict]) -> None:
    """Save expenses list to JSON file."""
    _ensure_data_file()
    
    try:
        DATA_FILE.write_text(json.dumps(expenses, indent=2), encoding="utf-8")
    except IOError as e:
        print(f"Error saving expenses: {e}")