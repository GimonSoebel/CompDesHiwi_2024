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
#Jasmine Zhu
import random as rand
from tabulate import tabulate          #pls install tabulate with pip

## 1.Define Data Base fields using data structures
fields = ("Key", "Building Element", "Room", "Length", "Height", "Thickness")
numofelements = 10          #can use rand to generate arbitrary int of elements


elementoptions = {"Foundation", "Floor", "Column", "Beam", "Wall", "Ceiling", "Roof"}
roomoptions = ("Morgue", "Operating Room", "Staff Room", "Bathroom", "Closet", "Office")
minlength = 0.5
maxlength = 6.0
minheight = 2.2
maxheight = 3.5
minthickness = 0.1
maxthickness = 0.5

# elementids = []
# buildingelements = []
# rooms = []
# materials = []
# lengths = []
# volumes = []

building_elements = {}
for item in range(0,numofelements):
    #generate key
    keyspelledout = rand.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=5)
    currentkey = ''
    for character in keyspelledout:
        currentkey = currentkey+character
    # elementids.append(currentid)

    #generate building element
    currentelement = (rand.choice(tuple(elementoptions)))

    #generate room
    currentroom = (rand.choice(roomoptions))

    #generate length
    currentlength = round(rand.uniform(minlength, maxlength), 2)

    #generate height
    currentheight = round(rand.uniform(minheight, maxheight), 2)

    #generate thickness
    currentthickness = round(rand.uniform(minthickness, maxthickness), 2)

    #create dictionary entry
    elemententry = {'type':currentelement, 'room':currentroom, 'length':currentlength, 'height':currentheight, 'thickness':currentthickness}
    building_elements.update({currentkey:elemententry})

def add_element(newtype, newroom, newlength, newheight, newthickness):
    keyspelledout = rand.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=5)
    newkey = ''
    for character in keyspelledout:
        newkey = newkey+character

    newelemententry = {'type':newtype, 'room':newroom, 'length':float(newlength), 'height':float(newheight), 'thickness':float(newthickness)}
    building_elements.update({newkey:newelemententry})

def calculate_area(key):                                                    #not calculating correctly, slightly off perhaps from a rounding error
    keyelement = building_elements.get(key)
    area = round((keyelement.get('length'))*(keyelement.get('height')), 2)
    return area

def calculate_volume(key):                                                  #not calculating correctly, slightly off perhaps from a rounding error
    keyelement = building_elements.get(key)
    keyelement = building_elements.get(key)
    volume = round((keyelement.get('length'))*(keyelement.get('height'))*(keyelement.get('thickness')), 3) 
    return volume

def get_elements_by_type(elementtype):
    matches = []
    bldg_elem_list = list(building_elements.values())
    for x in bldg_elem_list:
        if (x.get('type')==elementtype):
            matches.append(list(building_elements.keys())[bldg_elem_list.index(x)])
    return matches

def menu():
    ans=True
    while ans:
        print(("""
        1.View Database
        2.Add Element
        3.Find area of element
        4.Find volume of element
        5.Search elements by type
        6.Quit
        """))

        ans=input("Enter the number of the task you'd like to perform:")
        if ans=="1": 
            flat_bldg_elem = [[name, *inner.values()] for name, inner in building_elements.items()]
            print(tabulate(flat_bldg_elem, headers=fields)) 
        elif ans=="2":
            newType = input("Enter the type of the element you wish to add:")
            newRoom = input("Enter the room of the element you wish to add:") 
            newLength = input("Enter the length of the element you wish to add:")
            newHeight = input("Enter the height of the element you wish to add:")
            newThickness = input("Enter the thickness of the element you wish to add:")
            add_element(newType,newRoom, newLength, newHeight, newThickness)
        elif ans=="3":
            requestKey= input("Enter the key of the element you want the area of:")
            requestedArea = calculate_area(requestKey)
            print("The area of element", requestKey, "is", requestedArea, "m^2") 
        elif ans =="4":
            requestKey= input("Enter the key of the element you want the volume of:")
            requestedVolume = calculate_volume(requestKey)
            print("The volume of element", requestKey, "is", requestedVolume, "m^3")
        elif ans=="5":
            requestedtype = input("What type of element are you looking for?")
            elementsintype = get_elements_by_type(requestedtype)
            if not elementsintype:
                print("There are no", requestedtype.lower(), "elements")
            else:
                print ("The following keys correspond to", requestedtype.lower(), "elements in the database:", elementsintype)
        elif ans=="6":
            print("\n Goodbye")
            break
        elif ans !="":
            print("\n Not Valid Choice Try again") 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

menu()