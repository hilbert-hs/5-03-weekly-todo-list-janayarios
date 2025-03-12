# 5.03 Weekly ToDo List
selection = ''
todos = {
    "monday": [],
    "tuesday": [],
    "wednesday": [],
    "thursday": [],
    "friday": [],
    "saturday": [],
    "sunday": [],
}

def add(_list):
    daySelect = input("\nWhat day would you like to add to?: ").lower()
    if daySelect in _list:
        addedItem = input(f"\nWhat would you like to add to {daySelect}'s list?: ")
        if addedItem not in todos[daySelect]:
            _list[daySelect].append(addedItem)
            print(f"\nYou have added '{addedItem}' to {daySelect}'s to do list")
        else:
            print("\nYou already have that in the list!")
    else:
        print("\nThat is not a day of the week!")

def get(_list):
    daySelect = input("\nWhat day would you like to get?: ").lower()
    if daySelect in _list:
        print(f"\nFor {daySelect}'s to-do list, you have:\n{_list[daySelect]}")
    else:
        print("\nThat is not a day of the week!")  


while selection != "quit":
    selection = input("\nWould you like to 'add', 'get', or 'quit'?: ")
   
    if selection == "add":  
        add(todos)

    elif selection == "get":
        get(todos)
    