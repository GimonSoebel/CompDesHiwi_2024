import random
import uuid

maxNum = 10  #maximum number of elements in the database 
num = list(range(0, maxNum))
element_data = {}
new_element_data = {}

##Create ids for initial data
keys = []

for i in num:
    key = str(i)
    keys.append("element"+key)

###Hardcoding others for initial data
types = ["wall", "window", "door", "floor", "ceiling", "piller", "beam", "other"]  
materials =  ["graphene", "concrete", "glass", "wood", "recycled plastic","paper"] 
rooms = ["living room", "bedroom", "kitchen", "bathroom", "bedroom2", "staircase","entrance hall"] 
   #length, height, thickness will be created later
    

element_data = {}
for i in num:
    Id = keys[i]
    
    element_data[Id]= {
        "element_type" : random.choice(types),
        "material" : random.choice(materials), 
        "room" : random.choice(rooms),
        "length" : round(random.uniform(0.5, 12.0), 1),
        "height" : round(random.uniform(0.5, 8.0), 1),  
        "thickness" : round(random.uniform(0.01, 0.5), 2),
        }

    


#print (element_data)


#def add_element(element_data, Id, element_type, material, room, length, height, thickness):
def add_element(Id, type, material, room, length, height, thickness):
    """
    Adding a new element with user inputs
    """

    new_element_data= {
        "element_type" : type,
        "material" : material, 
        "room" : room,
        "length" : length,
        "height" : height,  
        "thickness" : thickness,
        }
    
    element_data[Id] = new_element_data

    print("Element added successfully!\n", new_element_data)


def calculate_area(Id):
    """
    Calculating the area of a building element
    """
    element = element_data.get(Id)
    if not element:
        print("Element not found.")
        return None
    
    area = element["length"] * element["height"]
    print(f"Area of element '{Id}' is {area} m².")
    return area


def calculate_volume(Id):
    """
    Calculating the volume of a building element
    """
    element = element_data.get(Id)
    if not element:
        print("Element not found.\n")
        return None

    volume = element["length"] * element["height"] * element["thickness"]
    print(f"Volume of element '{Id}' is {volume} m³.\n")
    return volume


def search_elements_by_type(search_type):
    """
    Getting elements with specifin type from user input
    """
   
    searching_elements = [Id for Id, details in element_data.items() if details['element_type'] == search_type]
    if searching_elements:
        print(f"Elements of type '{search_type}': {searching_elements}\n")
    else:
        print(f"No elements of type '{search_type}' found.\n")
    return searching_elements




def to_start():
    """
    Showing a menu to start
    """
    while True:
        print("These are the elements in your element dictionary:\n", element_data)
        print("1. Add a building element")
        print("2. Calculate area of an element")
        print("3. Calculate volume of an element")
        print("4. Get elements by type")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            Id = input("Enter a unique key for the element: ")
            if Id in element_data:
                print("This key already exists. Please enter a unique key.")
                return
            
            type = input("What is your element's type?")
            material = input("What is its material?")
            room = input("Which room does it belong to?")
            length_str = input("what is its length?") 
            length = float(length_str)
            height_str = input("what is its height?") 
            height = float(height_str)
            thickness_str = input("what is its thickness?") 
            thickness = float(thickness_str)

            add_element(Id, type, material, room, length, height, thickness)
            
        elif choice == "2":
            search_key = input("Enter the key of the element to calculate its area: ")
            calculate_area(search_key)
            

        elif choice == "3":
            search_key = input("Enter the key of the element to calculate its volume: ")
            calculate_volume(search_key)
            

        elif choice == "4":
            search_type = input("Enter the type of element to search: ")
            search_elements_by_type(search_type)
            

        elif choice == "5":
            print("Exiting the program. Thank you so much! Hope to see you soon:)")
            break
        else:
            print("Invalid option. Please try again.\n")


to_start()
