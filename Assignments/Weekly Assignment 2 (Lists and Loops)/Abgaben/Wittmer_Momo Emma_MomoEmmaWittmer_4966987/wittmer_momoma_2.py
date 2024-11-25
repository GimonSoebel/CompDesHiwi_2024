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
materials = {"Graphene", "Concrete", "Glass", "Wood", "Recycled Plastics"}
lenght_m = [2, 3.4, 5, 6.8, 1.5]
room = ("living room", "staircase", "bedroom", "kitchen", "bathroom")
height = [1, 2, 3, 1.5, 2.5, 3.5]

## 2. Data base filling using Nested tuples into a List
ElementDataBase = []
i = 0
while i < 12:
    ElementDataBase.append((random.choice(tuple(materials)), random.choice(lenght_m), random.choice(room), random.choice(height)))
    i = i + 1

## 3.Printing Data Base
print()
print(ElementDataBase)
print()
print("our database has", len(ElementDataBase), "elements")
print("at least one data structure has at least 5 elements:", (4 < (max(len(materials), len(lenght_m), len(room), len(height)))))#
print("property 0 of element 1:", ElementDataBase[1][0])
