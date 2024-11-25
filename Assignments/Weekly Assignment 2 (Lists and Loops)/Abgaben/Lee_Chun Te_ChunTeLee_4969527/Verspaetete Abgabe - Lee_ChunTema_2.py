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

# Building element types
building_elements=["Wall", "Window", "Floor", "Door", "Ceiling"]

# Room types
rooms= ("Living Room", "Toilet", "Kitchen", "Bathroom", "Office")

#heights definition
# element_heights={"Wall": 3.0, "Window": 1.25, "Floor":0.25, "Door":2.35,"Ceiling":0.15}
element_heights=[3.0, 1.25, 0.25, 2.35, 0.15]
# print("Heights of Elements:", element_heights)

#length defintion
rooms_length=[5.0, 3.0, 3.5, 1.8,3.5]
room_dimensions = dict(zip(rooms, rooms_length))

# Another field
propertyfield = ["property1 ","property2"]

# Another field
propertyfield = {"property1", "property2"}

##add more
room_number={}

## 2. Data base filling using Nested tuples into a List

ElementDataBase = []
for i in range(10):
    House_number= f"House-{i+1}",
    Element_Heights=random.choice(element_heights),
    Building_Elements=random.choice(building_elements),
    Rooms=random.choice(rooms),
    Room_Length=random.choice(rooms_length),
    Materials=random.choice(list(materials)),

    all_element = (room_number,Element_Heights,Building_Elements,Rooms,Room_Length,Materials)

    ElementDataBase.append((House_number, Element_Heights, Building_Elements, Rooms,Room_Length,Materials))   

ElementDataBase.extend([("House-11", 3.0, "Wall", "Office", 3.5, "Concrete"),("House-12", 1.25, "Window", "Kitchen", 3.0, "Glass")])  
   



## 3.Printing Data Base
print("Database Overview:")
for all_element in ElementDataBase:
    print(all_element)
    

# Print the amount of elements
print(f"\nTotal number of elements: {len(ElementDataBase)}")

# Check that one of your data structures contains at least 5 different options or properties
if len(materials) >= 5:
    print("\nThe 'materials' set contains at least 5 different type of options or properties.")

# Print one specific property of one specific element and communicate its location on the list
specific_index = 6 
specific_property = ElementDataBase[specific_index][1] 
print(f"\n For index: {specific_index} property is {specific_property}")
