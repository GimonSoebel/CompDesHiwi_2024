material_id= {1,2,3,4,5}
building_element= ["beam", "colomn", "floor", "roof", "ceiling", "stair", "wall_1", "wall_2", "window", "door_1"]
room= [
    ("livingroom", "room_1"),
    ("Bedroom", "room_2"),
    ("kitchen", "room_3"),
    ("bathroom", "room_4")
]


element_length= [10, 0.8, 5, 9, 2.4]
element_height= [0.7, 15, 0.5, 0.8, 0.5, 0.18,3]
material_name= ("wood", "concrete", "gypsum", "glass", "ceramic")
u_values_set = {0.20, 1.10, 1.80, 0.15, 0.14}
# Determine the maximum length
max_lenght= max(len(building_element), len(element_height), len(element_length))

# Extend the lists to the maximum length
while len(building_element) < max_lenght:
    building_element.append(building_element[-1])
while len(element_height) < max_lenght:
    element_height.append(element_height[-1])
while len(element_length) < max_lenght:
    element_length.append(element_length[-1])

# Zip the lists into a nested list
nested_list= list(zip(building_element, element_length, element_height))
print(nested_list)

# use extend
building_element.extend(["door_2", "door_3"])
print(building_element)

# use indexing
print(material_name.index("concrete"))

# 1. Print the entire database
print("\nBuilding Element Database:")
for index, element in enumerate(nested_list):
    print(f"Element {index + 1}: Type: {element[0]}, Length: {element[1]}, Height: {element[2]}")

# 2. Print the amount of elements
print(f"\nTotal number of building elements: {len(building_element)}")

# 3. Check my data structures contains at least 5 different options or properties
print("\nThe material_name tuple contains the following materials:")
for material in material_name:
    print(material)
print(f"Total unique materials: {len(material_name)}")

# 4. Print one specific property of one specific element
print("\nspecific element in this building :")
specific_element = "wood" 
print(f"Element: {specific_element} - Type: {nested_list[7][0]}, Length: {nested_list[7][1]}, Height: {nested_list[7][2]}")


