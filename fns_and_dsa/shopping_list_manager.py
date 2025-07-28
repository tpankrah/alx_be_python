shopping_list = []

def add_item(item):
    shopping_list.append(item)
    return True

def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        return True
    
def show_items():
    return shopping_list


def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        

        if choice == '1':
            # Prompt for and add an item
            item = (input('Enter the item to add: '))
            if add_item(item):
                print(f'{item} added to shopping list ')

        elif choice == '2':
            # Prompt for and remove an item
            item = (input('Please enter item name '))            
            remove_item(item)
            print(f'{item} removed from shopping list ')

        elif choice == '3':
            # Display the shopping list
             items = show_items()
             for item in items:
                 print(item)

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    print(shopping_list)

if __name__ == "__main__":
    main()
