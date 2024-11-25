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

## 1.Define Data Base fields using data structures

# Defining the floors
floor = [8,3] # respectively number of floors and basements
floor_code = ["F","B"] # F for floor, B for basement

# Defining the position in the plan
axes = (8,20) # respectively number of rows and columns
row = [chr(i) for i in range(97, 97 + axes[0])] # rows named by letters, the function chr() uses the ASCII code
column = [i+1 for i in range(axes[1])] # columns begining from 1

# Available materials
materials = {"Steel", "Reinforced concrete", "Coir geo-textiles", "Glass", "Wood", "Recycled plastics"}

# Types of structural elements
type = ("Wall", "Beam", "Column", "Slab", "Still (window)", "Cantilever", "Window")

# Length
length = [round(random.uniform(0, 8),3) for i in range(30)] # 30 random values between 0 and 8 in meters, rounded to the nearest mm

## 2. Data base filling using Nested tuples into a List

id = []
ElementDataBase = []
i = 0
while i < random.randint(10,30): # at least 10 elements
    if floor[1] != 0:
        id_level = random.choice ([str(random.randint(0,floor[0])) + floor_code[0], str(random.randint(1,floor[1])) + floor_code[1]]) # choose a random level (floor or basement)
    else:
        id_level = str(random.randint(0,floor[0])) + floor_code[0] # choose a random floor if no basement

    # Creating the element properties
    element_level = id_level
    element_type = random.choice (type) # choose a random type
    element_local_plan = str(random.choice (column)) + random.choice (row) # choose a location on the plan
    element_materials = random.choice (list(materials)) # choose a random material
    element_length = random.choice(length) # choose a random length among the proposed values (it means that two elements can have the same length)

    # Creating the element id
    id_type =  element_type[0]
    id_local_plan =  element_local_plan
    id_materials = element_materials[0]
    id_length = str(int(element_length))

    id.extend ([id_type + id_materials + id_length + id_level + id_local_plan]) # add a new id ( and not a list containing the id) to the list

    # Creating the list of elements containing their properties and ids
    ElementDataBase.append ((id[-1], element_type, element_materials, element_length, element_level, element_local_plan)) # add the tuple to the list
    i += 1

index_random = random.randint(0, len(ElementDataBase)) # find a random index 
ElementDataBase.insert(index_random, "This is a test") # add at this index a string

## 3.Printing Data Base

j = 1
for i in ElementDataBase: # print only the tuples which means the elements
    if isinstance(i, tuple):
        print(f"{i} - Element number {j}")
        j += 1

# Print the number of elements

Elements = []
for i in ElementDataBase:
    if isinstance(i,tuple):
        Elements.append(i) # create a list with only tuples with Elements properties

print("The nested list contains " + str(len(Elements)) + " elements")

nbr_of_Elements = sum(1 for element in ElementDataBase if isinstance(element, tuple)) # other way to do it
print("The nested list contains " + str(nbr_of_Elements) + " elements")

# Check that one of your Data structures contains at least 5 different options or properties and communicate it

used_materials = []
if len(materials)>=5:
    for i in materials:
        used_materials.append(i)
    print("The materials used are " + str(used_materials))
else:
    print("The materials list contains less than 5 different properties")


# Print one specific property of one specific element and communicate its location on the list

index_Element = random.randint(0,len(ElementDataBase)-1)

while isinstance(ElementDataBase[index_Element],tuple) == False: # if it is not a tuple and therefore an element
    index_Element = random.randint(0,len(ElementDataBase)-1)

index_Property = random.randint(0,len(ElementDataBase[index_Element])-1)

print("The property is " + str(list(ElementDataBase[index_Element])[index_Property]))
print("It is localetd in the element " + str(list(ElementDataBase[index_Element])) + " in position " + str(index_Property) + " (starting from 0)") # position in the element starting from 0


# Print the 3 longest elements

Elements_sorted = sorted(Elements, key=lambda x:x[3], reverse=True) # sort the list based on the the height in position 3
print("The 3 longest elements are " + str(Elements_sorted[0:3]))





        
    


    



