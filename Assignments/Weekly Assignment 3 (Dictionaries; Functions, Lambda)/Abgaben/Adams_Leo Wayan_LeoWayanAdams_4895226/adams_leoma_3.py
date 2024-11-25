"""
Assignment 3: Building Information Modeling (BIM) Tool

Imagine you are developing a Building Information Modeling (BIM) Tool that stores information about different building elements.
Your task is to create a Python program that interacts with the user to collect and analyse data using dictionaries, built-in functions, UDFs or lambda. 
The program should perform the following tasks:

1.  Create a dictionary called building_elements that will store information about various building elements.
Each element should be identified by a unique key (e.g., a string or integer).
The value associated with each key should be another dictionary containing the following information: type, room, length, height, thickness.

key: The unique key for the element. (e.g. InW.01.23)
type: The type of the building element. (e.g., "wall," "window," "door," etc.).
room: The name of the room assigned to the building element. (e.g. "living room", "staircase" etc. )
length: The length of the element in meters.
height: The height of the element in meters.
thickness: The width of the element in meters.

2. Create a function called add_element that allows users to add a new building element to the building_elements dictionary.
This function should contained the previous contained parameters:

3. Create a function called calculate_area that calculates and returns the area of a building element in m2.
Create a function called calculate_volume that calculates and returns the volume of a building element in m3.
The above two functions should take a key as a parameter and use the information from the building_elements dictionary to perform the calculations.

4. Create a function called get_elements_by_type that takes a type (e.g., "wall," "window," "door") as a parameter and
returns a list of keys for all building elements of that specific type.
"""

# create dict building_elements with various elements
    # unique element key
    # key value in another dict for 1 type 2 room 3 lenght 4 height 5 thickness

building_elements = {
    'BE.1': {
        'type':'wall',
        'room':'living room',
        'lenght':'2.0',
        'height':'3.0',
        'thickness':'0.25',
    },
    'BE.2': {
        'type':'window',
        'room':'staircase',
        'lenght':'1.0',
        'height':'1.5',
        'thickness':'0.1',
    },
    'BE.3': {
        'type':'door',
        'room':'kitchen',
        'lenght':'1.0',
        'height':'2.2',
        'thickness':'0.2',
    }
}
# function add_element to buidling_eleements
def add_element():
    new_key = 'BE.{}'.format(len(building_elements)+1)
    print("Element {} has been created. Add its type, room, lenght, height and thickness,".format(new_key))
    while True:
        new_type = input("Enter Type (Letters only): ")
        if (new_type.isalpha()):
            new_type = str(new_type.lower())
            break
        else:
            print("LInvalid Input! etters only, no numbers or special symbols!")
    
    while True:
        new_room = input("Enter Room (Letters only): ")
        if (new_room.isalpha()):
            new_room = str(new_room.lower())
            break
        else:
            print("Invalid Input! Letters only, no numbers or special symbols!")   

    while True: #asked chatgpt on how to test for numerical input. suggested try / except
        try:
            new_length = float(input("Enter Length (in meters): "))
            break
        except ValueError:
            print("Invalid Input! Numbers only, no letter or special symbols!")

    while True: 
        try:
            new_height = float(input("Enter Height (in meters): "))
            break
        except ValueError:
            print("Invalid Input! Numbers only, no letter or special symbols!")

    while True: 
        try:
            new_thickness = float(input("Enter Thickness (in meters): "))
            break
        except ValueError:
            print("Invalid Input! Numbers only, no letter or special symbols!")

    while True:
        print(f"You created Element: {new_key}, with Type: {new_type}, Room: {new_room}, "
        f"Length: {new_length}, Height: {new_height}, and Thickness: {new_thickness}."
        )
        confirmation = input(f"Do you want to add Element {new_key} to the Building Elements Database? (y/n): ").lower()
        if confirmation == 'y':
            building_elements[new_key] = {
                'type': new_type,
                'room': new_room,
                'lenght': new_length,
                'height': new_height,
                'thickness': new_thickness,
            }
            print(f"Element {new_key} has been added to the Building Elements Database")
            break
        elif confirmation == 'n':
            print(f"Element {new_key} was added to the Building Elements Database :(")
            break
        else:
            print("Invalid Input! Please type 'y' for yes or 'n' for no.")
    
def calculate_area():
    while True:
        key = input("Enter the Element Key (e.g. BE.1): ")

        if key in building_elements:
            element = building_elements[key]

            try:
                area = float(element['lenght']) * float(element['thickness'])
                print(f"The area of Building Element {key} is {area:.2f} m²") #.2f formatting to floating point with 2 decimal places, asked cgpt
                return
            except (ValueError):
                print(f"Invalid Input! Element {key} has invalid 'lenght' or 'thickness' properties")
                return
        else:
            print(f"Invalid Key! '{key}' doesn't exist  in the Building Element Database. Please try again")
            return

def calculate_volume():
    while True:
        key = input("Enter the Element Key (e.g. BE.1): ")

        if key in building_elements:
            element = building_elements[key]

            try:
                volume = float(element['lenght']) * float(element['thickness']) * float(element['height'])
                print(f"The volume of Building Element {key} is {volume:.2f} m³") #.2f formatting to floating point with 2 decimal places
                return
            except (ValueError):
                print(f"Invalid Input! Element {key} has invalid 'lenght', 'thickness', or 'height' properties")
                return
        else:
            print(f"Invalid Key! '{key}' doesn't exist  in the Building Element Database. Please try again")
            return

def get_elements_by_type():
    search_type = input("Enter the type of building element (e.g. 'wall'): ").strip().lower() #strip removes spaces

    # initialze emtpy list to store matching keys
    matching_keys = []

    #loop through all key values in building dict
    for key, element in building_elements.items():
        if element['type'].lower() == search_type:
            matching_keys.append(key)
    
    if matching_keys:
        print(f"The following Building Elements contain the type {search_type}: {matching_keys}")
    else:
        print(f"There are no Building Elements that contain the type {search_type}.")
    
    return matching_keys

def print_database():
    print("\nBuilding Element Database:")
    for key in building_elements:
        element = building_elements[key]
        print(f"{key}: {element}")
    
def menu():
    while True:
        print("\nWelcome to the Building Element Databse:")
        print("1. Add a new Building Element BE")
        print("2. Print the complete Database")
        print("3. Calculate the Area of a Building Element")
        print("4. Calculate the Volume of a Building Element")
        print("5. Search the Building Element by type")
        print("6. Exit the Database")
        print()

        try:
            user_choice = int(input("Enter a number 1-6: ").strip())
        except ValueError:
            print("Invalid Input! Enter a number between 1 and 6." )
            continue

        if user_choice == 1:
            add_element()
        elif user_choice == 2:
            print_database()     
        elif user_choice == 3:
            calculate_area()
        elif user_choice == 4:
            calculate_volume()
        elif user_choice == 5:
            get_elements_by_type()
        elif user_choice == 6:
            print("Exiting the Database.")
            break
        else:
             print("Invalid Input! Enter a number between 1 and 6." )

menu()