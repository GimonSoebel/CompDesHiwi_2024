import uuid
import random


element_data = []


maxNum = 6  #maximum number of elements in the database 
num = list(range(0, maxNum))



#1. Create hardcoded written Data Structures

##Create unique IDs
ids = []
for i in num:
    new_uuid = str(uuid.uuid4())
    ids.append(new_uuid)

##Hardcoding other data 
types = ("Wall", "Window", "Door", "Floor", "Ceiling", "Piller", "Beam", "Other")  #tuple
materials =  {"Graphene", "Concrete", "Glass", "Wood", "Recycled Plastic"}   #set
rooms = ["Living Room", "Bedroom", "Kitchen", "Bathroom", "Staircase","Entrance Hall"]  #list
lengths = []    #will be created later
heights = []    #will be created later

##addition by hardcoding

materials.add("Paper Tube")
rooms.append("Bedroom2")


#2. Write a series of code lines that fill the database in one List 

##creating "num" sets of element and appending them to database
for i in num:
    Id = ids[i]
    Type = random.choice(types)
    Material = random.choice(list(materials)) #convert set to list
    Room = random.choice(rooms)
    Length = round(random.uniform(0.5, 12.0), 1) 
    Height = round(random.uniform(0.5, 8.0), 1)  
    
    eachElement = (Id, Type, Material, Room, Length, Height)   #data for each element

    element_data.append(eachElement)




#3. Print the Database with some added strings in a way that is nice to read

##Print the entire database
DataBase = []
n=0
for a in element_data:
    
    #eachData = "ID:" + a[0] + " TYPE:" + a[1] + " MATERIAL:" + a[2] + " ROOM:" + a[3] + " LENGTH:" + str(a[4]) + "m HEIGHT:" + str(a[5]) +"m"
    eachData = "ID:" + a[0], " TYPE:" + a[1] ," MATERIAL:" + a[2] , " ROOM:" + a[3] , " LENGTH:" + str(a[4]) +"m", "HEIGHT:" + str(a[5]) +"m"
    n += 1
    print(n, "=", eachData)
    DataBase.append(eachData)

#print(DataBase)
##Print the amount of elements
print("Total Number of Elements in the Database: " + str(len(element_data)))
#print(n-1) #this would also work


##Check that one of your Data structures contains at least 5 different options or properties and communicate it
ListofMaterialUsed = set()  #using set not to have overlap
for a in element_data:
      Material_used = a[2]
      ListofMaterialUsed.add(Material_used)  #get the list of all kinds of material used


if len(ListofMaterialUsed) >= 5:
        print("This building has at least 5 different materials:", ListofMaterialUsed)  
        #print(ListofMaterialUsed)
else:
        print("This building has less than 5 different materials:", ListofMaterialUsed)
        #print(ListofMaterialUsed)


##Print one specific property of one specific element and communicate its location on the list
##search for types
index = random.randint(0,len(element_data))
#element_index = element_data[index]
element_index = DataBase[index]

#print (element_index)
print ("The Element at the position of", index+1, "=", element_index[1])

##Optional challenge: requires more python knowledge  Print the 3 longest elements by length
sorted_elements = sorted(element_data, key=lambda x:(x[4]), reverse=True)
print("The 3 longest elements are:")
for s in range(3):
      print(s+1,"=",sorted_elements[s][4],"m")

