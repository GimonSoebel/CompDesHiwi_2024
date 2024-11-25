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
# Step 1: Initialize an empty dictionary to store building elements
building_elements = {
    "Door.01.02": {
        "type": "Door",
        "room": "living room",
        "length": 1.5,      # length in meters
        "height": 2.5,      # height in meters
        "thickness": 0.15   # thickness in meters
    },
    "Win.01.01": {
        "type": "window",
        "room": "living room",
        "length": 1.25,      # length in meters
        "height": 1.8,      # height in meters
        "thickness": 0.05   # thickness in meters
    },
    "InW.03.03": {
        "type": "Wall",
        "room": "kitchen",
        "length": 3.5,      # length in meters
        "height": 3.0,      # height in meters
        "thickness": 0.25   # thickness in meters
    }
}

# print(building_elements)

# Step 2: Create a function allows users to add a new building element

# Function to add a new building element to the dictionary
def add_element(key, element_type, room, length, height, thickness):
    # Add a new entry to the building_elements dictionary
    building_elements[key] = {
        "type": element_type,
        "room": room,
        "length": length,
        "height": height,
        "thickness": thickness
    }
    print(f"Element '{key}' added successfully.")

add_element("InW.05.02", "wall", "bedroom", 5.0, 2.5, 0.3)
add_element("Win.01.07", "window", "office", 1.5, 1.2, 0.05)
add_element("Door.02.01", "door", "bathroom", 0.9, 2.1, 0.05)
add_element("InW.01.23", "wall", "living room", 5.0, 2.5, 0.3)
add_element("Win.01.04", "window", "living room", 1.5, 1.2, 0.05)
add_element("Door.02.01", "door", "kitchen", 0.9, 2.1, 0.05)
add_element("Win.01.02", "window", "bedroom", 1.0, 1.5, 0.05)
# print(building_elements)

# Step 3 :Create a function
# Function to calculate area (length * height) of a building element
def calculate_area(key):
    element = building_elements.get(key)
    if element:
        area = element["length"] * element["height"]
        return area
    else:
        return "Element not exist."

# Function to calculate volume (length * height * thickness) of a building element
def calculate_volume(key):
    element = building_elements.get(key)
    if element:
        volume = element["length"] * element["height"] * element["thickness"]
        return volume
    else:
        return "Element not exist."
    
print("Area of InW.05.02:", calculate_area("InW.05.02"), "m^2")
print("Volume of Win.01.01:", calculate_volume("Win.01.01"), "m^3")

# Step 4 :
def get_elements_by_type(element_type):
    # List comprehension to find keys where the type matches the specified type
    elements_of_type = [key for key, value in building_elements.items() if value["type"] == element_type]
    return elements_of_type

# Get all elements of type e.g "window"
print("Get All window elements:", get_elements_by_type("window"))