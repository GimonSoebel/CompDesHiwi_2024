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
Id: unique Id.                                                                                              #tuple?
type: The type of the building element. (e.g., "wall," "window," "door," etc.).                             #tuple?
room: The name of the room assigned to the building element. (e.g. "living room", "staircase" etc.)         #list
length: The length of the element in meters.            #list
height: The height of the element in meters.            #list
material: type of material                              #set
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
import random as rand
from tabulate import tabulate          #pls install tabulate with pip

## 1.Define Data Base fields using data structures
fields = ("ID", "Building Element", "Room", "Material", "Length", "Volume")

"""
list of random ids
note to self: change code below to use set, while loop, and counter to ensure unique ids
"""
numofelements = 10          #can use rand to generate arbitrary int of elements

elementoptions = {"Foundation", "Floor", "Column", "Beam", "Wall", "Ceiling", "Roof"}
roomoptions = ("Entry", "Living Room", "Kitchen", "Bathroom", "Bedroom", "Office")
matoptions = ["Steel", "Wood", "Concrete", "Brick", "Stone", "Clay"]
minlength = 0.5
maxlength = 6.0
minvolume = pow(minlength, 3)
maxvolume = 0.5*pow(maxlength, 2)
print (maxvolume)

elementids = []
buildingelements = []
rooms = []
materials = []
lengths = []
volumes = []
for element in range(0,numofelements):
    #generate ids
    idspelledout = rand.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=5)
    currentid = ''
    for character in idspelledout:
        currentid = currentid+character
    elementids.append(currentid)

    #generate building elements
    buildingelements.append(rand.choice(tuple(elementoptions)))

    #generate rooms
    rooms.append(rand.choice(roomoptions))

    #generate materials
    materials.append(rand.choice(matoptions))

    #generate lengths
    lengths.append(round(rand.uniform(minlength, maxlength), 2))

    #generate volumes
    volumes.append(round(rand.uniform(minvolume, maxvolume), 2))

idtuple = tuple(elementids.copy())

## 2. Data base filling using Nested tuples into a List
ElementDataBase = [fields]
for e in range(0,numofelements):
    properties = (idtuple[e], buildingelements[e], rooms[e], materials[e], (str(lengths[e])+" m"), (str(volumes[e])+" m^3"))      #i think this is bad practice
    ElementDataBase.append(properties)

print(tabulate(ElementDataBase))

print("There are ", numofelements, "elements in this database.")
roomsleft = set(roomoptions)-set(rooms)
if roomsleft is not None:
    print("There are no elements from the following rooms: ", roomsleft)
else: 
    print("There is at least one building element from each room")


"""
ElementDataBase = [
    ("element id or name","height","another property", "another property"), #This is one building element
    ("your second element","height","another property", "another property"), #This is another building element
    ]


## 3.Printing Data Base
print()
"""