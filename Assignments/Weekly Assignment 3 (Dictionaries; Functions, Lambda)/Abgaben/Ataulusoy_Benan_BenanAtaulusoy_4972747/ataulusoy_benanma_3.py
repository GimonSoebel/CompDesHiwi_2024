"""
Assignment 3: Building Information Modeling (BIM) Tool

Imagine you are developing a Building Information Modeling (BIM) Tool that stores information about different building elements.
Your task is to create a Python program that interacts with the user to collect and analyse data using dictionaries, built-in functions, UDFs or lambda. 
The program should perform the following tasks:

1.  Create a dictionary called building_elements that will store information about various building elements.
Each element should be identified by a unique key (e.g., a string or integer).
The value associated with each key should be another dictionary containing the following information: type, room, length, height, thickness.

key: The unique key for the element. (e.g. InW.01.23)
type: The type of the building element. (e.g., "wall," "window," "door," etc.).
room: The name of the room assigned to the building element. (e.g. "living room", "staircase" etc. )
length: The length of the element in meters.
height: The height of the element in meters.
thickness: The width of the element in meters.

2. Create a function called add_element that allows users to add a new building element to the building_elements dictionary.
This function should contained the previous contained parameters:

3. Create a function called calculate_area that calculates and returns the area of a building element in m2.
Create a function called calculate_volume that calculates and returns the volume of a building element in m3.
The above two functions should take a key as a parameter and use the information from the building_elements dictionary to perform the calculations.

4. Create a function called get_elements_by_type that takes a type (e.g., "wall," "window," "door") as a parameter and
returns a list of keys for all building elements of that specific type.
"""
#Dictionary
building_elements = {
    "InW.01.23": {"type": "wall", "room": "living room", "length": 6.0, "height": 3.0, "thickness": 0.3}, 
    "InW.01.24": {"type": "window", "room": "bedroom", "length": 1.5, "height": 1.7, "thickness": 0.2}, 
    "InW.01.25": {"type": "door", "room": "kitchen", "length": 1.8, "height": 2.4, "thickness": 0.1} }
#Add elements
def add_element(key, type, room, length, height, thickness):

    if key in building_elements:
        print(f"Key '{key}' already exists.")
    else:
     
        building_elements[key] = {
            "type": type,
            "room": room,
            "length": length,
            "height": height,
            "thickness": thickness
        }
        print(f"Added new element with key: {key}")

#area

def calculate_area(key):
    if key in building_elements:
        element = building_elements[key]
        length = element["length"]
        height = element["height"]
        area = length * height
        return area
    else:
        print("Key is not found.")
        return None

 #volume

def calculate_volume(key):
    if key in building_elements:
        element = building_elements[key]
        length = element["length"]
        height = element["height"]
        thickness = element["thickness"]
        volume = length * height * thickness
        return volume
    else:
        print("Key is not found.")
        return None
    
#Show elements
def show_elements():
    if not building_elements:
        print("No elements to display.")
    else:
        print("\nBuilding Elements:")
        for key, attributes in building_elements.items():
            print(f"\nKey: {key}")
            for attr, value in attributes.items():
                print(f"  {attr.capitalize()}: {value}")

# Get elements by type (wall, window, door, etc.)
def get_elements_by_type(element_type):
    matching_keys = [key for key, attributes in building_elements.items() if attributes["type"] == element_type]
    return matching_keys


running = True
while running:
    print("Please choose the operation you want:")
    print("1. Add a new element")
    print("2. Calculate the area and volume of an element")
    print("3. Show existing building elements")
    print("4. Get elements by type")
    print("5. Exit")

    choice = input("Enter your choice (1, 2, 3, 4 or 5): ")

    if choice == '1':
        key = input("Enter the key: ")
        type = input("Enter the type (wall, window, door, etc.): ")
        room = input("Enter the room (living room, bedroom, etc.): ")
        length = float(input("Enter the length (m): "))
        height = float(input("Enter the height (m): "))
        thickness = float(input("Enter the thickness (m): "))
        add_element(key, type, room, length, height, thickness)

    elif choice == '2':
        key = input("Enter the key of the element to calculate the area: ")
        area = calculate_area(key)
        if area is not None:
            print(f"Area of element {key}: {area} m²")

        key = input("Enter the key of the element to calculate the volume: ")
        volume = calculate_volume(key)
        if volume is not None:
            print(f"Volume of element {key}: {volume} m³")

    elif choice == '3':
        show_elements()  

    elif choice == '4': 
        element_type = input("Enter the type of elements to retrieve (wall, window, door, etc.): ") 
        elements_by_type = get_elements_by_type(element_type)  
        if elements_by_type:
            print(f"Elements of type '{element_type}': {elements_by_type}")
        else:
            print(f"No elements found of type '{element_type}'.")

    elif choice == '5':
        print("Exiting program.")
        running = False  # Exit the loop

    else:
        print("Invalid choice. Please enter 1, 2, 3, 4 or 5.")
         
