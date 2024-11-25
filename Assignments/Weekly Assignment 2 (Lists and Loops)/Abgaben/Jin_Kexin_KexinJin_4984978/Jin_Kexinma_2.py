import random

# 1. Define data structures for properties
element_types = ["wall", "window", "door", "roof", "floor"]  # List
rooms = {"living room", "kitchen", "bedroom", "bathroom", "staircase"}  # Set
materials = ("wood", "brick", "concrete", "glass", "metal")  # Tuple
lengths = [random.randint(2, 10) for _ in range(10)]  # List generated with list comprehension

# 2. Fill the database with a list of nested tuples
building_elements = []

for i in range(10):
    element_id = i + 1
    element_type = random.choice(element_types)
    room = random.choice(list(rooms))
    length = lengths[i]
    height = random.randint(1, 5)  # Random height between 1 and 5 meters
    material = random.choice(materials)
    
    building_elements.append((element_id, element_type, room, length, height, material))

# 3. Print the database in a readable format
print("Building Element Database:")
for element in building_elements:
    print(f"ID: {element[0]}, Type: {element[1]}, Room: {element[2]}, "
          f"Length: {element[3]}m, Height: {element[4]}m, Material: {element[5]}")

print(f"\nTotal number of elements: {len(building_elements)}")

# Check that one of the data structures contains at least 5 different options
if len(element_types) >= 5:
    print("The 'element_types' list contains at least 5 different options.")

# Print a specific property of one specific element
specific_element_index = 2  # For example, the 3rd element
print(f"\nElement at index {specific_element_index} has a length of {building_elements[specific_element_index][3]} meters.")

# Optional: Print the 3 longest elements
longest_elements = sorted(building_elements, key=lambda x: x[3], reverse=True)[:3]
print("\nThe 3 longest elements are:")
for element in longest_elements:
    print(f"ID: {element[0]}, Length: {element[3]}m")