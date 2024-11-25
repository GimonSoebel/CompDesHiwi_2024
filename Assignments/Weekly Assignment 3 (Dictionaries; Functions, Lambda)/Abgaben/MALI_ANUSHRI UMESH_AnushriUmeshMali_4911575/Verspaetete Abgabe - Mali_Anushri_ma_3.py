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

import random

# Initial building elements database and reference sets for automatic generation
building_db = {}
element_types = {"wall", "window", "door", "beam", "column", "floor"}
room_types = {"living room", "staircase", "kitchen", "bedroom", "office"}
existing_keys = set()

# Get user input for number of elements to auto-populate
while True:
    try:
        num_elements = int(input("Enter the number of elements to auto-populate in the database: "))
        if num_elements < 0:
            raise ValueError
        break
    except ValueError:
        print("Please enter a positive integer.")

# Automatically generate building elements with random values
for _ in range(num_elements):
    elem_type = random.choice(list(element_types))
    room = random.choice(list(room_types))
    length = random.uniform(0.45, 4.0)  # Random length between 0.45m and 4m
    height = random.uniform(0.45, 4.0)  # Random height between 0.45m and 4m
    thickness = random.uniform(0.05, 2.0)  # Random thickness between 0.05m and 2m
    
    # Generate a unique key for each element
    while True:
        key = elem_type[0].upper() + str(random.randint(100, 999))
        if key not in existing_keys:
            break
    
    existing_keys.add(key)
    building_db[key] = {
        "type": elem_type,
        "room": room,
        "length": length,
        "height": height,
        "thickness": thickness
    }

print("Automatically populated building elements:", building_db)

# Function to add a new element to the database
def add_new_element():
    elem_type = input("Enter the type of element (e.g., wall, window, door): ").lower()
    room = input(f"Enter the room where the {elem_type} is located: ").lower()
    
    while True:
        try:
            length = float(input("Enter the element's length in meters: "))
            height = float(input("Enter the element's height in meters: "))
            thickness = float(input("Enter the element's thickness in meters: "))
            if length <= 0 or height <= 0 or thickness <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter positive values for dimensions.")

    while True:
        key = elem_type[0].upper() + str(random.randint(100, 999))
        if key not in existing_keys:
            break

    existing_keys.add(key)
    building_db[key] = {
        "type": elem_type,
        "room": room,
        "length": length,
        "height": height,
        "thickness": thickness
    }
    
    print(f"Element '{key}' added successfully!")

# Function to calculate the area of an element by its key
def calculate_element_area(element_key):
    if element_key in building_db:
        elem = building_db[element_key]
        area = elem["length"] * elem["height"]
        print(f"The area of the {elem['type']} '{element_key}' is {area} m².")
    else:
        print("Element not found in the database.")

# Function to calculate the volume of an element by its key
def calculate_element_volume(element_key):
    if element_key in building_db:
        elem = building_db[element_key]
        volume = elem["length"] * elem["height"] * elem["thickness"]
        print(f"The volume of the {elem['type']} '{element_key}' is {volume} m³.")
    else:
        print("Element not found in the database.")

# Function to retrieve elements by specified type
def list_elements_by_type(search_type):
    elements_of_type = [key for key, details in building_db.items() if details["type"] == search_type.lower()]
    if elements_of_type:
        print(f"Elements of type '{search_type}': {elements_of_type}")
    else:
        print(f"No elements of type '{search_type}' found.")

# Test functions
add_new_element()
calculate_element_area("W123")  # Replace with an actual key from the database
calculate_element_volume("W123")  # Replace with an actual key from the database
list_elements_by_type("wall")

