import random
#Function to check if input is a float 
def ask_valid_float(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print('Invalid input! Please enter a number.')

# Dictionary to ask for all the input
prompts = {
    "material": "Enter material: ",
    "category": "Enter category (e.g. structure, enclosure, other): ",
    "element_type": "Enter type (e.g. roof, wall, stairs): ",
    "length": "Enter length (in meters): ",
    "height": "Enter height (in meters): ",
    "thickness": "Enter thickness (in meters): "
}

#Main Database that is a nested set
building_elements = {}

#Data for Randomization
random_materials = {"Graphene", "Concrete", "Glass", "Wood", "Recycled Plastics", "Plastic", "Steel", "Rubber", "Ceramic"}
random_categories = {"structure", "enclosure", "other"}
random_types = {"foundation", "slabs", "roof", "wall", "stairs", "door", "window"}

#Function to add element
def add_element():
    element = {} 
    #Iteration trhough every input Dictionary
    for key, prompt in prompts.items():
        if key in ["length", "height", "thickness"]: # Checking the numeric values for correct input
            element[key] = ask_valid_float(prompt)
        else:
            element[key] = input(prompt) 
    
    #Get Data from set and define as string for readability 
    material = element["material"]
    category = element["category"]
    element_type = element["element_type"]
    
    #Setting up the "key" ID
    initials = material[:2] + "." + category[:2] + "." + element_type[:2]
    element_id = len(building_elements) + 1
    element_key = f"{element_id}.{initials}"
    
    #Storing the set in the Dataset
    building_elements[element_key] = element
    print(f"Element added with ID {element_key}.")

#random element generation with a specified amount of genereations
def generate_random_element():
    element = {} 
    nmb_random_inputs = int(input('How many elements should be created? '))
    print("The following random elements were added:")
    for i in range(nmb_random_inputs):
        element["material"] = random.choice(list(random_materials))
        element["category"] = random.choice(list(random_categories))
        element["element_type"] = random.choice(list(random_types))
        element["length"] = random.uniform(1, 20)
        element["height"] = random.uniform(1, 20)
        element["thickness"] = random.uniform(1, 20)

        #Get Data from set and define as string for readability 
        material = element["material"]
        category = element["category"]
        element_type = element["element_type"]
        
        #Setting up unique ID
        initials = material[:2] + "." + category[:2] + "." + element_type[:2]
        element_id = len(building_elements) + 1
        element_key = f"{element_id}.{initials}"
    
        building_elements[element_key] = element
        
        print(f"{element_key}.")

#Function to display all items with unique ID
def get_all_elements():
    print("\nBuilding Elements:\n" + "="*50)
    for idx, key in enumerate(building_elements.keys(), start=1):
        print(f"{idx}. ID: {key}")
    print("="*50)

#Function to display all item with all Properties
def get_all_elements_detailed():
    print("\nDetailed Building Elements:\n" + "="*50)
    for idx, (key, value) in enumerate(building_elements.items(), start=1):  
        print(f"\n{idx}. ID: {key}")
        for prop, val in value.items(): #Loops to display each property. prop refers to property name, val represents the value 
            print(f"   {prop.capitalize()}: {val}")
        print("-" * 50)
    print("="*50)
#Function to display specific
def get_specific_element():
    print("\nAvailable Building Elements:\n" + "="*50)
    for idx, key in enumerate(building_elements.keys(), start=1):
        print(f"{idx}. ID: {key}")
    print("="*50)
    
    try:
        element_number = int(input("Enter the number of the element you want to view: ")) 
        selected_element_key = list(building_elements.keys())[element_number - 1] #change input to usable index
        
        print(f"\nBuilding Element with ID {selected_element_key}:\n" + "="*50)
        for prop, val in building_elements[selected_element_key].items():   #loop that iterates through element keys
            print(f"   {prop.capitalize()}: {val}")
        
        # Calling the FUnctions for calculations 
        calculate_area(selected_element_key)
        calculate_volume(selected_element_key)
        
        print("="*50)
        
    except (ValueError, IndexError):
        print("Invalid selection. Please try again.")

def calculate_area(spec_el_id): 
    element = building_elements[spec_el_id] #get the specified Element in get specific_element_function
    area = element["length"] * element["height"] 
    print(f"\nArea: {area} square meters.") 
    return area

def calculate_volume(spec_el_id):
    element = building_elements[spec_el_id]  #get the specified Element in get specific_element_function
    volume = element["length"] * element["height"] * element["thickness"]
    print(f"\nVolume: {volume} cubic meters.")  
    return volume

def get_elements_by_type(element_type):
    filtered_elements = {key: value for key, value in building_elements.items() if value["element_type"] == element_type} #for loop that iterates through a new dictionary, the type is filtered with the if statement, that checks for given type
    return filtered_elements

def print_elements_by_type(element_type):
    elements = get_elements_by_type(element_type) #
    if elements:
        print(f"\nBuilding Elements of type '{element_type}':\n" + "="*50)
        for idx, (key, value) in enumerate(elements.items(), start=1): #Loops to display filtered elements
            print(f"\n{idx}. ID: {key}")
            for prop, val in value.items(): #Loops to display each property. prop refers to property name, val represents the value 
                print(f"   {prop.capitalize()}: {val}")
            print("-" * 50)
    else:
        print(f"\nNo elements found for type '{element_type}'.")

def edit_element_properties():
    get_all_elements() #showing all the elements with a numeric ID

    try:

        element_number = int(input("Enter the number of the element you want to edit: ")) # Let the user select the element to edit by choosing a number
        selected_element_key = list(building_elements.keys())[element_number - 1]  # Adjust input to actual index
        print(f"\nSelected Element: ID {selected_element_key}")

        # Show the properties of the selected element with numbers 
        print("\nProperties available for editing:\n" + "-"*50)
        properties = list(building_elements[selected_element_key].keys())   #get all the keys of the properties
        for idx, prop in enumerate(properties, start=1):    # Uses counter as index for choosable option
            print(f"{idx}. {prop}") #prints property with counter as index
        
        prop_number = int(input("\nEnter the number of the property you want to edit: ")) #Asking what property to change
        if prop_number < 1 or prop_number > len(properties):
            print("Invalid property selection!")
            return
        
        prop_to_edit = properties[prop_number - 1] #changing the given input to index number
        
        # Ask the user for the new value
        if prop_to_edit in ["length", "height", "thickness"]:   
            new_value = ask_valid_float(f"Enter new value for {prop_to_edit}: ")
        else:
            new_value = input(f"Enter new value for {prop_to_edit}: ")
        
        building_elements[selected_element_key][prop_to_edit] = new_value #Updating new property
        print(f"{prop_to_edit} has been updated for element ID {selected_element_key}.")
        
    except (ValueError, IndexError):
        print("Invalid selection. Please try again.")
#Sub menu for adding
def add_menu():
    while True:
        user_choice2 = input(
            "\nAdd Element\nChoose an option:\n"
            "1. Add Element with specific properties\n"
            "2. Add one or more elements with random properties\n"
            "r. Resume to Main Menu\n"
            "Enter your choice: "
        )
        if user_choice2 == '1':
            add_element()
        elif user_choice2 == '2':
            generate_random_element()
        elif user_choice2.lower() == 'r':
            print("Resuming to main menu.\n")
            break
        else:
            print("Invalid choice! Please choose a valid option.")
#Sub menu for editing
def edit_menu():
    while True:
        user_choice2 = input(
            "\nEdit Element\nChoose an option:\n"
            "1. Edit element properties\n"
            "r. Resume to Main Menu\n"
            "Enter your choice: "
        )
        if user_choice2 == '1':
            edit_element_properties()
        elif user_choice2.lower() == 'r':
            print("Resuming to main menu.\n")
            break
        else:
            print("Invalid choice! Please choose a valid option.")
#Sub menu for viewing elements
def view_menu():
    while True:
        user_choice2 = input(
            "\nView Elements\nChoose an option:\n"
            "1. Show specific element\n"
            "2. View elements by type\n"
            "3. View all elements\n"
            "4. View all elements (detailed)\n"
            "r. Resume to Main Menu\n"
            "Enter your choice: "
        )
        if user_choice2 == '1':
            get_specific_element()

        elif user_choice2 == '2':
            element_type = input("Enter element type to filter by (e.g., wall, window): ")
            print_elements_by_type(element_type)
        elif user_choice2 == '3':
            get_all_elements()
        elif user_choice2 == '4':
            get_all_elements_detailed()
        elif user_choice2.lower() == 'r':
            print("Resuming to main menu.\n")
            break
        else:
            print("Invalid choice! Please choose a valid option.")
#Main menu Loop
while True:
    user_choice = input(
        "\nMain Menu\nChoose an option:\n"
        "1. Add Element ➕\n"
        "2. Edit Element 🔧\n"
        "3. View Elements and Properties 👁️\n"
        "q. Quit 🚪\n"
        "Enter your choice: "
    )
    if user_choice == '1':
        add_menu()
    elif user_choice == '2':
        edit_menu()
    elif user_choice == '3':
        view_menu()
    elif user_choice.lower() == 'q':
        print("Exiting the program.\n")
        break
    else:
        print("Invalid choice! Please choose a valid option.")
