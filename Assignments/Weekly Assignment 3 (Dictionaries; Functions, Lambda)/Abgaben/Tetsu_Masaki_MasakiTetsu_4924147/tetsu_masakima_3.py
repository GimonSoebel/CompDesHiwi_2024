def main():
    
    # A dictionary for input function messages
    message_dict = {
        "init":"You can create a building element dictionary with this python file.\n"\
            "Please add elements following the instruction below.",
        "continue":"\nWhat would you like to do next?\n"\
            "Options(1-4):\n"\
            "  1: Add items in the building element dictionary\n"\
                "  2: Show all building elements\n"\
                    "  3: Calculate area and volume of a building element in the dictionary\n"\
                        "  4: Create a list of keys for all building elements of the specific type\n"\
                            "Please type the number (Do you want to quit?(type 'q')): ",
        "analysis":"Please type the id number which you want to analysis(e.g. MA_00001): ",
        "get_eles":"Please type a building element type (e.g. wall, window): ",
        "type":"What is the type of the building element? (e.g.'wall','window','door', etc.): ",
        "room":"What is the name of the room assigned to the building element? (e.g.'living room', 'staircase' etc. ): ",
        "length":"What is the length of the element in meters? (e.g. 2.3, 3.0): ",
        "height":"What is the height of the element in meters? (e.g. 2.3, 3.0): ",
        "thickness":"What is the thickness of the element in meters? (e.g. 0.01, 0.03): "
        }
    keys_cal = ["length", "height", "thickness"]
    
    # Define a dictionary called building_elements
    building_elements = {}
    
    id = 0
    while True:
        try:
            if id == 0:
                # The initial stage for managing this building information modeling tool
                print(message_dict["init"])
                building_elements[f"MA_{id:0>5}"] = add_element(message_dict)
                id += 1
            else:
                # Choose action from options(1-4)
                num = int(input_format_string(message_dict["continue"], str))
                
                if num == 1:
                    # Add elements in the dictionary
                    building_elements[f"MA_{id:0>5}"] = add_element(message_dict)
                    id += 1
                    
                elif num == 2:
                    # show every element in the dictionary
                    show_db(building_elements)
                    
                elif num == 3:
                    # Calculate area and volume of a building element
                    while True:
                        try:
                            id_num = input_format_string(message_dict["analysis"], str)
                            ele_dict = building_elements[id_num]
                            break
                        except KeyError:
                            print("-----Please select the id in the building element dictionary-----")
                            continue
                        
                    area = calculate_area(*[ele_dict[key] for key in keys_cal[:2]] )
                    volume = calculate_volume(*[ele_dict[key] for key in keys_cal])
                    print(f"{"-"*120}\nID:{id_num} Area: {area:,.2f}m2, Volume: {volume:,.2f}m3\n{"-"*120}")
                
                elif num == 4:
                    # Create a list of keys for all building elements of the specific type
                    selected_type = input_format_string(message_dict["get_eles"], str)
                    keys_ls = get_elements_by_type(building_elements, selected_type)
                    print(f"{"-"*120}\nIDs: ", *keys_ls, f"\n{"-"*120}")
                    
        except StopIteration:
            break



def add_element(message_dict):
    
    items_dict = {}
    items_dict["type"] = input_format_string(message_dict["type"], str).lower()
    items_dict["room"] = input_format_string(message_dict["room"], str).lower()
    items_dict["length"] = input_format_string(message_dict["length"], float)
    items_dict["height"] = input_format_string(message_dict["height"], float)
    items_dict["thickness"] = input_format_string(message_dict["thickness"], float)
    
    return items_dict


def calculate_area(height, thickness):
    
    return height*thickness


def calculate_volume(length, height, thickness):
    
    return length*height*thickness

        
def get_elements_by_type(db, selected_type):
    
    keys_ls = []
    
    for id in db:
        if db[f"{id}"]["type"] == selected_type:
            keys_ls.append(id)
    
    if not keys_ls:
        print(f"{selected_type} is not found in this database.") 
        
    return keys_ls


def show_db(db):
    
    print("-"*120)
    for id in db:
        text_db_items = ", ".join([f"ID: {id}"]+[": ".join([key, str(db[id][key])]) for key in db[id]])
        print(text_db_items)
    print("-"*120)


def input_format_string(message:str, format_func):
    
    while True:
        try:
            if format_func == str:
                value = input(message).strip(" '/\\\"[]_-~:;,.")
                if value.lower() == "q":
                    raise StopIteration
            else:
                value = format_func(input(message))
                
            return value
        
        except ValueError:
            if format_func == int:
                print("-----Please input an integer number-----")
            elif format_func == float:
                print("-----Please input a number-----")
            else:
                print("-----Please input any text-----")
 
    
    
if __name__ == "__main__":
    main()