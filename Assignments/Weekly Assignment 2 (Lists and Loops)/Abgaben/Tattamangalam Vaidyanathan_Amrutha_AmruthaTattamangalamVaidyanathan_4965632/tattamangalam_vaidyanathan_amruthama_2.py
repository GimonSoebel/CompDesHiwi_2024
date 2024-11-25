import random

# 1. Define Database Fields Using Data Structures
# Available materials (Set)
materials = {"Graphene", "Concrete", "Glass", "Engineered Wood", "Recycled Plastics", "Steel", "Brick", "Aluminium", "Copper", "Plaster", "Ceramic", "Fiber Cement", "PVC", "Stone", "Marble", "Terrazzo", 
             "Bamboo", "Cork", "Rubber", "Vinyl","Hemp","Straw", "Clay", "Adobe", "Mud", "Grass", "Thatch", "Slate", "Asphalt", "Tar", "Bitumen", "Felt","Polyurethane", "Polystyrene", "Fiberglass",
             "Acrylic","Nylon","Cotton","Jute","Leather","Paper","Cardboard","Coconut","Birch","Maple","Oak","Mahogany","Teak","Cherry","Walnut","Beech","Ash","Poplar","Cedar","Spruce","Pine","Fir","Larch"}

# Building element types (List)
element_types = ["Wall", "Window", "Door", "Column", "Beam", "Slab", "Roof", "Stair", "Railing", "Furniture","Facade","Ceiling", "Floor", "Foundation", "Partition", "Balustrade", "Louver", "Skylight", "Canopy", 
                 "Pergola", "Trellis", "Fence", "Gate", "Pavilion", "Kiosk", "Shade", "Awning", "Deck", "Patio", "Porch", "Veranda", "Terrace", "Balcony", "Loggia", "Arcade", "Corridor", "Gallery", "Atrium"]

# Rooms (Tuple)
rooms = ("Living Room", "Kitchen", "Bathroom", "Bedroom", "Staircase", "Balcony", "Office", "Hallway", "Storage Room", "Garage", "Terrace", "Garden", "Patio", "Attic", "Basement", "Roof", "Facade", "Corridor",
         "Lobby", "Elevator", "Toilet", "Dining Room", "Library", "Studio", "Workshop", "Laundry Room", "Closet", "Pantry", "Guest Room", "Children's Room", "Home Office", "Home Cinema", "Gym", "Spa", "Sauna", 
         "Pool","Bar", "Restaurant", "Cafe", "Shop", "Showroom", "Gallery", "Museum", "Theater", "Auditorium", "Concert Hall", "Cinema", "Library", "School", "Kindergarten", "University", "Hospital", "Clinic")

# Possible lengths for elements (List populated using list comprehension)
lengths = [round(random.uniform(0.5, 5.0), 2) for _ in range(20)]

# Heights (List populated using list comprehension)
heights = [round(random.uniform(2.0, 4.0), 2) for _ in range(20)]

# IDs (List generated with a loop to ensure unique IDs)
element_ids = [f"Element-{i+1}" for i in range(20)]

# Display that materials contain at least 5 options
if len(materials) >= 5:
    print(f"\n \n The 'materials' set contains {len(materials)} different options.\n")

# 2. Fill the Database with Nested Tuples in a List
# Initialize an empty list for the database
element_database = []

# Populate the list with 20 elements
for i in range(20):
    element_id = f"Element-{i+1}"
    element_type = random.choice(element_types)
    room = random.choice(rooms)
    length = lengths[i]  # Use a value from the lengths list
    height = heights[i]  # Use a value from the heights list
    material = random.choice(list(materials))
    
    # Append element as a tuple to the database list
    element_database.append((element_id, element_type, room, length, height, material))

# 3. Print the Database
# Print all elements in a readable format
print("Building Elements Database:")
for element in element_database:
    print(f"\n ID: {element[0]}: \n \t Type: {element[1]} \n \t Room: {element[2]} \n \t Length: {element[3]} m \n\t Height: {element[4]} m \n\t Material: {element[5]} " )

# Print the total number of elements
print(f"\nTotal number of elements: {len(element_database)}")

# Printing one specific property of one specific element
# Prompt the user to enter an index for the element they want to know about
# Loop until the user enters a valid index
while True:
    # Prompt the user to enter an index for the element they want to know about
    index = int(input(f"\nEnter the index # whose type of building element you would like to know (between 1 & {len(element_database)}): "))

    # Check if the input index is within the valid range
    if 1 <= index <= len(element_database):
        # Access the type of the building element at the specified index (adjusted for 0-based indexing)
        element = element_database[index - 1]
        
        # Display the details of the specified element
        print(f"\nDetails of the building element at index {index}:")
        print(f"  ID: {element[0]}")
        print(f"  Type: {element[1]}")
        print(f"  Room: {element[2]}")
        print(f"  Length: {element[3]} m")
        print(f"  Height: {element[4]} m")
        print(f"  Material: {element[5]}")
        break  # Exit the loop since the input is valid
    else:
        # Inform the user of an invalid input and prompt them to re-enter
        print(f"Invalid index. Please enter a number between 1 and {len(element_database)}.")
        
# Printing the 3 longest elements
# Sort elements by length in descending order and get the top 3
sorted_elements = sorted(element_database, key=lambda x: x[3], reverse=True)[:3]
print("\nThe 3 longest elements are:")
for element in sorted_elements:
    print(f"ID: {element[0]}, \n \t Length: {element[3]} m")