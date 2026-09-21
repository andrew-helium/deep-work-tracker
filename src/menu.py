from tracker import load_categories, save_categories, add_category, delete_category

def show_menu():
    print("1. List categories")
    print("2. Pick a category")
    print("3. Add a category")
    print("4. Delete a category")
    print("5. Quit")

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

def main():
    categories = load_categories()
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
                    print(f"You picked: {name}")
        elif choice == "3":
            name = prompt_new_category()
            if add_category(categories, name):
                print(f"Added {name}.")
            else:
                print(f"{name} already exists.")
        elif choice == "4":
            if not categories:
                print("No categories yet.")
            else:
                name = get_category_choice(categories)
                if name is None:
                    print("Nothing deleted.")
                else:
                    delete_category(categories, name)
                    print(f"Deleted {name}.")
        elif choice == "5":
            save_categories(categories)
            print("Saved. Bye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()