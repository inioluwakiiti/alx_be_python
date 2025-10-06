def add_item(shopping_list, item):
    """Add an item to the shopping list."""
    shopping_list.append(item)
    print(f"{item} added to the list.")


def remove_item(shopping_list, item):
    """Remove an item from the shopping list if it exists."""
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the list.")
    else:
        print(f"{item} not found in the list.")


def display_list(shopping_list):
    """Display all items in the shopping list."""
    print("\nShopping List:")
    for i, item in enumerate(shopping_list, 1):
        print(f"{i}. {item}")
    print()


# --- TEST CODE ---
if __name__ == "__main__":
    my_list = []
    add_item(my_list, "Milk")
    add_item(my_list, "Bread")
    display_list(my_list)
    remove_item(my_list, "Milk")
    display_list(my_list)
