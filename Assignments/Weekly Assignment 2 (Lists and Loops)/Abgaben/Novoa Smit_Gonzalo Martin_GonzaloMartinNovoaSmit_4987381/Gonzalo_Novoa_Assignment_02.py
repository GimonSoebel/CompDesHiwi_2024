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

###PROPETIES
type = ("Wall", "Shear-Wall", "Roof", "Ceiling", "Floor", "Facade", "Beams", "Columns", "Door", "Window")
 
typeid = []
for i in range (0, len(type)):
    typeid.append((type[i][0]) + str (1000 +i))
#Alternative
#typeid = [((type[i][0]) + str (1000 +i)) for i in range (0, len(type))]              

room = ("Living Room", "Kitchen", "Bedroom", "Bathroom", "Home Office")

material = ("Concrete", "Wood", "Marble", "Ceramic")

lenght = []

height = []

database = []

var_database = [typeid, type, room, material, lenght, height]
str_database = ["ID", "Type", "Room", "Material", "Lenght", "Height"]


#Random Value Generation

#Lenght 
for i in range(0, (len(type))):
    lenght.append ("L:" + str(round((random.uniform(1, 15)), 2)) + "m")

#Height 
for i in range(0, (len(type))):
    height.append ("H:" +str(round((random.uniform(1, 15)), 2)) + "m")

#Data Base Creation
"""""
i%(len(typeid)
Allows to wrap around list index number
"""
for i in range (0, len(type)):
    database.append ((typeid[(i%(len(typeid)))], type[(i%(len(type)))], room[(i%(len(room)))], material [i%(len(material))], lenght [i%(len(lenght))], height[i%(len(height))]))
  

#Print Data Base
print ("")
print ("Elements Data Base (ID, Type, Room, Material, Lenght, Height):")
print ("")

for i in range (0, len(type)):
    
    print (*database [i], sep =', ')

#Total Number of Elements
print ("")
print ("Total Elements: " + str (len(database)))
print ("")

#Properies with 5 more options
print ("Propeties with 5 or more options:")
print ("")

for i in range (0, len(var_database)):
    if (len (var_database[i])) >= 5:
    
     print (str_database[i])



#INPUT Location of Specific Propeties
print ("")
print ("Locate Specific Element Propety")
print ("Available Elements:" + str(type))
element_inp = input ("Please Type Element: ")
print ("")

print ("Propeties Database:")
print (str_database)
database_type = (database[type.index(element_inp)])
prop_inp = input ("Please type Propety: ")
print ("")
print (str(prop_inp) + " is on number " + str(str_database.index(prop_inp)) + ":")

print (database_type[(str_database.index(prop_inp))])
print ("")