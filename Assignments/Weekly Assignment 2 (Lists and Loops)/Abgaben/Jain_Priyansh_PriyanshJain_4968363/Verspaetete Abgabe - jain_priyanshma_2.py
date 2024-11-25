"""
Assignment 2: Populating a list of Building Elements

Imagine you are developing a Building Element Database that stores different fields (properties) to describe a database of different building elements.
Your task is to create a Python program that is hardcoded to automatically fill this database and visualize it:

1. Create hardcoded written Data Structures such as List, Sets, and Tuples that allow you to define a set of options for defining different properties of the elements in the database.
    -Minimum one List, one Set, one Tuple
    -Minimum 4 Data Structures
    -Include Length as one of the fields
    Optional: fill some of the Data structures with code instead of hardcoding it, but this will require loops or list comprehension    

Example of possible properties:
Id: unique Id.
type: The type of the building element. (e.g., "wall," "window," "door," etc.).
room: The name of the room assigned to the building element. (e.g. "living room", "staircase" etc.)
length: The length of the element in meters.
height: The height of the element in meters.
material: type of material
etc.

2. Write a series of code lines that fill the database in one List with nested tuples by referring to Data Structures that you defined before.
    -Use List.append, use List.extend, use indexing (e.g. myList[i] = 3)
    -Minimum 10 elements
    Optional challenge (but fun): Use Random by checking the python reference. E.g. Random.randint, Random.choice to fill some of the properties of the elements.

3. Print the Database with some added strings in a way that is nice to read
    -Print the entire database
    -Print the amount of elements
    -Check that one of your Data structures contains at least 5 different options or properties and communicate it
    -Print one specific property of one specific element and communicate its location on the list
    Optional challenge: requires more python knowledge
        -Print the 3 longest elements
"""
### Base code
import random

## 1. Define Ddata Base fields using data structures

# 01_Location of elements
locations = {"Living Room", "Bedroom", "Kitchen", "Bathroom", "Lobby"}

# 02_Types of elements
types = {"Column" , "Beam ", "Wall ", "Door ", "Window "}

# 03_Types of materials
materials = {"Concrete", "Brick", "Glass", "Wood"}

# 04 & 05_Length & width of elements
lengths = [round(random.uniform(1.0, 5.0),2) for _ in range(10)]

heights = [round(random.uniform(1.0, 3.0),2) for _ in range(10)]

## 2. Database filling 

building_elements =[]

for i in range(10):
    
    element_id = i+1
    element_location = random.choice(list(locations))
    element_type = random.choice(list(types))
    element_material = random.choice(list(materials))
    element_length = random.choice(lengths)
    element_height = random.choice(heights)

    building_elements.append((element_id, element_location, element_type, element_material, element_length, element_height))

# print(building_elements)

## 3. Printing 

# 01_Printing Database

for element in building_elements:
    print(f"ID: {element[0]}, Location: {element[1]}, Type: {element[2]}, Material: {element[3]}, Length: {element[4]}m, Height: {element[5]}m")


# 01_Printing the total number of elements

print(f'\nTotal number of elements: {len(building_elements)}')


# Check if one of the data structures has at least 5 different options

if len(locations) >= 5:
    print("\nThe 'rooms' set contains at least 5 different options.")

# Print one specific property of one specific element

specific_element_user_input = int(input("\nPlease enter an interger corresponding to the element ID to get the length "))-1

if 0 <= specific_element_user_input <= len(building_elements):
    print(f"\nThe length of element with ID {building_elements[specific_element_user_input][0]} "
      f"({building_elements[specific_element_user_input][1]}- {building_elements[specific_element_user_input][2]}) is {building_elements[specific_element_user_input][4]} m.")

else:
    print("\nError: Please add a valid input.")

