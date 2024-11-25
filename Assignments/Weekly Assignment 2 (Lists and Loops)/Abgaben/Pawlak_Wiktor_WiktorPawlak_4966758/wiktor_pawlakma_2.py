import random 
const_len = 20

##0. Make unique ids -> could be => def MkeIds()
'''
https://docs.python.org/3/library/hashlib.html
'''
import hashlib

ids = list(range(0, const_len))
hashes = []
for value in ids:
    # Make the hash obect -> sha256
    h = hashlib.sha256()  
    h.update(str(value).encode())  
    # get the hexadecimal digit 
    hashes.append(h.hexdigest()) 

## 1.Define Ddata Base fields using data structures

# Materiasl (Set)
materials = {"Graphene", "Concrete", "Glass", "Wood", "Recycled Plastics"}

# Element types (Tuple)
element_types = ("Wall", "Window", "Door", "Column", "Beam")

# Rooms (List)
rooms = ["Living Room", "Bedroom", "Kitchen", "Bathroom", "Staircase"]

# Hardcoding additions
rooms.append('Balcony')
materials.add('Asbestos :))))')
rooms[2], rooms[3] = rooms[3], rooms[2]

# Adding to the tuple's not possible but...
element_types_list = list(element_types)  # Convert tuple to list
element_types_list.extend(['Tiles', 'Lamp'])  # Extend the list
element_types = tuple(element_types_list)  # Convert back to tuple

## 2. Fill the dictionary (The task was with tuples but I decided to do this with dictionaries)

ElementDataBase = []

#loop through const len 0 to const len to fill the dictionary const_len times 
for i in range(const_len):
    element_id = hashes[i]
    element_type = random.choice(element_types)
    room = random.choice(rooms)
    length = round(random.uniform(1.0, 10.0), 2)  # Length between 1.0 and 10.0 meters
    height = round(random.uniform(2.0, 5.0), 2)   # Height between 2.0 and 5.0 meters
    material = random.choice(list(materials))
    
    # Create a dictionary for each element
    element = {
        "ID":  element_id,
        "Type": element_type,
        "Room": room,
        "Length": length,
        "Height": height,
        "Material": material,
        "Name": f"{material} {element_type} {i}" 
    }
    
    ElementDataBase.append(element)

    
if __name__ == '__main__':
    
    ## 3.Printing Data Base
    print("Building Element Database:")
    print("--------------------------")
    for index, element in enumerate(ElementDataBase):
        print(f"Element {index + 1}: {element['Name']}")
        print(f"  ID: {element['ID']}")
        print(f"  Type: {element['Type']}")
        print(f"  Room: {element['Room']}")
        print(f"  Length: {element['Length']} m")
        print(f"  Height: {element['Height']} m")
        print(f"  Material: {element['Material']}\n")
    
    print(f"Total number of elements: {len(ElementDataBase)}\n")
    # Check that one of the data structures contains at least 5 different options or properties
    if len(materials) >= 5:
        print(f"The 'materials' data structure contains at least 5 different materials :) :")
        print(materials)
    else:
        print("The 'materials' data structure contains less than 5 different materials :c")

    
    
    search_index = 4
    specific_element = ElementDataBase[search_index]
    print(f"\nThe length of the element at position {search_index + 1} "
          f"('{specific_element['Name']}') is {specific_element['Length']} meters.")

    # Sort by lenghts 
    sorted_elements = sorted(ElementDataBase, key=lambda x: x['Length'], reverse=True)
    #Find three the longest => or sorted_elements[:3] 
    for i in range(3):
        print(f'{i +1} longest element (by Length) is {sorted_elements[i]}')