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

## 1.Define Ddata Base fields using data structures

# set
materials = {"Graphene", "Concrete", "Glass", "Wood", "Recycled Plastics"}

# list
lenghts = [1.0, 1.5, 2.0, 2.5, 3.0]

# list
widths = [0.5, 0.75, 1.0, 1.25, 1.5]

# tuple
types = ("Wall", "Window", "Door", "Floor")

# list
rooms = ["Living Room", "Bathroom", "Bedroom", "Kitchen", "Staircase"]
         
## 2. Data base filling using Nested tuples into a List

# List to hold all elements
ElementDataBase = []

# for loop to fill the database with n (10) elements 
n_elements = 10
for i in range(n_elements):
    element = (
        f"Element_{i+1}",   #fstring to include variable from forloop in string
        random.choice(types),
        random.choice(rooms),
        random.choice(widths),
        random.choice(lenghts),
        random.choice(tuple(materials)),
    )
    ElementDataBase.append(element)


## 3.Printing Data Base
# Print Database
print("Element Database:")
for element in ElementDataBase:
    print(f"ID: {element[0]}, Type: {element[1]}, Room: {element[2]}, Widht: {element[3]}, Lenght: {element[4]}, Material: {element[5]},")

# Print total amount of elements
print("Total amount of elements in database: {}".format(n_elements))

# check if at least 5 properties
if len(rooms) >= 5:
    print("The datastructure Rooms contains at least five different options.")
else:
    print("The datastructure Rooms does not contain at least five different options.")

# index of specific element
element_index = 3 

# printing properity "room" of element at chosen index
#print(f"The room of {ElementDataBase[element_index-1][0]} is {ElementDataBase[element_index][2]} and its location on the list is index")

print(f"The Room of {ElementDataBase[element_index-1][0]} is {ElementDataBase[element_index][2]} and located at index 2 in the Element list")
