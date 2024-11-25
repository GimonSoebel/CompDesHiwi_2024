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

# 00-01-T-001 (Floor-Room-Tür-Nr)
# T - F - WA - WI - FB - D - ST - 

import inquirer

building_elements = {
    "00-01-T-001" : {
        "Type" : "Tür",
        "Room" : "Diele",
        "Room-nr" : "01",
        "Width" : 0.985,
        "Height" : 1.985,
        "Thickness" : 0.05,
        "Material" : "Holz"
    },
    "00-02-T-001" : {
        "Type" : "Tür",
        "Room" : "Küche", 
        "Room-nr" : "02", 
        "Width" : 0.985, 
        "Height" : 1.985,
        "Thickness" : 0.05,
        "Material" : "Holz"
    }, 
    "00-01-WA-001" : {
        "Type" : "Wand Außen", 
        "Room" : "Diele",
        "Room-Nr" : "01",
        "Width" : 6.25,
        "Height" : 3.5,
        "Thickness" :  0.25,
        "Material" : "Beton"
    }
}


""" def addelement ():
        building_elements.update({input("Building Element ID: "):
        {"Type" : input('Please enter the building element type: '),
        "Room" : input('Please enter the room description: '),
        "Room Nr" : int(input('Please enter the room number: ')),
        "Width" : float(input('Width of building element in meters: ')),
        "Height" : float(input('Height of building element in meters: ')),
        "Thickness" :  float(input('Thickness of building element in meters: ')),
        "Material" : inquirer.prompt(questions)}
        }
        )
 """

def addelement ():

    questions = [
    inquirer.List('Material',
                    message="Choose the material of your building element: ",
                    choices=['Timber', 'Concrete', 'Brick', 'Metal'],),]

    id_input = input("Building Element ID: ")
    type_input =  input('Please enter the building element type: ')
    room_input = input('Please enter the room description: ')
    nr_input = int(input('Please enter the room number: '))
    width_input = float(input('Length of building element in meters: '))
    height_input = float(input('Height of building element in meters: '))
    thickness_input = float(input('Thickness of building element in meters: '))
    material_input = inquirer.prompt(questions)

    confirm = [
    inquirer.Confirm("continue", message="Should I implement the element into the database?", default=True),
]
    confirmation_input = inquirer.prompt(confirm)
   
    if confirmation_input["continue"]:
        building_elements.update({id_input : {"Type" : type_input, "Room" : room_input, "Room Nr." : nr_input, "Width" : width_input, "Height" : height_input, "Thickness" : thickness_input, "Material" : material_input}})
        
        for key,value in building_elements.items():
            print (f" Element-ID: {key}")
            for k,v in value.items():
                print(f"  {k} : {v}")
            print (" ")
            print ("- "*20)
            print (" ")
            print("Your Element has been added to the dictionary")

    else:
         print("Operation aborted. The input was not added.")

                        

# function calculate area
def calculate_area ():
    # create a list of the keys 
    keys_list = list(building_elements.keys())

    # choose a list item
    questions_key = [
        inquirer.List(
            "Building Elements",
            message="Please choose a key from the dictionary:",
            choices=keys_list,
        ),
    ]
    # prompting the choosing and extracting the value
    answer_key = inquirer.prompt(questions_key)

    selected_key = answer_key["Building Elements"]
    print(selected_key) # just the value of the key

    # extracting a specific value in the nested dictionary
    # multiply the width and height values

    area = building_elements[selected_key]['Width']* building_elements[selected_key]['Height']
    print(f"The area of this element is {area} squaremeters")

def calculate_volume ():
     # create a list of the keys 
    keys_list = list(building_elements.keys())

    # choose a list item
    questions_key = [
        inquirer.List(
            "Building Elements",
            message="Please choose a key from the dictionary:",
            choices=keys_list,
        ),
    ]
    # prompting the choosing and extracting the value
    answer_key = inquirer.prompt(questions_key)

    selected_key = answer_key["Building Elements"]
    print(selected_key) # just the value of the key

    # extracting a specific value in the nested dictionary
    # multiply the width and height values

    volume = building_elements[selected_key]['Width']* building_elements[selected_key]['Height']*building_elements[selected_key]['Thickness']
    print(f"The volume of this element is {volume} cubicmeters")



def get_elements_by_type()
    # extract "Type" value and convert into list
    type_values = list({element["Type"] for element in building_elements.values()})
    print("Available Types:", type_values)

    # choose a list item
    questions_type = [
            inquirer.List(
                "Types",
                message="Please choose a element type:",
                choices=type_values,
            ),
        ]
    # prompting the type choosing
    answer_type = inquirer.prompt(questions_type)

    # just the value of the type
    selected_type = answer_type["Types"]
    print(f"Alle Elemente der Kategorie '{selected_type}':") 

    # for this category -> print ID
    for key,value in building_elements.items():
        if building_elements[key]["Type"] == selected_type:
            print (f" Element-ID: {key}")




addelement ()

calculate_area()
calculate_volume()

get_elements_by_type()
