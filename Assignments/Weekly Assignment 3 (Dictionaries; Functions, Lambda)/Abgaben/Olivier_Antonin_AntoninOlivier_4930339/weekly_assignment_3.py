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
"""
import random

Elements_type = {"wall", "window", "door", "beam", "column", "slab"}
Elements_room = {"living room", "staircase", "bedroom", "kitchen", "corridor"}


Elements_nbr = int(input("Please choose the number of elements"))
i = 1
building_elements = {"162712":{"type":"wall", "room":"living room", "length":1.34, "height":1.94, "thickness":0.18}} # creating the first element

while i < Elements_nbr: # filling the list of building elements, the value of each key are normaly obtained from hardcoding
   Element_key = str(random.randint(0,200000))
   Elements_length = round(random.uniform(0,5),3) # floats rounded to the nearest mm
   Elements_height = round(random.uniform(0,2),3)
   Elements_thickness = round(random.uniform(0,0.40),3)

   if Element_key not in building_elements.keys(): # to make sure keys are unique
      building_elements.update({str(Element_key): {"type":random.choice(list(Elements_type)), "room":random.choice(list(Elements_room)), "length":Elements_length, "height":Elements_height, "thickness":Elements_thickness}})
      i += 1

print("="*30 + " Buildings elements " + "="*30)
for key, value in building_elements.items(): # displaying only keys and values for better understanding
    print(f"Key: {key}, Value: {value}")
print("\n")

"""
2. Create a function called add_element that allows users to add a new building element to the building_elements dictionary.
This function should contained the previous contained parameters:
"""

def add_element(dictionary, element_type, element_room, element_length, element_height, element_thickness):
   type = str(element_type) # making sure we are dealing with strings and floats rounded to the nearest mm
   room = str(element_room)
   length = round(element_length,3)
   height = round(element_height,3)
   thickness = round(element_thickness,3)

   element_key = str(random.randint(0,200000)) # id chosen to be a random integer between 0 and 200000
   while element_key in building_elements.keys(): # changing the idea if it has already been taken
      element_key = str(random.randint(0,200000))
   dictionary.update({str(element_key): {"type":type, "room":room, "length":length, "height":height, "thickness":thickness}}) # adding a new element to the dictionary

add_element(building_elements, "wall", "living room", 3.23, 2.82, 0.25)

print("="*30 + " Adding one element " + "="*30) # displaying the new dictionary showing keys and values
for key, value in building_elements.items():
    print(f"Key: {key}, Value: {value}")
print("\n")


"""
3. Create a function called calculate_area that calculates and returns the area of a building element in m2.
"""
def calculate_area(element_key):
   key = element_key
   element = building_elements.get(key)
   length = element["length"]
   height = element["height"]
   area = round(length * height,3)
   return area


random_key = random.choice(list(building_elements.keys())) # picking a random element (id) to calculate its surface

print("="*15 + " Calculating the area of a random element " + "="*15)
area_element = calculate_area(random_key)
print(f"The area of the element id:{random_key} is {area_element}m²")
print("\n")
  

"""
Create a function called calculate_volume that calculates and returns the volume of a building element in m3.
The above two functions should take a key as a parameter and use the information from the building_elements dictionary to perform the calculations.
"""
def calculate_volume(element_key):
   key = element_key
   element = building_elements.get(key)
   length = element["length"]
   height = element["height"]
   thickness = element["thickness"]
   volume = round(length * height * thickness,3)
   return volume

random_key = random.choice(list(building_elements.keys())) # picking a random element (id) to calculate its volume

print("="*15 + " Calculating the volume of a random element " + "="*15)
volume_element = calculate_volume(random_key)
print(f"The volume of the element id:{random_key} is {volume_element}m³")
print("\n")

"""
4. Create a function called get_elements_by_type that takes a type (e.g., "wall," "window," "door") as a parameter and
returns a list of keys for all building elements of that specific type.
"""
def get_element_by_type(element_type):
   keys_list = []
   for key, value in building_elements.items():
      if value["type"] == element_type:
         keys_list.append(key)
   return keys_list

random_type = random.choice(list(Elements_type)) # picking a random type

print("="*15 + " Displaying the list of elements with the same type " + "="*15)
list_elements = get_element_by_type(random_type)
print(f"The elements with the id {list_elements} are all {random_type}s")
print("\n")
