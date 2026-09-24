from datetime import datetime

from tracker import load_categories, save_categories, add_category, delete_category
from tracker import load_sessions, save_sessions, start_session, stop_session

def show_menu():
    print("1. List categories")
    print("2. View sessions in a category")
    print("3. Start timer")
    print("4. Stop timer")
    print("5. Add a category")
    print("6. Delete a category") # Should deleting a category = deleting sessions from that category?
    print("7. Quit")

def list_categories(categories):
    if not categories:
        print("No categories yet.")
        return
    for i, name in enumerate(categories, start=1):
        print(f"{i}. {name}")

def get_category_choice(categories):
    """Ask the user to type a number, return the matching category name (or None if invalid)."""
    list_categories(categories)
    choice = input("Pick a number: ")
    try:
        index = int(choice) - 1
    except ValueError:
        print("That's not a number...")
        return None

    if 0 <= index < len(categories):
        return categories[index]
    else:
        return None

def prompt_new_category():
    name = input("New category name: ").strip()
    return name

def view_category_sessions(sessions, category):
    """Print every past session recorded for category, with its date and duration."""
    matches = [s for s in sessions if s["category"] == category]
    if not matches:
        print(f"No sessions recorded for {category} yet.")
        return
    for s in matches:
        start = datetime.fromisoformat(s["start"])
        minutes = s["duration_seconds"] / 60
        print(f"{start.strftime('%b %d, %I:%M %p')} — {minutes:.1f} min")

def main():
    categories = load_categories()
    sessions = load_sessions()
    active_session = None

    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            list_categories(categories)
        elif choice == "2":
            if not categories:
                print("No categories yet.")
            else:
                name = get_category_choice(categories)
                if name is None:
                    print("Nothing selected.")
                else:
                    view_category_sessions(sessions, name)
        elif choice == "3":
            if active_session is not None:
                print(f"A timer is already running for {active_session['category']}. Stop it first.")
            elif not categories:
                print("No categories yet.")
            else:
                name = get_category_choice(categories)
                if name is None:
                    print("Nothing started.")
                else:
                    active_session = start_session(name)
                    print(f"Started timing {name}.")
        elif choice == "4":
            if active_session is None:
                print("No timer is running.")
            else:
                finished = stop_session(active_session)
                sessions.append(finished)
                save_sessions(sessions)
                minutes = finished["duration_seconds"] / 60
                print(f"Stopped. Logged {minutes:.1f} minutes on {finished['category']}.")
                active_session = None
        elif choice == "5":
            name = prompt_new_category()
            if add_category(categories, name):
                print(f"Added {name}.")
            else:
                print(f"{name} already exists.")
        elif choice == "6": 
            if not categories:
                print("No categories yet.")
            else:
                name = get_category_choice(categories)
                if name is None:
                    print("Nothing deleted.")
                else:
                    delete_category(categories, name)
                    print(f"Deleted {name}.")
        elif choice == "7":
            save_categories(categories)
            print("Saved. Bye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()