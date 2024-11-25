# Create an empty dictionary
building_elements={}

## add a new building element to the building_elements dictionary
def add_element(key,type,room,length,height,thickness):
    building_elements[key]={"type":type,"room":room,"length":length,"height":height,"thickness":thickness}

### calculate the area
def calculate_area(key):
    elements=building_elements.get(key)
    if elements==None:
        print("Wrong key")
    else:
        area=elements["length"]*elements["thickness"]
        print(f"The area of the element is {area} m²")
### calculate the violume
def calculate_volume(key):
    elements=building_elements.get(key)
    if elements==None:
        print("Wrong key")
    else:
        volume=elements["length"]*elements["thickness"]*elements["height"]
        print(f"The volume of the element is {volume} m³")

#### get all the keys for a certain type
def get_elements_by_type(type):
    all_matching_keys=[]
    for key,value in building_elements.items():
        if value["type"]==type:
            all_matching_keys.append(key)
    if all_matching_keys:
        return all_matching_keys
    else:
        return("Key not found")


##### example
##### 1. add new elements
add_element("InW.01.23","wall","living room",4,3.3,0.2)
add_element("Win.01.12","window","bedroom",2,2,0.1)
add_element("Win.02.33","window","bathroom",1.2,1.5,0.1)
##### 2. calculate the area and volume
calculate_area("InW.01.23")
calculate_volume("InW.01.23")
##### 3. if we give a key that doesn't exit
calculate_area("Win.01.23")
##### 4. get elements by type
print(get_elements_by_type("window"))