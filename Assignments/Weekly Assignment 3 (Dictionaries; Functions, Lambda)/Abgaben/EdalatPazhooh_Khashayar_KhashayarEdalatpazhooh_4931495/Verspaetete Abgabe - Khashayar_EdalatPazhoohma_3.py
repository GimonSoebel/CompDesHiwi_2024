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

#Base Dictionary and Elements Properties

building_elements = {}
element_types = {"wall", "window", "door", "beam", "column", "floor"}
element_rooms = {"living room", "kitchen", "bedroom", "bathroom", "toilet"}
used_keys = set()

#Generating the key for each element

def generate_key(element_type):
    while True:
        key = element_type[0].upper() + str(random.randint(100, 999))
        if key not in used_keys:
            used_keys.add(key)
            return key

#Adding elements

def add_element():
    type_ = input("Enter element type (Somthing like wall, window, door!): ").lower()
    room = input("Enter room name: ").lower()
    try:
        length = float(input("Enter length in meters: "))
        height = float(input("Enter height in meters: "))
        width = float(input("Enter width in meters: "))
        #Checking parts - with the help of ChatGPT
        if length <= 0 or height <= 0 or width <= 0:
            print("Dimensions should be positive!")
            return
    except ValueError:
        print("Invalid input. Please enter numbers for dimensions.")
        return

    key = generate_key(type_)
    building_elements[key] = {
        "type": type_,
        "room": room,
        "length": length,
        "height": height,
        "width": width
    }
    print(f"Element '{key}' added successfully.\n")

def display_areas_and_volumes():
    if not building_elements:
        print("No building elements to display.\n")
        return

    for key, element in building_elements.items():
        area = element["length"] * element["height"]
        volume = element["length"] * element["height"] * element["width"]
        print(f"Element '{key}' (Type: {element['type']}) - Area: {area:.2f} m², Volume: {volume:.2f} m³")
        #I learned how to use f-strings in here from ChatGPT

def get_elements_by_type():
    type_ = input("Enter the element type to retrieve: ").lower()
    matching_elements = [key for key, elem in building_elements.items() if elem["type"] == type_]
    if matching_elements:
        print(f"Elements of type '{type_}': {matching_elements}\n")
    else:
        print(f"No elements of type '{type_}' found.\n")

#Our Fun BIM Program!

print("Welcome to the Building Elements Manager!")

while True:
    add_element()
    display_areas_and_volumes()
    get_elements_by_type()

    more_elements = input("Do you want to add more elements to the database? (only answer with yes or no): ").strip().lower()
    if more_elements != "yes":
        print("Exiting the program. Final database:")
        print(building_elements)
        break

#Thank You!