import json
import os

CATEGORIES_FILE = "data/categories.json"
DEFAULT_CATEGORIES = ["reading", "writing", "coding", "research"]

def load_categories():
    if os.path.exists(CATEGORIES_FILE):
        with open(CATEGORIES_FILE, "r") as f:
            return json.load(f)
    else:
        return DEFAULT_CATEGORIES.copy()

def save_categories(categories):
    with open(CATEGORIES_FILE, "w") as f:
        json.dump(categories, f, indent=2)

if __name__ == "__main__":
    cats = load_categories()
    print("Loaded categories:", cats)
    save_categories(cats)
    print("Saved to", CATEGORIES_FILE)

