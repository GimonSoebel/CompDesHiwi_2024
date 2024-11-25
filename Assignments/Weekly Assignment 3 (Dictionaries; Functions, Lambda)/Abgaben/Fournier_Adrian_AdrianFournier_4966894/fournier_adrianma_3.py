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

building_elements = {}

# base sets to choose elements from for the automatic population. The add_element function is not constrained to these values.
elem_type = {"wall", "window", "door", "beam", "column", "floor"}
elem_room = {"living room", "staircase", "kitchen", "bedroom", "office"}
elem_key = set({})

#how many elements to populate in the database. User input.
while True:
    try:
        numElements = int(input("How many elements do you want to be auto-populated in the database?"))
        if numElements < 0:
            raise ValueError
        break
    except ValueError:
        print("Please enter a positive integer.")

#automatically populate a database with random values
for i in range(numElements):
    types = random.choice(list(elem_type))
    room = random.choice(list(elem_room))
    length = random.randrange(45,400)/100
    height = random.randrange(45,400)/100
    thickness = random.randrange(5,200)/100
    elem = {"type": types, "room": room, "length": length, "height": height, "thickness": thickness}
    while True:
        key = types[0]+str(random.randrange(1000))
        if key not in elem_key:
            break
    elem_key.add(key)
    building_elements.update({key: elem})
print(building_elements)

# function to add an element to a list
def add_element():
    while True:
        types = input("Please enter the type of element this is")
        elem_type.add(types)
        room = input("What room is this " + str(types)+ " in?")
        elem_room.add(room)
        try:
            length = float(input("Please enter its length in m: "))
            height = float(input("Please enter its height in m: "))
            thickness = float(input("Please enter its thickness in m: "))
            if length < 0 or height < 0 or thickness < 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter dimensions greater than 0: ")
    # this would not work if you had more than 1000 items of the same type
    while True:
        key = types[0]+str(random.randrange(1000))
        if key not in elem_key:
            break
    elem_key.add(key)
    elem = {"type": types, "room": room, "length": length, "height": height, "thickness": thickness}
    building_elements.update({key: elem})
    
add_element()

print(building_elements)

# function to calculate the area of an element
def calculate_area(element_key):
    if element_key in building_elements.keys():
        elem = building_elements[element_key]
        area = elem["length"] * elem["height"]
        print("The area of this " + str(elem["type"]) +  " is " + str(area))
    else:
        print("There is no such element.")

# function to calculate the volume of an element
def calculate_volume(element_key):
    if element_key in building_elements.keys():
        elem = building_elements[element_key]
        volume = elem["length"] * elem["height"] * elem["thickness"]
        print("The area of this " + str(elem["type"]) +  " is " + str(volume))
    else:
        print("There is no such element.")

# function to retrieve all elements by type
def get_elements_by_type(element_type):
    elem_by_type =[]
    for i in building_elements:
        if building_elements[i]["type"] == element_type:
            elem_by_type.append(building_elements[i])
    print(elem_by_type)

get_elements_by_type("wall")
