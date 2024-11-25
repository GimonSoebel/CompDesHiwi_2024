#List of building element types
element_types = ["External Wall", "Window", "Door", "Ceiling"] 

#Set of rooms
rooms = {"living room", "bedroom", "bathroom", "kitchen"}  

#Tuple of materials
materials = ("Concrete", "Wood", "Glass", "Gypsumboard", "Cermaic tiles")

#List of IDs
element_ids = [f"EID{i+1}" for i in range(10)]

#List of Element Length in meters
length = [1.0, 1.5, 2.0, 3.0]

#List of Element Height in meters
height = [1.0, 1.5, 2.0, 3.0]

#List of Building Element Database using Sets
Database_of_Building_Elements = [
    (element_ids[0], element_types[0], "living room", length[3], height[2], materials[0]),
    (element_ids[1], element_types[1], "bedroom", length[0], height[1], materials[2]),
    (element_ids[2], element_types[2], "kitchen", length[0], height[2], materials[1]),
    (element_ids[3], element_types[3], "bathroom", length[1], height[3], materials[3])
    ]

element_types.append("Internal wall")
element_types.extend(["wall finishing", "roof"])
rooms.add("store")

#Add the new elements
Database_of_Building_Elements.append((element_ids[4], element_types[4], "living Room", length[2], height[2], materials[3])) 
Database_of_Building_Elements.append((element_ids[5], element_types[5], "Bathroom", length[1], height[3], materials[4]))
Database_of_Building_Elements.append((element_ids[6], element_types[6], "roof", length[3], height[3], materials[1]))
Database_of_Building_Elements.append((element_ids[7], element_types[4], "kitchen", length[0], height[1], materials[4]))
Database_of_Building_Elements.append((element_ids[8], element_types[1], "bedroom", length[1], height[1], materials[2]))
Database_of_Building_Elements.append((element_ids[9], element_types[3], "store", length[0], height[2], materials[1]))

#Get the number of elements in a tuple
num_Database_of_Building_Elements = len(Database_of_Building_Elements)

#Table of Building Element Database:
print("Building Element Database:")
print(f"{'Element Id':<12} {'Element Type':<18} {'Room Function':<15} {'Element Length(m)':<18} {'Element Height(m)':<18} {'Material used':<15}")
print("-" * 90)
#Insert each row of elements in the Table:
for element in Database_of_Building_Elements:
    print(f"{element[0]:<12} {element[1]:<18} {element[2]:<15} {element[3]:<18} {element[4]:<18} {element[5]:<15}")

#Print Number of Elements in the Building Database:
print ("\nNumber of Elements in the Building Database is: " + format(num_Database_of_Building_Elements) + " elements.")

#Check if one of the data structures has at least 5 different options:
if len(element_types) >= 5:
    print("\nThe 'Material' set contains at least 5 different options:", materials)

#Print a specific property of a specific element and its location
window_index = element_types.index("Window")
print(f"\nIn the element {Database_of_Building_Elements[1]}', the element type '{Database_of_Building_Elements[window_index][1]}' is located at the {window_index+1} position within the element in the Building Database list.\n") 
