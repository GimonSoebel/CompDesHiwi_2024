# Initialize the building_elements dictionary
building_elements = {}

# Function to add a new building element
def add_element(key, element_type, room, length, height, thickness):
    """
    Adds a new building element to the building_elements dictionary.
    """
    building_elements[key] = {
        "type": element_type,
        "room": room,
        "length": length,
        "height": height,
        "thickness": thickness
    }

# Adding sample elements
sample_elements = [
    ("InW.01.23", "wall", "living room", 4.0, 2.5, 0.3),
    ("Win.02.05", "window", "bedroom", 1.5, 1.2, 0.1),
    ("Dr.03.01", "door", "hallway", 0.9, 2.0, 0.1),
    ("Fl.04.12", "floor", "kitchen", 3.0, 0.1, 0.3),
    ("Dado.05.09", "dado", "bathroom", 2.0, 0.9, 0.05)
]

for key, element_type, room, length, height, thickness in sample_elements:
    add_element(key, element_type, room, length, height, thickness)

# Define a function to display all sample elements
def display_sample_elements():
    print("Sample Building Elements:")
    for key, details in building_elements.items():
        print(f"ID: {key}, Type: {details['type']}, Room: {details['room']}, "
              f"Length: {details['length']} m, Height: {details['height']} m, Thickness: {details['thickness']} m")

# Define calculate_area and calculate_volume functions
def calculate_area(key):
    if key in building_elements:
        element = building_elements[key]
        return element["length"] * element["height"]
    else:
        print(f"Element '{key}' not found in the database.")
        return None

def calculate_volume(key):
    if key in building_elements:
        element = building_elements[key]
        return element["length"] * element["height"] * element["thickness"]
    else:
        print(f"Element '{key}' not found in the database.")
        return None

# Define get_elements_by_type function
def get_elements_by_type(element_type):
    return [key for key, element in building_elements.items() if element["type"] == element_type]

# Main Program Loop
while True:
    print("\nBuilding Information Modeling (BIM) Tool")
    print("1. Display sample elements")
    print("2. Add a new building element")
    print("3. Calculate area of a building element")
    print("4. Calculate volume of a building element")
    print("5. Get elements by type")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        # Display sample elements
        display_sample_elements()
        
    elif choice == '2':
        # Collect data from the user to add a new element
        key = input("Enter the unique key for the element (e.g., InW.01.23): ")
        element_type = input("Enter the type of the building element (e.g., wall, window, door): ")
        room = input("Enter the room name the element is assigned to (e.g., living room, kitchen): ")
        length = float(input("Enter the length of the element in meters: "))
        height = float(input("Enter the height of the element in meters: "))
        thickness = float(input("Enter the thickness of the element in meters: "))
        add_element(key, element_type, room, length, height, thickness)
        print(f"Added element '{key}' of type '{element_type}' to the dictionary.")
        
    elif choice == '3':
        key = input("Enter the unique key of the element to calculate area: ")
        area = calculate_area(key)
        if area is not None:
            print(f"Area of element '{key}': {area} m²")
            
    elif choice == '4':
        key = input("Enter the unique key of the element to calculate volume: ")
        volume = calculate_volume(key)
        if volume is not None:
            print(f"Volume of element '{key}': {volume} m³")
            
    elif choice == '5':
        element_type = input("Enter the type of building element to retrieve (e.g., wall, window): ")
        elements = get_elements_by_type(element_type)
        print(f"Keys of all '{element_type}' elements: {elements}")
        
    elif choice == '6':
        print("Exiting the program.")
        break
        
    else:
        print("Invalid choice. Please select an option from 1 to 6.")
