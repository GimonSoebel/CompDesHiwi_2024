
#1.  Create a dictionary called building_elements that will store information about various building elements.
#Each element should be identified by a unique key (e.g., a string or integer).
#The value associated with each key should be another dictionary containing the following information: type, room, length, height, thickness.

# List of types and rooms
type = ["door", "window", "Floor", "wall", "ceiling"]
room = ["bathroom", "hallway", "diningroom", "livingroom", "kitchen"]


from random import uniform

# empty dici
building_elements = {}

# add elements to dici
for i in range(5): 
    building_elements[i] = {
        "room": room[i],
        "type": type[i],
        "height": round(uniform(1, 10), 2),
        "length": round(uniform(1, 10), 2),
        "width": round(uniform(1, 10), 2),
    }

# print dictionary 
print(building_elements)

#2. Create a function called add_element that allows users to add a new building element to the building_elements dictionary.
#This function should contained the previous contained parameters:

#Ask user to input parameters
addtype = input("What type would you like to add?") 
addroom = input("What room would you like to add?") 
addheight, addlenght, addwidth = input("Please type the height, lenght and width of the room, spererated by a space").split()

listlengh1 = len(building_elements)

#Create a new element
add_element = {
    listlengh1: {
        "type": addtype,
        "room": addroom,
        "height": addheight,
        "length": addlenght,
        "width": addwidth,
   }
}

#add_element =  {listlenght: {"type": addtype, "room": addroom, "height": addheight, "length": addlenght, "width": addwidth}}

building_elements.update(add_element)

listlenght2 = len(building_elements)
#print(listlenght)

print(building_elements)
x = building_elements.get(1)
print(x)
#print(type(x))

#3. Create a function called calculate_area that calculates and returns the area of a building element in m2.
#Create a function called calculate_volume that calculates and returns the volume of a building element in m3.
#The above two functions should take a key as a parameter and use the information from the building_elements dictionary to perform the calculations.

#GEtting Dimensions from Dictionary
dim1 = [float(element["length"]) for element in building_elements.values()]
dim2 = [float(element["width"]) for element in building_elements.values()]
dim3 = [float(element["height"]) for element in building_elements.values()]
 

def area(lengths, widths):
    total_area = 0
    for l, w in zip(lengths, widths):  
        total_area += l * w
    return total_area

total_area = round(area(dim1, dim2),2)
print("The total area is: ", total_area)  

def volume(lengths, widths, heights):
    total_volume = 0
    for l, w, h in zip(lengths, widths, heights):  
        total_volume += l * w * h
    return total_volume

total_volume = round(volume(dim1, dim2, dim3),2)
print("The total volume is: ", total_volume)  


#4. Create a function called get_elements_by_type that takes a type (e.g., "wall," "window," "door") as a parameter and
       # returns a list of keys for all building elements of that specific type.
 
# Get range of listlenght2, plus every number per iteration


def get_elements_by_type(building_elements, element_type):
    matching_keys = []
    for key, value in building_elements.items():
        if value["type"] == element_type:
            matching_keys.append(key)
    return matching_keys

key_window = get_elements_by_type(building_elements, "window")
print("The Keys of elements with type 'window' is in the :", key_window, ". dictionary")

