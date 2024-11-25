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
building_elements = {}

key = {}
type = {}
room = {}
length = {}
height = {}
thickness = {}
area = {}
volume = {}

def float_input(value):
    while True:
        try:
            return float(input(value))
        except ValueError:
            print("Invalid input. Please enter a number.")

def add_element():

    key = input("Enter a unique key (id) for building element: ")
    type = input("Enter the type of a building element: " )
    room = input("Enter a name of the room assigned to the building element: ")
    length = float_input("Enter the length of the building element in meters: ")
    height = float_input("Enter the heigth of the building element in meters: ")
    thickness = float_input("Enter the thickness of the building element in meters: ")

    area_calc = height * length
    volume_calc = area_calc * thickness

    elements = {"type": type,
        "room": room,
        "length": length,
        "height": height,
        "thickness": thickness
    }
    
    building_elements[key] = elements
    area[key] = round(area_calc,2)
    volume[key] = round(volume_calc,2)


while True:
    print ("\nAdd elements to the 'Building Elements' dictionary. \nIt will have unique ID, type, room, length, height and tickness properties.\n")
    add_element()
    adding_new_item = input("Do you wanna continue add element (yes/no): ")
    if adding_new_item != "yes":
        break 

print("\nThe created 'Building Elements' list is:\n")
for key, element in building_elements.items():
    print(f"Element {key}\nType: {element['type']}\n"
          f"Room: {element['room']}\n"
          f"Length: {element['length']} m\n"
          f"Height: {element['height']} m\n"
          f"Thickness: {element['thickness']} m\n")

for k, v in area.items():
    print(f"The area of the element {k}: {v} m2")

print()
for k, v in volume.items():
    print(f"The volume of the element {k}: {v} m3")

def get_elements_by_type():

    parameter = input("Enter the parameter to search by (e.g., type, room, length, height, thickness): ")
    value = input(f"Enter the value for {parameter}: ")

    if parameter in ["length", "height", "thickness"]:
        try:
            value = float(value)
        except ValueError:
            print(f"Please enter a number for {parameter}.")
            return

    matching_keys = [key for key, element in building_elements.items() if parameter in element and str(element[parameter]) == str(value)]
    
    print()
    if matching_keys:
        print(f"Keys for elements where '{parameter}' is '{value}': {matching_keys}")
    else:
        print(f"No elements found with {parameter} = {value}.")

print()
get_elements_by_type()