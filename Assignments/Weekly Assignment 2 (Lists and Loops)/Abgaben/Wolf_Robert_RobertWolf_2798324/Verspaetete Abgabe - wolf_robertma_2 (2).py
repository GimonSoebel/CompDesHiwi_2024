









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
"""
import random

number_of_elements=15
element_list=[]
element_postion= ["Wall","Roof","Floor","Basement"]
materials = ["Concrete", "Glass", "Wood", "Plastics","Steel"]
#dimension_in_x =[1.2,4.6,2.4]
#dimension_in_y =[2.5,3,2.4]
#dimension_in_z =[1.1,4.3,2.3]

for i in range(number_of_elements):#creating nested tuples in a list with descriptive strings
    #each element has an ID, a position, a Material,and x,y and z dimensions
    element_list.append((("ID:",i),("Element position:",random.choice(element_postion)),("Element Material:",random.choice(materials)),("X-Dimension:",round(random.uniform(0,20), 2)),("Y-Dimension:",round(random.uniform(0,20), 2)),("Z-Dimension:",round(random.uniform(0,20), 2))))

print(f"Complete List: {(element_list)}")#print complete list with properties
print()#empty line
print(f"Number of elements: {len(element_list)}")#lenght of list(number of elements)(defined by hardcoded value for number of elements)


index_of_element_to_delete=[]# create empty list for indices of elements to delete
user_input_number_of_elements_to_pop=int(input("How many Elements you want to delete?:"))#how many elements should be deleted



for i in range(int(user_input_number_of_elements_to_pop)):
    user_input_id_to_delete=input(f"index of item number {i+1} to delete:")
    index_of_element_to_delete.append(user_input_id_to_delete)
print("GoodInput")



element_list_deleted=element_list.copy()
#print(element_list)

for i in index_of_element_to_delete:
    print(i)
    element_list_deleted.pop(int(i))

#print(element_list_deleted)

used_materials=set()
biggest_x_dim=0
biggest_y_dim=0
biggest_z_dim=0

for i in range(len(element_list_deleted)):
        used_materials.add(element_list_deleted[i][2][1]) #show used materials
        
        #find biggest dimension
        if element_list_deleted[i][3][1]>biggest_x_dim: #if  X-dimension biger then other x dim
            biggest_x_dim=element_list_deleted[i][3][1]# set as biggest x dim

        if element_list_deleted[i][4][1]>biggest_y_dim: #if  X-dimension biger then other x dim
            biggest_y_dim=element_list_deleted[i][4][1]# set as biggest x dim
        
        if element_list_deleted[i][5][1]>biggest_z_dim: #if  X-dimension biger then other x dim
            biggest_z_dim=element_list_deleted[i][5][1]# set as biggest x dim
print(f"biggest x Dimension: {biggest_x_dim}")
print(f"biggest y Dimension: {biggest_y_dim}")
print(f"biggest z Dimension: {biggest_z_dim}")



if len(used_materials)>=5:
      print("More then 5 Materials used, those are:")
      for i in used_materials:

        print(i)
else:
    print("Less then 5 Materials used, those are:")
    for i in used_materials:

        print(i)



"""revised by ChatGPT for better readability, and nested tuples in list changed as Dictionairy


import random

# Parameters for elements
number_of_elements = 15
element_positions = ["Wall", "Roof", "Floor", "Basement"]
materials = ["Concrete", "Glass", "Wood", "Plastics", "Steel"]

# Generate list of elements with properties as nested tuples
element_list = [
    (
        ("ID:", i),
        ("Element position:", random.choice(element_positions)),
        ("Element Material:", random.choice(materials)),
        ("X-Dimension:", round(random.uniform(0, 20), 2)),
        ("Y-Dimension:", round(random.uniform(0, 20), 2)),
        ("Z-Dimension:", round(random.uniform(0, 20), 2))
    )
    for i in range(number_of_elements)
]

print(f"Complete List: {element_list}\n")
print(f"Number of elements: {len(element_list)}")

# Collect indices of elements to delete
index_of_element_to_delete = []
try:
    user_input_number_of_elements_to_pop = int(input("How many Elements do you want to delete?: "))
    for i in range(user_input_number_of_elements_to_pop):
        while True:
            try:
                index = int(input(f"Index of item number {i + 1} to delete: "))
                if 0 <= index < len(element_list):
                    index_of_element_to_delete.append(index)
                    break
                else:
                    print("Invalid index, please try again.")
            except ValueError:
                print("Please enter a valid integer index.")
except ValueError:
    print("Please enter a valid integer for the number of elements to delete.")

# Remove selected elements by index
element_list_deleted = [element for idx, element in enumerate(element_list) if idx not in index_of_element_to_delete]
print(f"\nNew List with deleted Elements: {element_list_deleted}")

# Analysis of remaining elements
used_materials = set()
biggest_x_dim = biggest_y_dim = biggest_z_dim = 0

for element in element_list_deleted:
    # Unpack tuple for readability
    _, _, (_, material), (_, x_dim), (_, y_dim), (_, z_dim) = element
    used_materials.add(material)

    # Find largest dimensions
    biggest_x_dim = max(biggest_x_dim, x_dim)
    biggest_y_dim = max(biggest_y_dim, y_dim)
    biggest_z_dim = max(biggest_z_dim, z_dim)

print(f"\nBiggest X Dimension: {biggest_x_dim}")
print(f"Biggest Y Dimension: {biggest_y_dim}")
print(f"Biggest Z Dimension: {biggest_z_dim}")

# Display used materials
if len(used_materials) >= 5:
    print("More than 5 Materials used; they are:")
else:
    print("Less than 5 Materials used; they are:")

for material in used_materials:
    print(material)
"""