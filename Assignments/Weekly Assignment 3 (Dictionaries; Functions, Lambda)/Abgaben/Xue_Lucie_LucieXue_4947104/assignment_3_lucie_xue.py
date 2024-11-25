#User input can't be just a number, has to have at least some form of string
def get_alnum_input(user_input):
    while True:
        if user_input.isdigit() == False:  # Checks if the input contains at least some form of string
            return user_input.lower()
        else:
            print("Please input a valid word, at least partially.")
            user_input = input("Enter again: ") 

def get_float_input(key_name, element_type):
    while True:
        x = input("What {} is your {}?: ".format(key_name, element_type))
        try:
            number = float(x)
            return number
        except ValueError:
            print("Please input a valid number.")
        
def check_element_type_amount(element_dictionary, element_type):
    element_type_amount = 0
    for element in element_dictionary:
        temp_dict = element_dictionary[element]
        temp_dict_values = temp_dict.values()
        if element_type in temp_dict_values:
            element_type_amount += 1
    return element_type_amount

def add_element_to_dict(ID_number, dictionary):
    element_gen_ID = ID_number # doesn't have to be inside the function
    element_type = get_alnum_input((input("What building element do you want to add?: ")))
    element_type_ID = check_element_type_amount(building_elements, element_type)
    element_room = get_alnum_input((input("In what room is your {}?: ".format(element_type))))
    element_length = get_float_input("length", element_type)
    element_height = get_float_input("height", element_type)
    element_thickness = get_float_input("thickness", element_type)
    dict_temp = {
        "ID": element_gen_ID,
        "type": element_type,
        "type_ID": element_type_ID,
        "room": element_room,
        "length": element_length,
        "height": element_height,
        "thickness": element_thickness,
    }
    #I don't understand what is meant with InW.01.23 as a key
    element_key = str(element_room[0:2]).capitalize() \
        + str(element_type[0]).capitalize() + "." + "{0:03}".format(element_type_ID+1)
    dictionary[element_key] = dict_temp

def print_nicely(dictionary):
    print("This is your current database of elements:")
    for key, value in dictionary.items():
        print("{}: {}".format(key, value))
    


###Task 1 & 2


#executing code
building_elements = dict()
ID_number = 0

while True:
    answer = input("Do you want to add another element? (Yes or No): ").lower()
    if answer == "yes":
        add_element_to_dict(ID_number, building_elements)
        ID_number += 1
    elif answer == "no":
        print_nicely(building_elements)
        break
    else:
        print("Enter either Yes or No.")



###Task 3

def calculate_area(dictionary, target_key):
    target_dict = dictionary.get("{}".format(target_key))
    length = target_dict.get("length")
    height = target_dict.get("height")
    area = length * height
    return area

def calculate_volume(dictionary, target_key):
    target_dict = dictionary.get("{}".format(target_key))
    length = target_dict.get("length")
    height = target_dict.get("height")
    thickness = target_dict.get("thickness")
    volume = length * height * thickness
    return volume

#executing code
#let the user check area of specific element
element_to_check = input("Please enter the key of the element you want the area & volume for: ")

while True:
    if building_elements.get(element_to_check) is None:
        element_to_check = input(f"Key '{element_to_check}' doesn't exist. Please re-enter: ")
    else:
        break

element_area = calculate_area(building_elements, element_to_check)
element_volume = calculate_volume(building_elements, element_to_check)
print(f"The area of {element_to_check} is {element_area} and the volume is {element_volume}.")



###Task 4

def get_elements_by_type(dictionary, target_element_type):
    temp_list = list() #could make nested dict again with element keys
    for key, element in dictionary.items():
        if element.get("type") == target_element_type:
            temp_list.append(element)
    return temp_list 

target_element = input("What element type do you want a list of?: ").lower()
all_target_elements = get_elements_by_type(building_elements, target_element)
print(f"These are all {target_element} elements:", *all_target_elements, sep="\n")


