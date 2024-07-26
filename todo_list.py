import sys

# Function to display the menu
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add To-Do Item")
    print("3. Remove To-Do Item")
    print("4. Exit")

# Function to view the to-do list
def view_list(todo_list):
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for idx, item in enumerate(todo_list, start=1):
            print(f"{idx}. {item}")

# Function to add an item to the to-do list
def add_item(todo_list):
    item = input("\nEnter the to-do item: ")
    todo_list.append(item)
    print(f"'{item}' has been added to your to-do list.")

# Function to remove an item from the to-do list
def remove_item(todo_list):
    view_list(todo_list)
    if todo_list:
        try:
            item_index = int(input("\nEnter the number of the item to remove: ")) - 1
            if 0 <= item_index < len(todo_list):
                removed_item = todo_list.pop(item_index)
                print(f"'{removed_item}' has been removed from your to-do list.")
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main function to run the to-do list application
def main():
    todo_list = []

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ")
        if choice == '1':
            view_list(todo_list)
        elif choice == '2':
            add_item(todo_list)
        elif choice == '3':
            remove_item(todo_list)
        elif choice == '4':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
