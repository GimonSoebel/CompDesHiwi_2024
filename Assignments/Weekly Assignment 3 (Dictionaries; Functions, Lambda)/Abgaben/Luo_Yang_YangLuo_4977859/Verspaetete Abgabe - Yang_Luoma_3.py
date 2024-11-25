#Create a dictionary call building_elements
building_elements = {}

keyitem = 0

def function_bar(keyitem):
    i = int(input(" 1:add element \n 2:calculate area \n 3:calculate volumne \n 4:get element by type \n 5:clear all \n 6:print all \n"))
    if i == 1:
        add_element(keyitem)
    if i == 2:
        calculate_area()
    if i == 3:
        calculate_volume()
    if i == 4:
        get_elements_by_type()
    if i == 5:
        keyitem == 0
        building_elements.clear()
    if i == 6:
        print(building_elements)

#Create a function called add_element that allows users to add a new building element
def add_element(keyitem):
    ele_type = str(input("What is the type?"))
    ele_room = str(input("What is the room?"))
    ele_length = float(input("What is the length?"))
    ele_height = float(input("What is the height?"))
    ele_thickness = float(input("What is the thickness/width?"))

    keyStr = ele_type[0].upper()+ele_room[0].upper()+"_"+str(keyitem)

    building_elements[keyStr] = {"type":ele_type,"room":ele_room,"length":ele_length,"height":ele_height,"thickness":ele_thickness}
    return

#Create a function called calculate_area
def calculate_area():
    area = lambda a,b:a*b
    keys = building_elements.keys()
    print("All the keys are below:")
    for item in keys:
        print(item)
    setItem = input("Select the key: \n")
    if setItem in keys:
        length = building_elements[setItem]["length"]
        wid = building_elements[setItem]["thickness"]
        print(f"The area is {area(length,wid)} m²")
    elif len(building_elements) == 0:
        print("Please fill the building_elements dictionary first!")
    elif setItem not in keys: print("Please insert correct key!")

#Create a function called calculate_volume
def calculate_volume():
    volume = lambda a,b,c:a*b*c
    keys = building_elements.keys()

    print("All the keys are below:")
    for item in keys:
        print(item)
    setItem = input("Select the key: \n")
    if setItem in keys:
        length = building_elements[setItem]["length"]
        wid = building_elements[setItem]["thickness"]
        hei = building_elements[setItem]["height"]
        print(f"The volume is {volume(length,wid,hei)} m³")
    elif len(building_elements) == 0:
        print("Please fill the building_elements dictionary first!")
    elif setItem not in keys: print("Please insert correct key!")

#Create a function called get_elements_by_type
def get_elements_by_type():
        keys = building_elements.keys()
        values = building_elements.values()
        types = []
        for item in values:
            types.append(item["type"])
        setTypes = set(types)

        print("All the types are below:")
        for itemType in setTypes:
            print(itemType)

        setType = input("Select the type: \n")
        if setType in setTypes:
            keylist = []
            for key in keys:
                if building_elements[key]["type"] == setType:
                    keylist.append(key)
            print(f"The keys contains the specific type: {keylist}")

        elif len(building_elements) == 0:
            print("Please fill the building_elements dictionary first!")
        else: print("Please insert correct type!")

while True:
    print("")
    function_bar(keyitem)
    keyitem += 1
