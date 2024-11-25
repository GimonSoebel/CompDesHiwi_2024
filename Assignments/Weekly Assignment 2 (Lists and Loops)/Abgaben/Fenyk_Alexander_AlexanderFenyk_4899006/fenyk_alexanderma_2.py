import random


## 1. Hardcoded Data Structure using 4 different data types

# 1. List
rooms = ["living room", "kitchen", "bedroom", "bathroom", "hallway", "office", "storage room", "garage", "attic",
         "basement"]

# 2. Tuple
materials = ("Graphene", "Concrete", "Glass", "Wood", "Recycled Plastics")

# 3. Set
ids = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# 4. Dictionary
id_length = {1: 3.25, 2: 1.10, 3: 2.85, 4: 4.45, 5: 5.68, 6: 6.4, 7: 7.1, 8: 8, 9: 9.2, 10: 10.93}

ids = set()
# Optional, fill the set with ids
for i in range(1, 11):
    ids.add(i)
#print(ids)



## 2. Data base filling using Nested tuples into a List

database = [] # creation of database list
ids_converted = list(ids) #converting the set to a tuple

# different variants to add tuples (with their index) into a list 
database.append((ids_converted[0], rooms[0], materials[0], id_length.get(ids_converted[0])))
database.append((ids_converted[1], rooms[1], materials[1], id_length.get(ids_converted[1])))
database.append((ids_converted[2], rooms[2], materials[2], id_length.get(ids_converted[2])))

database.extend([(ids_converted[3], rooms[3], materials[3], id_length.get(ids_converted[3])),
                 (ids_converted[4], rooms[4], materials[4], id_length.get(ids_converted[4])),
                 (ids_converted[5], rooms[5], materials[0], id_length.get(ids_converted[5])),
                 (ids_converted[6], rooms[6], materials[1], id_length.get(ids_converted[6]))])

database[7:11] = [(ids_converted[7], rooms[7], materials[2], id_length.get(ids_converted[7])), 
                  (ids_converted[8], rooms[8], materials[3], id_length.get(ids_converted[8])),
                  (ids_converted[9], rooms[9], materials[4], id_length.get(ids_converted[9]))]

#print(database)

database.clear() # clears the list because of the optional challenge

# Optional challenge
for _ in range(10):
    id = random.randint(1, 10)
    database.append((id, random.choice(rooms), random.choice(materials), id_length[id]))

#print(database)

## 3.Printing Data Base

#Printing the Data Base
print("Database:")
for element in database:
    print(f"Id: {str(element[0])} Room: {element[1]} Material: {element[2]} Length: {str(element[3])}")

#Length of Database
print(f"Amount of elements: {len(database)}")

#Check for more than 5 different options
if len(rooms) >= 5:
    print("Rooms contains at least 5 different options or properties.")
else: 
    print ("Rooms contains less than 5 different options or properties.") #almost never the case as I defined more than 5 options for the rooms
    

# searching for a specific id in the database
wanted_id = int(input("Enter the id of the element you want to print from 1 to 10: "))
for element in database:
    if element[0] == wanted_id:
        print(f"Element with index {wanted_id} has the following properties:")
        print(f"Room: {element[1]}, Material: {element[2]}, Length: {element[3]}")
        break


# searching the property for a specific index
element_index = 5
specific_property= database[element_index][1]
print(f"Specific property of element with index {element_index} is {specific_property}")

# Optional challenge
# Print the 3 longest elements
sorted_database = sorted(database, key=lambda x: x[3], reverse=True) #Sorted for the length in reverse
print("The 3 longest elements based on length are:")
print(sorted_database)
for i, entry in enumerate(sorted_database[0:3]):
    print(f"{i}: {entry}")

