import random

element_id = {1,2,3,4,5}

element_type = ["beam", "coloumn", "roof", "wall", "window", "door", "slab", "Fence", "false ceiling", "Furniture"]

room = ["Living Room", "Kitchen", "Bathroom", "Bedroom", "Staircase", "Toilet", "Balcony", "verandah"]

element_material = ("Stone", "Concrete", "Glass", "Wood", "Recycled Plastics", "Gypsum", "steel", "mud", "iorn", "Bamboo")

element_ids = [i+1 for i in range(20)]

# Generate a list of 20 possible lengths for building elements, each between 1.0 and 10.0 meters, rounded to 2 decimal places
lengths = [round(random.uniform(1.0, 10.0), 2) for _ in range(20)]

# Generate a list of 20 possible heights for building elements, each between 2.5 and 6.0 meters, rounded to 2 decimal places
heights = [round(random.uniform(2.5, 6.0), 2) for _ in range(20)]

if len(element_material) >= 5:
    print(f"\nThe 'materials' set contains {len(element_material)} different options.\n")

# 2. Fill the Database with Nested Tuples in a List
element_database = []
for i in range(15):
    element_id = element_ids[i]
    element_type = random.choice(element_type)
    room = random.choice(room)
    length = lengths[i]
    height = heights[i]
    material = random.choice(element_material)

# Append element as a tuple to the database list
    element_database.append((element_id, element_type, room, length, height, material))

# 3. Print the Database
# Print all elements in a readable format
print("Building Elements Database:")
for element in element_database:
    print(f"\n ID: {element[0]}: \n \t Type: {element[1]} \n \t Room: {element[2]} \n \t Length: {element[3]} m \n\t Height: {element[4]} m \n\t Material: {element[5]} " )

#Print the 3 longest elements
sorted_elements = sorted(element_database, key=lambda x: x[3], reverse=True)[:3]
print("\n The 3 longest elements are:")
for element in sorted_elements:
    print(f"   - ID: {element[0]}, Length: {element[3]} m")

# Print the total number of elements
print(f"\n Total number of elements: {len(element_database)}")

# Print one specific property of one specific element and communicate its location
specific_index = random.randint(0, len(element_database) - 1)
selected_element = element_database[specific_index]
print(f"\n Specific detail: The type of building element at index {specific_index + 1} is '{selected_element[1]}', located in the '{selected_element[2]}'.")