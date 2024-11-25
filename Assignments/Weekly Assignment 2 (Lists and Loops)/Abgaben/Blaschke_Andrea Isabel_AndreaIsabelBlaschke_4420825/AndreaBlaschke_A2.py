
##Assignment 2: Populating a list of Building Elements##
"""
1. Create hardcoded written Data Structures such as List, Sets, and Tuples that allow you to define a set of options for defining different properties of the elements in the database.
    -Minimum one List, one Set, one Tuple
    -Minimum 4 Data Structures
    -Include Length as one of the fields
    -Optional: fill some of the Data structures with code instead of hardcoding it, but this will require loops or list comprehension    
"""
### 1.Define Data Base fields using data structures

materials = ["Graphene", "Concrete", "Glass", "Wood", "Recycled Plastics", "Metal"] #List
rooms = ["Livingroom", "Bathroom", "Bedroom", "Staircase", "Hallway", "Toilet"] #List
element_type = ("Partition", "Isolation", "Pluming", "Ceiling", "Equipment", "Floor", "Structure") #Tuple
height = {0.5, 1, 1.5, 2, 2.5, 3} #Set
Structural = (True, False) #Tuple

"""
2. Write a series of code lines that fill the database in one List with nested tuples by referring to Data Structures that you defined before.
    -Use List.append, use List.extend, use indexing (e.g. myList[i] = 3)
    -Minimum 10 elements
    Optional challenge (but fun): Use Random by checking the python reference. E.g. Random.randint, Random.choice to fill some of the properties of the elements.
"""

ElementDataBase = [
    ("Columne:",materials[2], rooms[5], element_type[6],Structural[1]), #1
    ("Beam:", materials[5], rooms[4], element_type[4], Structural[1]), #2
    ("Parquet:", materials[3], rooms[1], element_type[6], Structural[0]), #3
    ("Pipe:", materials[5], rooms[2], element_type[3], Structural[0]), #4
    ("Lamp:", materials[3], rooms[1], element_type[5], Structural[1]), #5
    ("Window:", materials[3], rooms[1], element_type[2], Structural[0]), #6
    ("Front Door:", materials[4], rooms[5], element_type[2], Structural[0]), #7
    ("Door Handle:", materials[5], rooms[1], element_type[4], Structural[0]) #8
    ]

ElementDataBase.append(("Lightswitch", materials[4], rooms[1], element_type[4], Structural[0])) #9
ElementDataBase.extend(("Cable Truss", materials[5], rooms[3], element_type[4], Structural[0])) #10


###3. Print the Database with some added strings in a way that is nice to read
#Print the entire database
print("Material Database for Computational Design:")
print(ElementDataBase)

#Print the amount of elements
Database_length = len(ElementDataBase)
print("The Data Base contains " +str(Database_length)+ "Items.")

#Check that one of your Data structures contains at least 5 different options or properties and communicate it
if len(materials) > 5:
    print("The List for materials contains more than 5 Elements")
else:
    print("The List is longer than shorter than 5")

proof_of_difference = set(materials)
print("The Elements in the Materials List are:" +str(proof_of_difference)+ ". They are all different from each other, since the List has been converted into a set")

#Print one specific property of one specific element and communicate its location on the list
print("The Material " +str(ElementDataBase[2][1])+ " is in a Property of the Element Parquet")
location_Property = materials.index(ElementDataBase[2][1])
print("The Item has Index " +str(location_Property)+ " on the Material List.")






