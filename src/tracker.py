import json
import os
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

SESSIONS_FILE = os.path.join(SCRIPT_DIR, "data", "sessions.json")
CATEGORIES_FILE = os.path.join(SCRIPT_DIR, "data", "categories.json")
DEFAULT_CATEGORIES = []

def load_sessions():
    """Load the list of past session records from disk (empty list if none saved yet)."""
    if os.path.exists(SESSIONS_FILE):
        with open(SESSIONS_FILE, "r") as f:
            return json.load(f)
    else:
        return []

def save_sessions(sessions):
    """Save the list of session records to disk."""
    os.makedirs(os.path.dirname(SESSIONS_FILE), exist_ok=True)
    with open(SESSIONS_FILE, "w") as f:
        json.dump(sessions, f, indent=2)

def start_session(category):
    """Begin timing category right now.
    Returns a dict representing the in-progress session."""
    return {"category": category, "start": datetime.now()}

def stop_session(active_session):
    """Given an in-progress session dict, compute how long it ran.
    Returns a finished session record ready to be saved."""
    end = datetime.now()
    start = active_session["start"]
    duration_seconds = (end - start).total_seconds()
    return {
        "category": active_session["category"],
        "start": start.isoformat(),
        "end": end.isoformat(),
        "duration_seconds": duration_seconds,
    }

def load_categories():
    os.makedirs(os.path.dirname(CATEGORIES_FILE), exist_ok=True)
    if os.path.exists(CATEGORIES_FILE):
        with open(CATEGORIES_FILE, "r") as f:
            return json.load(f)
    else:
        return DEFAULT_CATEGORIES.copy()

def save_categories(categories):
    with open(CATEGORIES_FILE, "w") as f:
        json.dump(categories, f, indent=2)

def add_category(categories, name):
    """Add name to categories if it's not already there.
    Returns True if added, False if it was a duplicate."""
    if name in categories:
        return False
    categories.append(name)
    return True

def delete_category(categories, name):
    """Remove name from categories if it's present.
    Returns True if removed, False if it wasn't found."""
    if name in categories:
        categories.remove(name)
        return True
    return False

if __name__ == "__main__":
    cats = load_categories()
    print("Loaded categories:", cats)
    save_categories(cats)
    print("Saved to", CATEGORIES_FILE)

