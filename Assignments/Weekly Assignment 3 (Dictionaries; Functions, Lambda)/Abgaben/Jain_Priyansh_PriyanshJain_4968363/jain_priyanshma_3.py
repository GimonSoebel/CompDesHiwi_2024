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

number_of_elements = 3
element_types = ["Column", "Beam", "Slab", "Wall", "Flooring"]
materials = ["Concrete", "Wood", "Brick", "Stone"]
location = ["Bedroom", "Kitchen", "Living Room", "Bathroom", "Hallway"]

# 01_Daatbse Creation
print("\nBuilding Database")
elements_dict = {}

# Function to generate random properties
def GenerateValues(element_type, prefix):
    element_dict = {}
    for i in range(number_of_elements):
        # Generate unique ID
        id = f'{prefix}_{i+1:02}'

        # Random properties
        length = round(random.uniform(3.0, 18.0), 2)
        width = round(random.uniform(2.0, 5.0), 2)
        depth = round(random.uniform(2.0, 5.0), 2)
        location_choice = random.choice(location)
        material_choice = random.choice(materials)

        # Store the data
        element_dict[id] = {
            "type": element_type,
            "location": location_choice,
            "material": material_choice,
            "length": f'{length} m',
            "width": f'{width} m',
            "depth": f'{depth} m'
        }
    return element_dict

# Generate elements for each type and add to the main dictionary
for element_type in element_types:
    prefix = element_type[0]  # First letter of element type (e.g., "B" for Beam)
    elements_dict.update(GenerateValues(element_type, prefix))

for id, details in elements_dict.items():
    print(f'{id} : {details}')

print(f'x'*150)


# 02_Function to add new element:
def AddElement(element_id, element_type, element_location, element_material, length, width, depth):
    # Check if the element_id already exists in elements_dict
    if element_id in elements_dict:
        print(f'Element ID {element_id} already exists. Choose a different ID.')
    else:
        # Add the new element to the dictionary
        elements_dict[element_id] = {
            "type": element_type,
            "location": element_location,
            "material": element_material,
            "length": f'{length} m',
            "width": f'{width} m',
            "depth": f'{depth} m'
        }
        print(f'Element {element_id} added successfully!')

# 03 Function to calculate area and volume"

def CalculateArea(element_key):
    element = elements_dict.get(element_key)  
    if element:
        # Convert dimensions to float 
        length = float(element["length"].replace(" m", ""))
        width = float(element["width"].replace(" m", ""))
        area = round(length * width, 2)
        print(f'The area of {element_key} is {area} sq.m.')
        return area
    else:
        print(f'Element {element_key} not found.')
        return None
        
def CalculateVolume(element_key):
    element = elements_dict.get(element_key)  
    if element:
        # Convert dimesnsions to float 
        length = float(element["length"].replace(" m", ""))
        width = float(element["width"].replace(" m", ""))
        depth = float(element["depth"].replace(" m", ""))
        volume = round(length * width * depth, 2)
        print(f'The volume of {element_key} is {volume} cu.m.')
        return volume
    else:
        print(f'Element {element_key} not found.')
        return None


# 04 Function to get elements by type
def get_elements_by_type(element_type):
    # Empty list for keys of elements that match the specified type
    matching_elements = []

    # Iterate through the elements dictionary
    for element_id, details in elements_dict.items():
        if details["type"].lower() == element_type.lower():
            matching_elements.append(element_id)

    # Return the list of matching element IDs
    if matching_elements:
        return matching_elements
    else:
        print(f"No elements found of type '{element_type}'.")
        return []


#####################################################################

### TO CHECK
'''
# 02_Adding elements in a dictionary
AddElement("W_04", "Wall", "Store", "Brick", 3.3, 6.8, 0.3)

print("\nUpdated Building Elements:")
for id, details in elements_dict.items():
    print(f"{id} : {details}")
print()

## 03_Calculating Area and Volume
CalculateArea("W_04")
CalculateVolume("W_04")
print()

## 04_Getting elements by type
wall_elements = get_elements_by_type("Wall")
print (wall_elements)
print()
'''

