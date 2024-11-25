"""
Assignment 2: Populating a list of Building Elements

Imagine you are developing a Building Element Database that stores different fields (properties) to describe a database of different building elements.
Your task is to create a Python program that is hardcoded to automatically fill this database and visualize it:

1. Create hardcoded written Data Structures such as List, Sets, and Tuples that allow you to define a set of options for defining different properties of the elements in the database.
    -Minimum one List, one Set, one Tuple
    -Minimum 4 properties
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
import uuid

## 1.Define Ddata Base fields using data structures

# Available materials
materials = {"Graphene", "Concrete", "Glass", "Wood", "Recycled Plastics"}

# Available types
type = ["window", "wall", "door", "ceiling", "door"]

# Available rooms
room = {"living room","bedroom", "bathroom", "kitchen", "basement", "attic"}

# Another field
elemID = []

height = []

length = []

##add more

## 2. Data base filling using Nested tuples into a List
ElementDataBase = []
smallerDatabase = []

materials.add('CLT')

# populate the database
for i in range(9):
    newmat = list(materials)[random.randrange(len(materials))]
    newtype = random.choice(type)
    newroom = random.choice(list(room))
    newID = uuid.uuid4()
    elemID.append(newID)
    newheight = random.randrange(1,30)/10
    height.append(newheight)
    newlength = random.randrange(1,45)/10
    length.append(newlength)
    ElementDataBase.append((newmat, newtype, newroom, newID, newheight, newlength))

# populate a smaller database and extend the database with the smaller one.
for i in range(random.randrange(1,9)):
    newmat = list(materials)[random.randrange(len(materials))]
    newtype = random.choice(type)
    newroom = random.choice(list(room))
    newID = uuid.uuid4()
    elemID.append(newID)
    newheight = random.randrange(1,30)/10
    height.append(newheight)
    newlength = random.randrange(1,45)/10
    length.append(newlength)
    smallerDatabase.append((newmat, newtype, newroom, newID, newheight, newlength))
ElementDataBase.extend(smallerDatabase)

    
## 3.Printing Data Base in readable format.
print(materials)
count = 0
for i in ElementDataBase:
    
    print("Element " + str(ElementDataBase[count][3]) + " is a " + 
          str(ElementDataBase[count][0]) + " " + 
          str(ElementDataBase[count][1]) + " in the " +
          str(ElementDataBase[count][2]) + " measuring " +
          str(ElementDataBase[count][4]) + "m high by " +
          str(ElementDataBase[count][5]) + "m long.")
    count = count + 1

print("There are " + str(len(ElementDataBase)) + " elements in the database.")

#Check for 5 properties or options
listLength = [["materials", len(materials)], ["type", len(type)], ["room", len(room)]]

longestList = listLength[0]
count = 0
for i in listLength:
    if listLength[count][1]>listLength[count-1][1]:
        longestList = listLength[count]
    count = count + 1
if longestList[1] < 5:
    print("No data structures have 5 or more options.")
else:
    print("There are " + str(longestList[1])+ " options to choose from in " + str(longestList[0]))

# print a random element property
index = random.randrange(0,len(ElementDataBase))
element = ElementDataBase[index]
print("Element " + str(element[3]) + " is at index " + str(index) + " in the database and is made of " + str(element[0]))

#find the longest element.
longestElement = ElementDataBase[0]
count = 0
for i in ElementDataBase:
    if ElementDataBase[count][5]>longestElement[5]:
        longestElement = ElementDataBase[count]
    count = count + 1
print("The longest element is "+ str(longestElement[3]))


