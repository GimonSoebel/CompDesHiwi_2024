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

def add_element_manually(bimDict):
    user_input_key = input("key:")
    user_input_type = input("type:")
    user_input_room = input("room:")
    user_input_length = float(input("length:"))
    user_input_height = float(input("height:"))
    user_input_thickness = float(input("thickness:"))
    single_element= {
        "type": user_input_type,
        "room": user_input_room,
        "length": user_input_length,
        "height": user_input_height,
        "thickness": user_input_thickness}
    bimDict[user_input_key] = single_element

def add_element_randomly(bimDict):      #just to make testing easier
    user_input_key = input("key:")
    single_element= {
        "type": random.choice(["wall", "window", "door"]),
        "room": random.choice(["living room", "staircase", "kitchen"]),
        "length": (random.random() * 5),
        "height": (random.random() * 5),
        "thickness": random.random()}
    bimDict[user_input_key] = single_element

def calculate_area(bimDict):
    user_input_key = input("key:")
    print(round((bimDict[user_input_key]["length"])*(bimDict[user_input_key]["height"]),2), "m²")

def calculate_volume(bimDict):
    user_input_key = input("key:")
    print(round((bimDict[user_input_key]["length"])*(bimDict[user_input_key]["height"])*(bimDict[user_input_key]["thickness"]), 2), "m³")

def get_elements_by_type(bimDict):
    user_input_type = input("type:")        #get desired type name from user
    n = 0                                   
    indices = []
    types = list(bimDict.values())          #make a list of all the elements (who are still dictionaries) 
    for x in types:                         #for every element
        if x["type"] == user_input_type:    #ask if its type matches the desired one
            indices.append(n)               #and if so, add its index to a list
        n = n+1
    for x in indices:                       #now for every of those indices
        print(list(bimDict.keys())[x])      #print the corresponding key
        #.values and .keys are supposed to return lists, but apparently they don't. chatgpt fixed it for me
    
run = True
while run == True:  #main loop
    user_input_selection = float(input(
        """
        press:
        1 to exit
        2 to add element manually
        3 to add element randomly
        4 to get element area
        5 to get element volume
        6 to get all elements of specified type\n"""))
    if user_input_selection == 1:
        run = False
        break
    if user_input_selection == 2:
        add_element_manually(building_elements)
    if user_input_selection == 3:
        add_element_randomly(building_elements)
    if user_input_selection == 4:
        calculate_area(building_elements)
    if user_input_selection == 5:
        calculate_volume(building_elements)
    if user_input_selection == 6:
        get_elements_by_type(building_elements)

