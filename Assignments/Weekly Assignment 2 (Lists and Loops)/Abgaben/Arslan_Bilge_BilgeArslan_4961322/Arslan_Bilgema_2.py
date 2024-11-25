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
import random

## 1.Define Data Base fields using data structures

id = [ 1,2,3,4,5,6,7,8,9,10 ]
building_elements = ("Wall", "Column", "Beam", "Window", "Door", "Floor", "Partition Wall")
materials = ["Concrete", "Glass", "Wood", "Recycled Plastics", "Steel", "Paper"]
rooms = ("Living Room ","Bedroom", "Kitchen", "Entrance", "Bathroom", "Balcony")
length = {0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0}
heights = {0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0}

length = sorted(length)
heights = sorted(heights)

## 2. Data base filling using Nested tuples into a List
element_database = []

element_database.append((id[0], building_elements[0], materials[0], rooms[0], length[7], heights[6]))
element_database.append((id[1], building_elements[1], materials[0], rooms[0], length[0], heights[7]))
element_database.append((id[2], building_elements[2], materials[0], rooms[0], length[9], heights[0]))
element_database.append((id[3], building_elements[3], materials[1], rooms[5], length[1], heights[3]))
element_database.append((id[4], building_elements[4], materials[2], rooms[1], length[1], heights[3]))

element_database.append((id[5], building_elements[4], materials[4], rooms[3], length[1], heights[3]))
element_database.append((id[6], building_elements[5], materials[2], rooms[1], length[9], heights[11]))
element_database.append((id[7], building_elements[5], materials[3], rooms[2], length[7], heights[9]))
element_database.append((id[8], building_elements[6], materials[3], rooms[3], length[2], heights[6]))
element_database.append((id[9], building_elements[6], materials[5], rooms[4], length[3], heights[4]))

# 3. Printing the entire database
print("Building Element Database:")
print()

for element in element_database:
    print(f"ID: {element[0]}, Type: {element[1]}, Material: {element[2]}, Room: {element[3]}, Length: {element[4]}, Height: {element[5]}")
print()

# Print the amount of elements in the database
print("Total number of elements in the database:", len(element_database))
print()

# Check that one of your Data structures contains at least 5 different options or properties and communicate it
if len(materials) >= 5:
    print("The 'materials' data structure contains at least 5 different options:", materials)
print()

# Print one specific property of one specific element and communicate its location on the list
specific_element = 4
property_to_print = "Room"
print(f"The '{property_to_print}' of the element at index {specific_element} (ID: {element_database[specific_element][0]}) is: {element_database[specific_element][3]}")
