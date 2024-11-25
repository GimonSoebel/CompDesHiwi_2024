import random

building_elements = {}

# Creating an example data base / dictionary
for i in range(4):
    # Creating a unique key for each element
    keys = f"AbbC.{1000 + len(building_elements) + 1}"
    types = random.choice(["wall", "window", "door", "beam", "slab", "column"])
    rooms = random.choice(["bedroom", "toilet", "dining room", "living room", "attic", "kitchen"])
    lengths = round(random.uniform(1, 6), 2)
    widths = round(random.uniform(1, 3), 2)
    thickness = round(random.uniform(0.1, 0.7), 2) 
    values = {'type': types, 'room': rooms, 'length': lengths, 'width': widths, 'thickness': thickness}
    building_elements[keys] = values

# Displaying the example dictionary
print("Initial building_elements dictionary:")
for keys, values in building_elements.items():
    print(f"{keys}: {values}")

# Function to allow the user to add new elements
def added_elements():
    new_key = f"AbbC.{1000 + len(building_elements) + 1}"
    # User input for the new element's details
    types2 = input("Enter the type of the building element (e.g., 'wall', 'window', 'door'): ")
    rooms2 = input("Enter the room name assigned to the element (e.g., 'living room'): ")
    lengths2 = float(input("Enter the length of the element in meters: "))
    widths2 = float(input("Enter the width of the element in meters: "))
    thickness2 = float(input("Enter the thickness of the element in meters: "))   
    # Add the new element to the dictionary with the new unique key
    building_elements[new_key] = {
        "type": types2,
        "room": rooms2,
        "length": lengths2,
        "width": widths2,
        "thickness": thickness2
    }
    print(f"Element '{new_key}' added successfully!")

#3.1 Calculating Area
def calculate_area():
 
    input_key_area = input("Enter the key of the building elements you want to know the area of (e.g., AbbC.1001): ")
    element = building_elements[input_key_area]
    length = element["length"]
    width = element["width"]
    area = length * width
    print(f"Area of element '{input_key_area}': {area} m²")

#3.2 Calculating Volume
def calculate_volume():
    input_key_volume = input("Enter the key of the building elements you want to know the volume of (e.g., AbbC.1001): ")
    element = building_elements[input_key_volume] 
    length = element["length"]
    width = element["width"]
    thickness = element["thickness"]
    volume = length * width * thickness
    print(f"Volume of element '{input_key_volume}': {volume} m³")

def get_elements_by_type():
    type_name = input("Enter the type of the building elements you are looking for (e.g., 'wall', 'window', 'door'): ")
    matching_keys = [key for key, value in building_elements.items() if value["type"] == type_name]
    print(f"Elements of type '{type_name}': {matching_keys}")


# Calling the add_element function to allow user input for a new element
added_elements()

# Display the updated building_elements dictionary
print("\nUpdated building_elements dictionary:")
for keys, values in building_elements.items():
    print(f"{keys}: {values}")

#Calling the calculate_area function to allow user input to calculate area of a single object
calculate_area()

#Calling the calculate_volume function to allow user input to calculate volume of a single object
calculate_volume()

#Calling the get_elements_by_type function to allow user input get the keys of objects with the type, inputed by user
get_elements_by_type()

