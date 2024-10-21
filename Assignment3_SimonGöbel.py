print("Hello iam an Building Information Modeling (BIM) Tool, i am here to assist you. Please Follow the steps below :D. ")

"""
Create a dictionary called building_elements that will store information about various building elements.
Each element should be identified by a unique key (e.g., a string or integer).
The value associated with each key should be another dictionary containing the following information: type, room, length, height, thickness.

key: The unique key for the element. (e.g. InW.01.23)
type: The type of the building element. (e.g., "wall," "window," "door," etc.).
room: The name of the room assigned to the building element. (e.g. "living room", "staircase" etc. )
length: The length of the element in meters.
height: The height of the element in meters.
thickness: The width of the element in meters.
"""

building_elements = {} 

"""
Create a function called add_element that allows users to add a new building element to the building_elements dictionary.
This function should contained the previous contained parameters:
"""

def add_element() : #creates a function that can be called for anytime

    while True :

        key = input("Add a unique key to the element you want to add: \n").lower() #every input is allowed for the key

        while True : #while loop to avoid wrong input from the user
            type_input = input("What type of building element do you want to add? (e.g., 'wall', 'window', 'door', etc.): \n").lower()
            if all(i.isalpha() or i.isspace() for i in type_input) : #checks every letter in the input if its alphabetic or has space in between
                break
            else :
                print("Invalid input. Please enter a valid type (has to be alphabetic). ") 

        while True : #while loop to avoid wrong input from the user
            room_input = input("What's the name of the room assigned to the building element? (e.g., 'living room', 'staircase', etc.): \n").lower()
            if all(i.isalpha() or i.isspace() for i in room_input) : #checks every letter in the input if its alphabetic or has space in between
                break
            else :
                print("Invalid input. Please enter a valid room (has to be alphabetic). ")

        while True : #while loop to avoid wrong input from the user
            try :
                length_input = float(input("What's the length of the element in meters?: \n"))
                break
            except ValueError : #doesn't allow input of values that aren't numeric or an float
                print("Invalid input. Please enter a valid length (has to be numeric). ")

        while True : #while loop to avoid wrong input from the user
            try :
                height_input = float(input("What's the height of the element in meters?: \n"))
                break
            except ValueError : #doesn't allow input of values that aren't numeric or an float
                print("Invalid input. Please enter a valid height (has to be numeric). ")

        while True : #while loop to avoid wrong input from the user
            try :
                thickness_input = float(input("What's the width of the element in meters?: \n"))
                break
            except ValueError : #doesn't allow input of values that aren't numeric or an float
                print("Invalid input. Please enter a valid thickness (has to be numeric). ")

        nested_dictionary = {'type': type_input, 'room': room_input, 'length': length_input, 'height': height_input, 'thickness': thickness_input} #creates a dictionary for all the values of the input
        building_elements[key] = nested_dictionary #nests the dictionary inside the already existing building_elements dictionary

        user_input = input("Type 'q' to exit the loop, or a different key to add another element: \n") #allows the user to put in more data or to quit the loop
        if user_input.lower() == 'q' :
            break

        print("_______________________________________________")

    return

add_element() #calls the function

print("__________________________________________________________________________________")

"""
Create a function called calculate_area that calculates and returns the area of a building element in m2.
Create a function called calculate_volume that calculates and returns the volume of a building element in m3.
The above two functions should take a key as a parameter and use the information from the building_elements dictionary to perform the calculations.
"""

def calculate_area(key) :

    element = building_elements.get(key) #key is a yet non existing value that later gets replaced with the value of key_input & .get() method returns the value of the item with the specified key

    if element : #checks if element is a existing value
        return element['length'] * element['thickness'] #element here has the value of key_input and then looks for the values of the keys 'length' and 'thickness' inside the nested dictionary
    else :
        return None #if element isn't an existing value nothing happens

def calculate_volume(key) :

    element = building_elements.get(key) #key is a yet non existing value that later gets replaced with the value of key_input & .get() method returns the value of the item with the specified key

    if element : #checks if element is a existing value
        return element['length'] * element['height'] * element['thickness'] #element here has the value of key_input and then looks for the values of the keys 'length', 'height' and 'thickness' inside the nested dictionary
    else :
        return None #if element isn't an existing value nothing happens

print("In the next step we want to run a calculation of the area and volume of an element. ")

while True : #while loop to avoid wrong input from the user

    key_input = input("Enter the key of the building element you want to run the calculation on: \n").lower() 

    if all(i.isdigit() or i.isspace() or i.isnumeric for i in key_input) and key_input in building_elements: #checks every letter in the input if its alphabetic or numeric or has space in between
        break
    else :
        print("Invalid input. Please enter a valid key (numeric and must exist in the dictionary). ")

area = calculate_area(key_input) #calls for the function, but now with the value of key_input assigned to it
volume = calculate_volume(key_input) #calls for the function, but now with the value of key_input assigned to it

if area is not None: #checks if the area has an value assigned to it
    print(f"Your building element has an area of {area} m2.")
else : 
    print("Invalid key entered for area calculation.")

if volume is not None: #checks if the volume has an value assigned to it
    print(f"Your building element has a volume of {volume} m3.")
else :
    print("Invalid key entered for volume calculation.")

print("______________________________________________________________________________________________")

"""
Create a function called get_elements_by_type that takes a type (e.g., "wall," "window," "door") as a parameter and
returns a list of keys for all building elements of that specific type.
"""

def get_elements_by_type(element_type) : #element_type is a yet non existing value that later gets replaced with the value of type_to_search

    keys_of_type = [] #creates a list that stores the values for the keys

    for key, element in building_elements.items() : #.items() method returns the key-value pairs of the dictionary, as tuples in a list
        if element['type'] == element_type :
            keys_of_type.append(key)
    return keys_of_type

print("In the next step we want to find out the keys assigned to an specific type of building element. ")

type_to_search = input("Enter the type of building element you want to find the keys for: \n").lower()
elements_of_type = get_elements_by_type(type_to_search) #calls for the function, but now with the value of type_to_search assigned to it

if elements_of_type : #checks if elements_of_type has an value assigned to it
    print(f"Keys of building elements with the type '{type_to_search}': {elements_of_type}")
else :
    print(f"No building elements found with the type '{type_to_search}'.")

print("")

print("Thank you, that's all for today :D")