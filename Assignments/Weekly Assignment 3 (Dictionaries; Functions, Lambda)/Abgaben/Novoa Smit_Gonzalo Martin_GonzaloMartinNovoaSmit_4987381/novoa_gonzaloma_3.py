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

###
import random

#FUNCTIONS

def random_dim (x,y):
    # genearates a random dimension base on range with a format of 2 decimals
    dim = round (random.uniform (x,y), 2)
    return dim



def add_element (add_type, add_room, add_material, add_lenght, add_height, add_thick, add_key, add_master_key):
   
   new_element = {"type":add_type, "room":add_room, "material":add_material, "lenght":add_lenght, "height":add_height, "thick":add_thick}

   new_element_dic = ({add_key:new_element})
   
   building_elements.update ({add_master_key:new_element_dic})



def calculate_area (master_key, sub_key):

    get_length = building_elements[master_key][sub_key]["length"]
    get_heigth = building_elements[master_key][sub_key]["height"]

    area = get_length * get_heigth

    return round (area,2)



def calculate_volume (master_key, sub_key):

    get_length = building_elements[master_key][sub_key]["length"]
    get_heigth = building_elements[master_key][sub_key]["height"]
    get_thick = building_elements[master_key][sub_key]["thick"]

    volume = get_length * get_heigth * get_thick

    return round (volume,2)


def get_elements_by_type (type):
    for i in building_elements:
     elem = (building_elements.get(i))  
    
     for e in elem:
       if (elem[e]["type"]) == type:
        print (str(i) + ": " + str(building_elements.get(i)))



###Information Lists for Random Generation of Building Elements

type = ["wall", "window", "door", "floor","roof"]
room = ["living room","kitchen","bedroom", "dinning room", "basement"]
material = ["wood", "concrete", "ceramic", "stone", "brick", "plastic"]

###Master Dictionary

building_elements = {}


###Radom Building Elements Generation

    #Generates a "n" number of Dictionaries for each Element Categrory (Wall, Windows, Etc..)

for i in type:
    for e in range (3):

        elem_dict = i + "_" + str(e)
        master_key = "0" + str(type.index(i)) + ".0" + str (e)

        elem_value = {elem_dict:
                         {"type":i,
                          
                          "room":random.choice(room), 
                          
                          "material":random.choice(material), 

                          "length":random_dim (1, 4), 

                          "height":random_dim (1, 4), 

                          "thick":random_dim (0.10, 0.50)}}
        
        building_elements.update ({master_key:elem_value})


###Printing by line Each Building Element

print ("")
print ("Availabe Building Elements:")
print ("")

for i in building_elements:
    print (str(i) + ": " + str(building_elements.get(i)))

###Printing add_element Function

add_element ("wall", "living room", "wood", 5.6 , 3.00, 0.15, "wall_3", "00.03")

print ("")
print ("Updated Building Elements:")
print ("")

for i in building_elements:
    print (str(i) + ": " + str(building_elements.get(i)))

print ("")

###Printing calculate_area Function

ca_master_key = "00.00"
ca__sub_key = "wall_0"

print ("Calculated Area: " + ca__sub_key)

print (str(calculate_area ("00.00",'wall_0')) + " m2")

print ("")

###Printing calculate_volume Function

cv_master_key = "00.00"
cv__sub_key = "wall_0"

print ("Calculated Volume: " + cv__sub_key)

print (str(calculate_volume (cv_master_key,cv__sub_key)) + " m3")

print ("")

####Printing get_elements_by_type Function

elem_type = "door"

print ("Building Elements with specific type: " + elem_type)

print ("")

print (get_elements_by_type (elem_type))

print ("")
