import random

building_elements = {}

#generate a unique identifier for each building element
def generate_unique_id():
    return "Element_" + str(random.randint(1000, 9999))


#add a new building element
def add_element():
    element_type = input("Enter the type of the building element ( wall, window, door, ...?): ").lower()
    room_name = input("Enter the room name where the element is located (living room, kitchen, bedroom, ...?): ").lower()

    #Asking for dimensions with basic error checking
    try:
        length = float(input("Enter the length of the element in meters: "))
        height = float(input("Enter the height of the element in meters: "))
        width = float(input("Enter the width of the element in meters: "))
        if length <= 0 or height <= 0 or width <= 0:
            print("Please enter positive values for dimensions.")
            return
    except ValueError:  #help of chatgpt
        print("Invalid input. Please enter numeric values for dimensions.")
        return

    #unique ID to store the element in the dictionary
    element_id = generate_unique_id()
    building_elements[element_id] = {
        "type": element_type,
        "room": room_name,
        "length": length,
        "height": height,
        "width": width
    }

    print("Building element added successfully!\n")


#area and volume of all elements
def show_element_details():
    if not building_elements:
        print("No building elements available.\n")
        return

    for element_id, element in building_elements.items():
        area = element["length"] * element["height"]
        volume = element["length"] * element["height"] * element["width"]
        print("Element ID: " + element_id + ", Type: " + element["type"] + ", Area: " + str(area) + " m², Volume: " + str(volume) + " m³")

#finding elements by type
def find_elements_by_type():
    type_to_find = input("Enter the type of building element you want to search for (e.g., wall, window): ").lower()
    found_elements = []

    for element_id, element in building_elements.items():
        if element["type"] == type_to_find:
            found_elements.append(element_id)

    if found_elements:
        print("Found the following elements of type '" + type_to_find + "': " + ", ".join(found_elements) + "\n")
    else:
        print("No elements found of type '" + type_to_find + "'.\n")

#Final Step

print("Welcome to the Building Elements Manager!")
while True:
    add_element()
    show_element_details()
    find_elements_by_type()

    continue_adding = input("Would you like to add elements? Type 'yes' to continue or 'no' to exit: ").lower()
    if continue_adding != "yes":
        print("Exiting the program.")
        print("Final list of building elements:")
        print(building_elements)
        break