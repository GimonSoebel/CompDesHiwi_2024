# STEP 1:
# what am I doing?

# creating data base with lists

# Define Data Structures by using lists, sets, and tuples to define various properties of building elements, such as the type, material, dimensions, etc.

#Imagine you're creating a music database instead of a building element database:
#A list of songs would work like my building_type list. You can have the same song repeated in the playlist if you want.
#A set of unique artists ensures you don’t list "Taylor Swift" more than once, similar to how the materials set ensures there’s only one "Glass" material.
#A tuple of genres is fixed, just like the element_types tuple, because I don’t want someone changing or adding to the pre-defined music genres.

materials = {"Concrete", "Glass", "Wood", "Steel", "Brick"}                         # material set {} to ensure materials are unique.
building_type = ["public", "semi public", "private", "governmental", "personal"]    # building_type list [] for ordered and possibly repeatable data.
element_types = ("Wall", "Door", "Window", "Floor", "Ceiling")                      # building element tuple () is a immutable list. Elements are fixed categories that cant be modified accidently.
element_ids = ["Element1", "Element2", "Element3", "Element4", "Element5"]          #  IDs are specific to each building element, and the order may matter if we want to refer to them later.

# STEP 2:
# what am I doing?

# Filling nested tuples in a list by creating a list of building elements, where each building element is represented as a tuple. I'll use the data structures I created earlier to fill in the details of each building element.
# Creating the database list
ElementDataBase = []  # An empty list to store our building elements

# Adding elements manually using data from our structures
ElementDataBase.append(("Element1", "Wall", "public", 3.5, "Concrete"))
ElementDataBase.append(("Element2", "Door", "semi public", 2.0 , "Wood"))
ElementDataBase.append(("Element3", "Window", "private", 1.5 , "Glass"))
ElementDataBase.append(("Element4", "Floor", "governmental", 5.0 , "Recycled Plastics"))
ElementDataBase.append(("Element5", "Ceiling", "personal", 4.2, "Steel"))
ElementDataBase.append(("Element6", "Wall", "private", 6.0, "Brick"))
ElementDataBase.append(("Element7", "Door", "governmental", 2.5, "Steel"))
ElementDataBase.append(("Element8", "Window", "personal", 1.8, "Concrete"))
ElementDataBase.append(("Element9", "Floor", "semi public", 4.0, "Wood"))
ElementDataBase.append(("Element10", "Ceiling", "public", 3.2, "Glass"))

# STEP 3: 

# Printing the database
print("Building Element Database:\n")
for element in ElementDataBase:
    print(f"ID: {element[0]}, Type: {element[1]}, Building Type: {element[2]}, Length: {element[3]}m, Material: {element[4]}")

# Print the total number of elements
print("\nTotal number of elements:", len(ElementDataBase))

# Check if one of the data structures contains at least 5 different options
if len(building_type) >= 5:
    print("\nThe 'building_type' list contains at least 5 different options:", building_type)

# Print one specific property of one specific element
specific_element_index = 2  # Example: choosing the third element (index 2)
specific_property = ElementDataBase[specific_element_index][3]  # Getting the length property
print(f"\nThe length of element at index {specific_element_index} (Element ID: {ElementDataBase[specific_element_index][0]}) is: {specific_property}m")

# Print the three longest elements
ElementDataBase.sort(key=lambda x: x[3], reverse=True)  # Sort by length in descending order
print("\nThe three longest elements are:")
for element in ElementDataBase[:3]:
    print(f"ID: {element[0]}, Length: {element[3]}m, Type: {element[1]}, Building Type: {element[2]}, Material: {element[4]}")

# Group and print elements by building type
print("\nElements grouped by building type:")
for b_type in building_type:
    print(f"\nBuilding Type: {b_type}")
    for element in ElementDataBase:
        if element[2] == b_type:
            print(f"  ID: {element[0]}, Type: {element[1]}, Length: {element[3]}m, Material: {element[4]}")
