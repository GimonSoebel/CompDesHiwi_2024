########## Assignment 03
###### 1.:
#create the Database
element_name = ["element01", "element02", "element03", "element04"]

element01 = {"Typ": "Wall", "Room": "Bedroom", "Length": "3m", "Height": "3m", "Thickness": "0,4m"}
element02 = {"Typ": "Window", "Room": "Kitchen", "Length": "0,5m", "Height": "1m", "Thickness": "0,06m"}
element03 = {"Typ": "Door", "Room": "Livingroom", "Length":"0,8m", "Height":"2m", "Thickness": "0.08m"}
element04 = {"Typ": "Equipment", "Room": "Bathroom", "Length":"0,2m", "Height":"0,5m", "Thickness": "0.05m"}

# the building_elements dictionary is constructed out of items from different lists and dictionaries, that define name and properties of elements.
# in this way i am able to retrieve the element properties in the following tasks
building_elements ={element_name[0] : element01, element_name[1] : element02, element_name[2] : element03, element_name[3] : element04}

### Print the Elements
from pprint import pprint
pprint(building_elements)



###### 2.:   
###### create a definition to add a new element
# create a UDF inside a UDF. ask user if they want to add a new element first, before starting the process of asking for input.
def add_element():
            
            new_element_name = input("What is the element name?:")
            element_name.append(new_element_name)
            
            new_element_prop = {
                    "type" : input("What is the Element Type?:"),
                    "room" : input("What is the Element Room?:"),
                    "length" : input("What is the Element length?:"),
                    "height" : input("What is the Element height?:"),
                    "thickness" : input("What is the Element thickness?:")
            }

            building_elements[new_element_name] = new_element_prop

def first_another_element():
             
             ask_user = input("Would you like to add another Element(yes/no) ?:")
             clean_text = ask_user.strip().lower()

             while clean_text == "yes":
                     add_element()
                     pprint(building_elements)
                     ask_user = input("Would you like to add another Element(yes/no) ?")
                     clean_text = ask_user.strip().lower()
                     if clean_text != "yes":
                             break

first_another_element()

# acalculate area and volume by calling the value from the keys "length, height and thickness" inside the element properties dictionaries
# clean up the user input and the data from dict and convert into float
def calculate_area():
        area_input = input("What Element Area would you like to calculate (e.g: element01)?:")
        chosen_element = building_elements.get(area_input.strip().lower())

        if chosen_element:
                a = chosen_element["Height"]
                b = chosen_element["Length"]

                length = float(a.replace("m","").replace(",", "."))
                height = float(b.replace("m","").replace(",", "."))

                area = length * height
                print(f"The area of {area_input} is {area} m².")

        else:
                print("Element not found. Please try again.")

while True:
        ask_for_area = input("Would you like to to calculate the area of an element (yes/no)?:").strip().lower()
        if ask_for_area == "yes":
                calculate_area()
        else:
                break

# calculate volume
def calculate_volume():
        volume_input = input("What Element Volume would you like to calculate (e.g: element01)?:")
        chosen_element_volume = building_elements.get(volume_input.strip().lower())

        if chosen_element_volume:
                a = chosen_element_volume["Height"]
                b = chosen_element_volume["Length"]
                c = chosen_element_volume["Thickness"]

                length = float(a.replace("m","").replace(",", "."))
                height = float(b.replace("m","").replace(",", "."))
                thickness = float(c.replace("m","").replace(",", "."))

                volume = length * height * thickness
                print(f"The area of {volume_input} is {volume} m³.")

        else:
                print("Element not found. Please try again.")

while True:
        ask_for_area = input("Would you like to to calculate the Volume of an element (yes/no)?:").strip().lower()
        if ask_for_area == "yes":
                calculate_volume()
        else:
                break

# extract the elements that have specific types
# 
def get_element_by_type(element_typ):
        matching_elements = []

        for key, properties in building_elements.items():
                if properties["Typ"].lower() == element_typ.lower():
                        matching_elements.append(key)
        return matching_elements

type_input = input("What Type are you looking for (e.g. Wall, Window)?:").strip()
matching_elements = get_element_by_type(type_input)

if matching_elements:
        print(f"Elements of type {type_input}: {matching_elements}")

else:
        print(f"No elements found for type {type_input}")

