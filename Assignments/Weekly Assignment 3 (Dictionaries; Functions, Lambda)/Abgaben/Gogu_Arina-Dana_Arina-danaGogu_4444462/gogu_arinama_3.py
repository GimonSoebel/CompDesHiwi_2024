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
The above two functions should take a key as a parameter and use the information from the building_elements dictionary to perform the calculations. ??

4. Create a function called get_elements_by_type that takes a type (e.g., "wall," "window," "door") as a parameter and
returns a list of keys for all building elements of that specific type.
"""

# Task 1
# Initialize an empty dictionary to store building elements
building_elements = {}

# Task 2
# user interface
def add_element():
   
    key = input("Under which name do you want to save the element?: (e.g., Element 1): ")
    type = input("Which type of building element it is?: (e.g., 'wall', 'window', 'door'): ")
    room = input("To which room do you want to assign the element? (e.g., 'living room', 'staircase'): ")

    length = float(input("What length does it has?:"))
    height = float(input("How high is it?: "))
    thickness = float(input("How thick is it?: "))
    
    # Store the element in the dictionary
    building_elements[key] = {
        'type': type,
        'room': room,
        'length': length,
        'height': height,
        'thickness': thickness
    }
    print(f"Element '{key}' has been added to the library!")
    print(f"Your new library:")
    print(building_elements) #overview

# Task 3

def calculate_area(): # Function for Area
    key = input("Element name:")
    if key in building_elements:
        element = building_elements[key]
        area = element['length'] * element['height']
        print(f"Area of element '{key}': {area} m²")
    else:
        print("This element couldn't be found in the dictionary.")

def calculate_volume(): # Function for Volume

    key = input("Element name:")
    if key in building_elements:
        element = building_elements[key]
        volume = element['length'] * element['height'] * element['thickness']
        print(f"Volume of element '{key}': {volume} m³")
    else:
        print("This element couldn't be found in the dictionary.")

# Task 4
def get_elements_by_type(): #check dictionary inputs
    element_type = input("Building element (e.g., 'wall', 'window', 'door') to filter by: ")
    elements_by_type = [key for key, element in building_elements.items() if element['type'] == element_type]
    if elements_by_type:
        print(f"Elements of type '{element_type}': {elements_by_type}")
    else:
        print(f"No elements of type '{element_type}' found.")

# To make it more interactive - I create an user interface
def main():

    while True:
        print("\n""Building Information Modeling (BIM) Tool")
        print("1. Check current dictionary")
        print("2. Add a new building element")
        print("3. Calculate area of an element")
        print("4. Calculate volume of an element")
        print("5. Get elements by type")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == "1":
            print(building_elements)
        elif choice == "2":
            add_element()
        elif choice == "3":
            calculate_area()
        elif choice == "4":
            calculate_volume()
        elif choice == "5":
            get_elements_by_type()
        elif choice == "6":
            print("Exiting the BIM tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please insert a number from 1 to 6.")
main()