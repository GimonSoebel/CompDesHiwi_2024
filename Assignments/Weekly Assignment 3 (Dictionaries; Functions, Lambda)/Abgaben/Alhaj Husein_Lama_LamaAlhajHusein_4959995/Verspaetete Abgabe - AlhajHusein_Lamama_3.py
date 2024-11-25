# Creating Building Elements Dictionary
building_elements = {}

# Function to add elements to Building Elements Dictionary.
def add_building_element(key, element_type, room, length, height, thickness):
    building_elements[key] = {
        "type": element_type,
        "room": room,
        "length (m)": length,
        "height (m)": height,
        "thickness (m)": thickness
    }

# Function to calculate the area of the building element in square meters.
def calculate_area_element(key):
    if key in building_elements:
        input = building_elements[key]
        return input["length (m)"] * input["height (m)"]
    return "Element not found."

# Function to calculate the volume of the building element in cubic meters.
def calculate_volume_element(key):
     if key in building_elements:
        input = building_elements[key]
        return input["length (m)"] * input["height (m)"] * input ["thickness (m)"]
     return "Element not found."

# Function to get elements by type
def get_elements_by_type(element_type):
    return [key for key, element in building_elements.items() if element['type'] == element_type]

# Forming the User Interface System
while True:
    print("\n1. Add the building element")
    print("2. Calculate area of the element")
    print("3. Calculate volume of the element")
    print("4. Get elements by type")
    print("5. Exit and list Building Element Dictionary")

    choice = input("Choose an option: ")

    if choice == '1':
        key = input("Enter the element key: ")
        element_type = input("Enter the type of the element (external wall, internal wall, window, door): ")
        room = input("Enter the name of the room that contains the element: ")
        length = float(input("Enter the length of the element in meters: "))
        height = float(input("Enter the height of the element in meters: "))
        thickness = float(input("Enter the thickness of the element in meters: "))
        add_building_element(key, element_type, room, length, height, thickness)
        print("\nElement has been added successfully.")
    
    elif choice == '2':
        key = input("Enter the element ID for area calculation: ")
        area = calculate_area_element(key)
        print("The area of the element is ", area, " square meters")

    elif choice == '3':
        key = input("Enter the element ID for volume calculation: ")
        volume = calculate_volume_element(key)
        print("The volume of the element is :", volume, " cubic meters")

    elif choice == '4':
        element_type = input("Enter the Type of element you want to get (external wall, internal wall, window, door): ")
        elements = get_elements_by_type(element_type)
        print("Elements of type", element_type, ":", elements)

    elif choice == '5':
        print("Exiting, The Created Building Element Dictionary is ")
        print (building_elements)
        break

    else:
        print("Invalid choice. Try again.")
 