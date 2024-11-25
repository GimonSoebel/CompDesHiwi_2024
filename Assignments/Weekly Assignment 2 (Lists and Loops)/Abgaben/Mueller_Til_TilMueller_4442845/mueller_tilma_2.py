# 1. Hardcoded Datastructure, one each = Tuple, List, Set

load_bearing = (True, False)            # Tuple
material = ["Wood", "Glass", "Concrete", "Steel"] # List
room = {"living_room", "dining_room", "bath_room", "corridor", "bed_room"}  # Set
lenght = [1, 2, 3, 4, 5]              # Set

# List operations
material.append("Plastics")
lenght.insert(1, 1.5)

print("These are the available materials : " , [material])
print("And these are the available rooms : " , [room])
print("This value shows rather the element is loadbearing or not : " , [load_bearing])
print("These are the available lenghts : " , [lenght])


# 2. Defining Building Elements in one nested Tuple
ElementDataBase = [
   ["First Element", material[1], "living_room", load_bearing[0], lenght[0]],   # First element
   ["Second Element", material[2], ["living_room", "dining_room"], load_bearing[1], lenght[1]], #Second element
   ["Third Element", material[4], "bath_room", load_bearing[1], lenght[2]],  #Thrid element
   ["Fourth Element", material[3], "corridor", load_bearing[1], lenght[2]],  #Fourth element
   ["Fith Element", material[3], ["Living_room", "bath_room", "bed_room"], load_bearing[0], lenght[3]],  #Fith element
   ["Sixth Element", material[2], "bath_room", load_bearing[0], lenght[4]],  #Sixth element
   ["Seventh Element", material[3], "bed_room", load_bearing[0], lenght[2]],  #Seventh element
   ["Eighth Element", material[2], "dining_room", load_bearing[1], lenght[4]],  #Eighth element
   ["Nineth Element", material[1], "dining_room", load_bearing[1], lenght[1]],  #Nineth element
   ["Tenth Element", material[1], "corridor", load_bearing[1], lenght[0]],  #Tenth element
   ]

#print(ElementDataBase)

#Thanks ChatGPT
# Count the total number of tuples within all elements in ElementDataBase
tuple_count = sum(1 for element in ElementDataBase for item in element if isinstance(item, tuple))

# Count the number of elements in ElementDataBase (each list represents one element)
element_count = len(ElementDataBase)

print(f"Number of elements in ElementDataBase: {element_count}")

property_options = {
    "name": 0,
    "material": 1,
    "rooms": 2,
    "load_bearing": 3,
    "length": 4,
}

# Print one proporty of one Element and comunicate the possition

#User Input
a = int(input ("Which element would you like to take a closer look at?  ")) -1
b = input ("Which proporty would you like to take a closer look at? Possible options are: material, rooms, load_bearing or lenght:  "  )


property_index = property_options[b]

print("okay, we are looking at the  " , ElementDataBase[a][a])
print("The desired property ", [b], "is:   "  , ElementDataBase[property_index][property_index] )
#Comunicate possition

property_index = int[property_position] + 1

print("The proporty",[b], "is the", [property_position], ". property in the list.")
#if a == int ("The (Elemen) )
#else print("please input an interger")

#print([ElementDataBase[input == a][input == b]])




# Check for difference of Building Elements
# Change Tuple to set



#if ElementDataBase[0] == ElementDataBase[1]:
 #   print("They are the same")

#else:
#    print("They are not the same")


