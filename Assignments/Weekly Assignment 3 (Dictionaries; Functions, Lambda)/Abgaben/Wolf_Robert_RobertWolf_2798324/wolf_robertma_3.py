####################################################################################
import random

# Fill in the attributes type, room, length, height, and thickness using random.choice and random rounded floats for one element
def fill_attributes_of_element():
    global possible_types, possible_rooms
    possible_types = ["wall", "window", "door", "roof"]
    possible_rooms = ["living room", "staircase", "kitchen", "bedroom", "bathroom"]
     
    filled_attributes = {
        "type": random.choice(possible_types),
        "room": random.choice(possible_rooms),
        "length": round(random.uniform(0, 15), 2),
        "height": round(random.uniform(0, 15), 2),
        "thickness": round(random.uniform(0, 1), 2)
    }
    return filled_attributes

# Generate dictionary, with "amount_elements" argument determining the number of building elements in Dict
def generate_building_elements(amount_elements):
    global building_elements #set the dict global so it can be acces from other functions
    building_elements = {}
    for i in range(amount_elements):
        key = f"Building Element {i + 1}"
        building_elements[key] = fill_attributes_of_element() #call the fill_attributes_of_element function

# Adds specific element to the dictionary
def add_element():
    key = f"Building Element {len(building_elements) + 1}"
    
    # Element type
    element_type = input("Type of Element: ")
    while element_type not in possible_types:
        user_answer = input("This type of element doesn't exist. Do you want to add it (Y for adding, any other key to retype)? ")
        if user_answer.lower() == "y":
            possible_types.append(element_type)
            break
        else:
            element_type = input("Type of Element: ")

    # Room of element
    room = input("Room of Element: ")
    while room not in possible_rooms:
        user_answer = input("This room doesn't exist. Do you want to add it (Y for adding, any other key to retype)? ")
        if user_answer.lower() == "y":
            possible_rooms.append(room)
            break
        else:
            room = input("Room of Element: ")

    # Element dimensions
    length = float_input("Length of Element: ")
    height = float_input("Height of Element: ")
    thickness = float_input("Thickness of Element: ")

    # Add the new element to building_elements
    building_elements[key] = {
        "type": element_type,
        "room": room,
        "length": length,
        "height": height,
        "thickness": thickness
    }
    return building_elements

# user_input into float, re-input until a valid float or int is entered
def float_input(user_input):
    while True:
        try:
            return round(float(input(user_input)), 3)
        except ValueError:
            print("Please enter a valid number.")

# user_input into int, re-input until a valid int is entered
def int_input(user_input):
    while True:
        try:
            return int(input(user_input))
        except ValueError:
            print("Please enter a valid number.")

#calculate Area of Element
def calculate_area(key_for_calc):
    elem_to_calc = building_elements[key_for_calc]
    print(f"Properties of {key_for_calc} {elem_to_calc}:")
    area = elem_to_calc["length"]*elem_to_calc["thickness"]
    print(f"Area of {key_for_calc}: {round(area,2)} m²")
    user_continuation=input("\n\n\nDo you want to Perform other Actions?\n\nPress Y for yes\nPress anything else to Quit\n\nconfirm with Enter key\n")
    if user_continuation == "Y" or user_continuation == "y":
        user_decision()
    else:
        pass

#calculate Volume of Element
def calculate_volume(key_for_calc):
    elem_to_calc = building_elements[key_for_calc]
    print(f"Properties of {key_for_calc} {elem_to_calc}:")
    volume = elem_to_calc["length"]*elem_to_calc["thickness"]*elem_to_calc["height"]
    print(f"Volume of {key_for_calc}: {round(volume,2)} m³")
    user_continuation=input("\n\n\nDo you want to Perform other Actions?\n\nPress Y for yes\nPress anything else to Quit\n\nconfirm with Enter key\n")
    if user_continuation == "Y" or user_continuation == "y":
        user_decision()
    else:
        pass

#get all elements of a certain type
def get_elements_by_type(type_of_elem):
    all_of_type = []
    all_keys_of_type = []
    for each_elem in building_elements:
        elem_properties = building_elements[each_elem]
        if elem_properties["type"]== type_of_elem:
            all_of_type.append(building_elements[each_elem])
            all_keys_of_type.append(each_elem)

    if len(all_of_type) == 0: #if there are no elements of that type found
        print(f"No Element found with the type {type_of_elem}, either there are none or there is a typo")
        user_decision() #let user decide again what to do


    print(f"{len(all_of_type)} Elements found with the type {type_of_elem}\n\nList of all Elements with this type:")
    combined_list = [f"({x}{y})" for x, y in zip(all_keys_of_type, all_of_type)]
    for i in combined_list:
        print(i)
    
    #do u want to continue
    user_continuation=input("\n\nDo you want to Perform other Actions?\n\nPress Y for yes\nPress anything else to Quit\n\nconfirm with Enter key\n")
    
    if user_continuation == "Y" or user_continuation == "y":
        user_decision()
    else:
        pass

#let user decide next action
def user_decision():
    decision = input("\n\nPress Y to add an Building Element \nPress A to calculate the Area of a specific Element\nPress V to calculate the Volume of a specific Element\nPress G to get all Elements of a type\nPress Q to Quit\n\nconfirm with Enter key\n")
    if decision == "Y" or decision == "y":
        add_element()
        print(f"Complete list of Building Elements{building_elements}")
        user_decision()#calling itself again for further decisions
    elif decision == "A" or decision == "a":
        key_of_element = f"Building Element {input("Number of Building Element to calculate the Area:")}"
        if key_of_element in building_elements:
            calculate_area(key_of_element)
        else:
            print("Enter Valid Number of Building Element")
            key_of_element = f"Building Element {input("Number of Building Element to calculate the Area:")}"
        #user_decision()#calling itself again for further decisions
    elif decision == "V" or decision == "v":
        key_of_element = f"Building Element {input("Number of Building Element to calculate the Volume:")}"
        if key_of_element in building_elements:
            calculate_volume(key_of_element)
        else:
            print("Enter Valid Number of Building Element")
            key_of_element = f"Building Element {input("Number of Building Element to calculate the Area:")}"
    elif decision == "G" or decision == "g":
        type_of_elem = input("Type of Building Elements to Show:  ")
        get_elements_by_type(type_of_elem)
        
    
    elif decision == "Q" or decision == "q":
        pass

    else:
        user_decision()

# Main function (main code/calling the functions)
def main():
    generate_building_elements(int_input("How many Building elements should be created?:"))
    print(building_elements)
    user_decision()
    


# running main (conventional calling of main useless in this case)
if __name__ == "__main__":
    main()





#################################
#Revised by ChatGPT for better readability and some code shortening:
"""
import random

# Fill in attributes for a building element with random choices and values
def fill_attributes_of_element():
    global possible_types, possible_rooms
    possible_types = ["wall", "window", "door", "roof"]
    possible_rooms = ["living room", "staircase", "kitchen", "bedroom", "bathroom"]
    
    return {
        "type": random.choice(possible_types),
        "room": random.choice(possible_rooms),
        "length": round(random.uniform(0, 15), 2),
        "height": round(random.uniform(0, 15), 2),
        "thickness": round(random.uniform(0, 1), 2)
    }

# Generate a dictionary of building elements with a specified number of entries
def generate_building_elements(amount_elements):
    global building_elements
    building_elements = {}
    for i in range(amount_elements):
        element_key = f"Building Element {i + 1}"
        building_elements[element_key] = fill_attributes_of_element()

# Add a specific element to the building_elements dictionary
def add_element():
    element_key = f"Building Element {len(building_elements) + 1}"
    
    # Get element type with validation and optional addition
    element_type = input("Type of Element: ")
    while element_type not in possible_types:
        add_new_type = input("This type doesn't exist. Add it? (Y to add, any other key to retype): ")
        if add_new_type.lower() == "y":
            possible_types.append(element_type)
        else:
            element_type = input("Type of Element: ")

    # Get room of element with validation and optional addition
    room = input("Room of Element: ")
    while room not in possible_rooms:
        add_new_room = input("This room doesn't exist. Add it? (Y to add, any other key to retype): ")
        if add_new_room.lower() == "y":
            possible_rooms.append(room)
        else:
            room = input("Room of Element: ")

    # Get dimensions with validated float inputs
    length = float_input("Length of Element: ")
    height = float_input("Height of Element: ")
    thickness = float_input("Thickness of Element: ")

    # Add the new element to the dictionary
    building_elements[element_key] = {
        "type": element_type,
        "room": room,
        "length": length,
        "height": height,
        "thickness": thickness
    }
    return building_elements

# Validates and converts user input to a float
def float_input(prompt):
    while True:
        try:
            return round(float(input(prompt)), 3)
        except ValueError:
            print("Please enter a valid number.")

# Validates and converts user input to an integer
def int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

# Calculate the area of a specific element and display it
def calculate_area(element_key):
    element = building_elements[element_key]
    area = element["length"] * element["thickness"]
    print(f"Properties of {element_key}: {element}")
    print(f"Area of {element_key}: {round(area, 2)} m²")
    continue_prompt()

# Calculate the volume of a specific element and display it
def calculate_volume(element_key):
    element = building_elements[element_key]
    volume = element["length"] * element["height"] * element["thickness"]
    print(f"Properties of {element_key}: {element}")
    print(f"Volume of {element_key}: {round(volume, 2)} m³")
    continue_prompt()

# Retrieve and display all elements of a specified type
def get_elements_by_type(element_type):
    matching_elements = {key: val for key, val in building_elements.items() if val["type"] == element_type}
    if not matching_elements:
        print(f"No elements found with type '{element_type}'. Check for typos.")
    else:
        print(f"Found {len(matching_elements)} elements of type '{element_type}':")
        for key, val in matching_elements.items():
            print(f"{key}: {val}")
    continue_prompt()

# Prompt the user to continue with another action
def continue_prompt():
    next_action = input("Do you want to perform another action? (Y for yes, any other key to quit): ")
    if next_action.lower() == 'y':
        user_decision()

# Allow the user to choose the next action
def user_decision():
    decision = input("\nChoose an action:\n"
                     "Y: Add a Building Element\n"
                     "A: Calculate Area of an Element\n"
                     "V: Calculate Volume of an Element\n"
                     "G: Get all Elements by Type\n"
                     "Q: Quit\n")
    
    if decision.lower() == "y":
        add_element()
        print(f"Current Building Elements: {building_elements}")
        user_decision()
    elif decision.lower() == "a":
        element_number = input("Number of Building Element to calculate Area: ")
        element_key = f"Building Element {element_number}"
        if element_key in building_elements:
            calculate_area(element_key)
        else:
            print("Invalid element number.")
            user_decision()
    elif decision.lower() == "v":
        element_number = input("Number of Building Element to calculate Volume: ")
        element_key = f"Building Element {element_number}"
        if element_key in building_elements:
            calculate_volume(element_key)
        else:
            print("Invalid element number.")
            user_decision()
    elif decision.lower() == "g":
        element_type = input("Type of Building Elements to show: ")
        get_elements_by_type(element_type)
    elif decision.lower() == "q":
        print("Goodbye!")
    else:
        print("Invalid choice. Try again.")
        user_decision()

# Main function to initialize and run the program
def main():
    generate_building_elements(int_input("Number of Building Elements to create: "))
    print("Generated Building Elements:", building_elements)
    user_decision()

if __name__ == "__main__":
    main()
"""