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

# Available materials
materials = {"Graphene", "Concrete", "Glass", "Wood", "Recycled Plastics"}

# Another field
propertyfield = ["property1 ","property2"]

# Another field
propertyfield = {"property1", "property2"}

##add more

## 2. Data base filling using Nested tuples into a List
ElementDataBase = [
    ("element id or name","height","another property", "another property"), #This is one building element
    ("your second element","height","another property", "another property"), #This is another building element
    ]


## 3.Printing Data Base
print()



#Define the elements


#
id = [0,1,2,3,4,5,6,7,8,9,10]
#list
element_types = ["door", "window", "wall", "floor", "ceiling"]
#Set
room = {"bathroom", "living room", "kitchen","bedroom","hall"}
#tuple
materials = ("glass", "plaster", "wood", "brick", "concrete")

height = [2.7, 3.0, 3.35, 3.2, 1.0]
lenght = [1.5, 1.0, 6.7, 7.0, 3.5]

database = []
elements = [
    (1, 2.7, "door", "bathroom", "glass", 1.5),
    (2, 3.0, "window", "living room", "wood", 1.0),
    (3, 3.35, "wall", "kitchen", "brick", 6.7),
    (4, 1.0, "floor", "bedroom", "wood", 7.0),
    (5, 1.0, "ceiling", "hall", "plaster", 3.5),
    (6, 3.0, "door", "livingroom", "wood", 1.0),
    (7, 2.7, "window", "kitchen", "glass",3.5),
    (8, 3.35, "wall", "bedroom", "plaster", 7.0),
    (9, 1.0, "floor", "hall", "concrete", 3.5),
    (10, 1.0, "ceiling", "bathroom", "plaster", 7.0)
]

for element in elements:
     database.append(element)


 #print database
print("Building Elements Database:")
for element in database:
    print(element)

# Print the total number of elements
print("\nTotal number of elements:", len(database))

# Check that the one of the list contains at least 5 different options
if len(element_types) >= 5:
    print("\nThe 'element_types' list contains at least 5 different options.")

# Print a specific property of a specific element and communicate its location in the list
specific_element = database[2]
print("\nThe third element in the list is:", specific_element)
print("The type of the third element is:", specific_element[2])
