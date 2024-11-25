import random

# 1. Define database fields using simple data structures

# set of materials
materials = {"Graphene", "Concrete", "Glass", "Wood", "Recycled Plastics"}

# list of types of building elements
element_types = ["wall", "window", "door", "roof", "floor"]

# tuple of room types
rooms = ("living room", "kitchen", "bathroom", "bedroom", "staircase")

# list of lengths (just hardcoded values for simplicity)
lengths = [3.0, 2.5, 4.0, 5.5, 6.0, 7.0, 1.5, 2.0, 3.5, 4.5]


# 2. Populate the database with nested tuples in a list
ElementDataBase = []

# Adding elements manually for simplicity
ElementDataBase.append(("Element-1", element_types[0], rooms[0], lengths[0], 2.5, "Graphene"))
ElementDataBase.append(("Element-2", element_types[1], rooms[1], lengths[1], 3.0, "Concrete"))
ElementDataBase.append(("Element-3", element_types[2], rooms[2], lengths[2], 4.0, "Glass"))
ElementDataBase.append(("Element-4", element_types[3], rooms[3], lengths[3], 2.8, "Wood"))
ElementDataBase.append(("Element-5", element_types[4], rooms[4], lengths[4], 3.3, "Recycled Plastics"))
ElementDataBase.append(("Element-6", element_types[0], rooms[0], lengths[5], 3.5, "Concrete"))
ElementDataBase.append(("Element-7", element_types[1], rooms[1], lengths[6], 2.0, "Wood"))
ElementDataBase.append(("Element-8", element_types[2], rooms[2], lengths[7], 3.2, "Glass"))
ElementDataBase.append(("Element-9", element_types[3], rooms[3], lengths[8], 4.1, "Graphene"))
ElementDataBase.append(("Element-10", element_types[4], rooms[4], lengths[9], 3.9, "Recycled Plastics"))

# 3. Print the Database

# print entire database
print("Building Elements Database:")
for element in ElementDataBase:
    print(f"ID: {element[0]}, Type: {element[1]}, Room: {element[2]}, Length: {element[3]}m, Height: {element[4]}m, Material: {element[5]}")
