import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CATEGORIES_FILE = os.path.join(SCRIPT_DIR, "data", "categories.json")
DEFAULT_CATEGORIES = []

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

