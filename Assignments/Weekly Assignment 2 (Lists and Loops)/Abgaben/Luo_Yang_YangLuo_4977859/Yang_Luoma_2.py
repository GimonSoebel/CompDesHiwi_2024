#Populating a list of building elements
import random

#Property fields
type = ["wall", "window", "door", "beam", "column"] #list
room = ("living room", "staircase", "bedroom") #tuple
materials = {"Graphene", "Concrete", "Glass", "Wood", "Recycled Plastics"} #set

#append
type.append("canopy")
#extend
roomSet = ["kitchen", "wash room"]
roomList = list(room)
roomList.extend(roomSet)

#Generate unique id
def genID(i,type):
    id = "ELE_"+ type[0].upper() +"_"+ str(i)
    return id

#Generate random length
def genLen():
    len = random.uniform(0,8)
    return round(len,2)

#Generate random height
def genHei():
    hei = random.uniform(0,4)
    return round(hei,2)

buildElementList = []

for i in range(15):
    getType = random.choice(type)
    getID = genID(i,getType)
    getRoom = random.choice(roomList)
    getMa = random.choice(list(materials)) #convert set into list
    getHei = genHei()
    getLen = genLen()

    buildElementList.append((getID,getType,getRoom,getMa,getHei,getLen))

#print entire database
print("Entire database:")
for item in buildElementList:
    strEle = f"ID: {item[0]}, Type: {item[1]}, Room: {item[2]}, Material: {item[3]}, Height: {item[4]}, Length: {item[5]}"
    print(strEle)
    #print()
print()

#print the amount of elements:
print("The amount of elements:")
print(f"The amount is: {len(buildElementList)}")
print()

#check that one of your Data structures contains at least 5 different options or properties and communicate it
print("The properties contain more than 5 options")
allProperty = {"type":type,"material":materials,"room":roomList}
for k in range(len(allProperty)):
    item = list(allProperty.values())[k]
    if len(item)>5:
        print(f"{list(allProperty.keys())[k]}")
print()

#Print one specific property of one specific element and communicate its location on the list
eleInd = 5
print(f"For the NO.{eleInd} element, the NO.3 property is Material: {buildElementList[eleInd][3]}")
print()

#Optional challenge: requires more python knowledge: Print the 3 longest elements
print("The 3 longest elements")
sorted_elements = sorted(buildElementList, key=lambda x: x[5], reverse=True)[:3]
for item in sorted_elements:
    print(f"The element ID is: {item[0]}")

