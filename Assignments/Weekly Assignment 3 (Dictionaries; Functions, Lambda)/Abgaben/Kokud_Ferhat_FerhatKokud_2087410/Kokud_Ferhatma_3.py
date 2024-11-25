import random

# Dictionary to store building elements
building_elements = {}

# Helper function to check if a value is provided or add a new one
def get_input_with_check(prompt, existing_value=None):
    if existing_value:
        use_existing = input(f"{prompt} (existing: '{existing_value}')? Press Enter to use existing or provide new: ")
        return existing_value if not use_existing else use_existing
    else:
        return input(prompt)

def get_float_input_with_check(prompt, existing_value=None):
    if existing_value:
        use_existing = input(f"{prompt} (existing: '{existing_value}')? Press Enter to use existing or provide new: ")
        return float(existing_value) if not use_existing else float(use_existing)
    else:
        return float(input(prompt))

# Function to manually add or update a building element with checks
def add_element_manually(bimDict):
    user_input_key = input("Enter key (e.g., 'AbbC.1001'): ")
    
    if user_input_key in bimDict:
        print(f"Key '{user_input_key}' already exists. Modifying existing entry.")
        existing_element = bimDict[user_input_key]
    else:
        existing_element = {}
        
    user_input_type = get_input_with_check("Enter type (e.g., 'wall', 'window', 'door')", existing_element.get("type"))
    user_input_room = get_input_with_check("Enter room name (e.g., 'living room')", existing_element.get("room"))
    user_input_length = get_float_input_with_check("Enter length in meters", existing_element.get("length"))
    user_input_height = get_float_input_with_check("Enter height in meters", existing_element.get("height"))
    user_input_thickness = get_float_input_with_check("Enter thickness in meters", existing_element.get("thickness"))

    single_element = {
        "type": user_input_type,
        "room": user_input_room,
        "length": user_input_length,
        "height": user_input_height,
        "thickness": user_input_thickness
    }
    bimDict[user_input_key] = single_element
    print(f"Element '{user_input_key}' added/updated successfully!")

# Function to add a building element with random values (for testing purposes)
def add_element_randomly(bimDict):
    user_input_key = input("Enter key (e.g., 'AbbC.1001'): ")
    single_element = {
        "type": random.choice(["wall", "window", "door", "beam", "slab", "column"]),
        "room": random.choice(["living room", "staircase", "kitchen", "bedroom", "attic"]),
        "length": round(random.uniform(1, 6), 2),
        "height": round(random.uniform(1, 3), 2),
        "thickness": round(random.uniform(0.1, 0.7), 2)
    }
    bimDict[user_input_key] = single_element
    print(f"Random element '{user_input_key}' added successfully!")

# Function to edit an existing element
def edit_element(bimDict):
    user_input_key = input("Enter key of the element to edit (e.g., 'AbbC.1001'): ")
    if user_input_key in bimDict:
        add_element_manually(bimDict)  # Reuse the add_element_manually function for editing
    else:
        print(f"Element with key '{user_input_key}' not found.")

# Function to view all elements
def view_all_elements(bimDict):
    if bimDict:
        print("\nAll building elements:")
        for key, element in bimDict.items():
            print(f"{key}: {element}")
    else:
        print("No elements to display.")

# Function to calculate area of a building element
def calculate_area(bimDict):
    user_input_key = input("Enter key of the element to calculate area (e.g., 'AbbC.1001'): ")
    if user_input_key in bimDict:
        element = bimDict[user_input_key]
        area = round(element["length"] * element["height"], 2)
        print(f"Area of element '{user_input_key}': {area} m²")
    else:
        print(f"Element with key '{user_input_key}' not found.")

# Function to calculate volume of a building element
def calculate_volume(bimDict):
    user_input_key = input("Enter key of the element to calculate volume (e.g., 'AbbC.1001'): ")
    if user_input_key in bimDict:
        element = bimDict[user_input_key]
        volume = round(element["length"] * element["height"] * element["thickness"], 2)
        print(f"Volume of element '{user_input_key}': {volume} m³")
    else:
        print(f"Element with key '{user_input_key}' not found.")

# Function to retrieve all elements of a specified type
def get_elements_by_type(bimDict):
    user_input_type = input("Enter the type of elements to retrieve (e.g., 'wall', 'window'): ")
    matching_keys = [key for key, value in bimDict.items() if value["type"] == user_input_type]
    if matching_keys:
        print(f"Elements of type '{user_input_type}': {matching_keys}")
    else:
        print(f"No elements of type '{user_input_type}' found.")

# Function to retrieve all elements of a specified room
def get_elements_by_room(bimDict):
    user_input_room = input("Enter the room name to retrieve elements (e.g., 'living room'): ")
    matching_keys = [key for key, value in bimDict.items() if value["room"] == user_input_room]
    if matching_keys:
        print(f"Elements in room '{user_input_room}': {matching_keys}")
    else:
        print(f"No elements in room '{user_input_room}' found.")

# Function to sort elements by a specified attribute
def sort_elements(bimDict):
    print("Sort building elements by one of the following attributes:")
    print("1. Type")
    print("2. Room")
    print("3. Length")
    print("4. Height")
    print("5. Thickness")
    
    choice = input("Enter the number corresponding to the attribute you'd like to sort by: ")
    attribute_map = {
        "1": "type",
        "2": "room",
        "3": "length",
        "4": "height",
        "5": "thickness"
    }
    
    attribute = attribute_map.get(choice)
    if attribute:
        sorted_elements = sorted(bimDict.items(), key=lambda item: item[1][attribute])
        print(f"\nBuilding elements sorted by '{attribute}':")
        for key, value in sorted_elements:
            print(f"{key}: {value}")
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")

# Function to show database summary
def show_database_summary(bimDict):
    print("\nDatabase Summary:")
    print(f"Total elements: {len(bimDict)}")
    type_count = {}
    for element in bimDict.values():
        type_count[element["type"]] = type_count.get(element["type"], 0) + 1
    for element_type, count in type_count.items():
        print(f"Type '{element_type}': {count} elements")

# Main function to handle user choices
def main_menu():
    while True:
        user_input_selection = input(
            """
            Choose an option:
            1 to View all elements
            2 to Add element manually
            3 to Add element randomly
            4 to Edit an existing element
            5 to Calculate area of an element
            6 to Calculate volume of an element
            7 to Get elements by type
            8 to Get elements by room
            9 to Sort elements by an attribute
            10 to Show database summary\nEnter your choice: """
        )
        
        if user_input_selection == "1":
            view_all_elements(building_elements)
        elif user_input_selection == "2":
            add_element_manually(building_elements)
        elif user_input_selection == "3":
            add_element_randomly(building_elements)
        elif user_input_selection == "4":
            edit_element(building_elements)
        elif user_input_selection == "5":
            calculate_area(building_elements)
        elif user_input_selection == "6":
            calculate_volume(building_elements)
        elif user_input_selection == "7":
            get_elements_by_type(building_elements)
        elif user_input_selection == "8":
            get_elements_by_room(building_elements)
        elif user_input_selection == "9":
            sort_elements(building_elements)
        elif user_input_selection == "10":
            show_database_summary(building_elements)
        else:
            print("Invalid choice. Please enter a number from 1 to 10.")

# Start the program
main_menu()
