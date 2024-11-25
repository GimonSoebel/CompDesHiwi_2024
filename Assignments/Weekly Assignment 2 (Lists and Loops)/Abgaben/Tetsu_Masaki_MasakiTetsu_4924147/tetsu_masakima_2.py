import random

def main():
    
    # parameters
    db_size = 30
    
    # types of properties
    type_pros = ["Building element type", "Room", "Material", "Length", "Height"]
    # Available building element types
    b_ele_type_l = {"wall", "window", "door", "stair", "ceiling", "column", "beam", "slab"}
    # Available materials
    material_l = ("graphene", "concrete", "glass", "steel", "wood", "reclaimed wood", "recycled Plastics")
    # Available room types
    room_type_l = ["living room", "staircase", "drawing room", "kitchen",
                    "dining room", "bedroom", "bathroom and toilet", "study room",
                    "guest room", "office room", "store room", "Verandah"]
    # length and height options
    length_l = [i/5 for i in range(5, 20)]
    height_l = [i/5 for i in range(5, 20)]
    
    # define a Building Element Database and input data into the database 
    ele_db = [("window", room_type_l[4], material_l[2], length_l[3], length_l[4]),
              ("stair", room_type_l[7], material_l[5], length_l[10], length_l[6]),
              ("column", room_type_l[1], material_l[3], None, length_l[12])]
    ele_db.append(("door", room_type_l[-1], material_l[6], length_l[5], length_l[3]))
    ele_db.extend([("ceiling", room_type_l[-3], material_l[6], length_l[5], length_l[3])])
    # input data into the database with a for loop
    i = 0
    while True:
        for b_ele in b_ele_type_l:
            room_type = random.choice(room_type_l)
            ele_mat = random.choice(material_l)
            ran_num = random.random()
            if ran_num > 0.1:
                length = random.choice(length_l)
                height = random.choice(height_l)
            elif ran_num > 0.05:
                length = random.choice(length_l)
                height = None
            else:
                length = None
                height = None
            data = (b_ele, room_type, ele_mat, length, height)
            ele_db.append(data)
            i += 1
            if i >= db_size-3:
                break
        if i >= db_size-3:
            break
            
    
    # print each element in the database and do calculation for finding the 3 longest elements
    ele_len = []
    for i, v in enumerate(ele_db):
        display_text = create_print_elements(v, i, type_pros)
        print(display_text)
        ele_len.append(len(display_text) - len(str(i)))
    
    num_eles_db = len(ele_db)
    
    # print the amount of elements
    print(f"\nThe amount of elements of database: {len(ele_db)}\n")
    
    # Check that one of your Data structures contains at least 5 different options or properties and communicate it
    while True:
        num_id = input_format_string(f"Which element's ID would you like to check to see if it has at least five different properties? (ID options: 0 to {num_eles_db-1}): ", int)
        if num_id < num_eles_db:
            break
        print("-----the selected number is out of range-----")
    
    num_items = len([v for v in ele_db[num_id] if v != None])
    if num_items < 5:
        print(f"No, ID {num_id} element has only {num_items} different properties.\n")
    else:
        print(f"Yes, ID {num_id} element has {num_items} different properties.\n")
    
    # Ask one specific property of one specific element and communicate its location on the list
    while True:
        num_id = input_format_string(f"Which element's ID would you like to see? (ID options: 0 to {num_eles_db-1}): ", int)
        if num_id < num_eles_db:
            break
        print("-----the selected number is out of range-----")
    
    options_text = ", ".join([f"{i}: {v}" for i, v in enumerate(type_pros)])
    
    while True:
        num_prop = input_format_string(f"Which property would you like to see in the element with ID {num_id}?\n"\
            f"**Options:\n   {options_text}\n"\
                "Please choose the number from the above options: ", int
                )
        if num_prop < len(type_pros):
            display_text = f"ID {num_id}, {type_pros[num_prop]}: {ele_db[num_id][num_prop]}"
            break
        print("-----the selected number is out of range-----")
        
    # print the chosen specific property of the chosen specific element
    print(display_text)
    
    
    # Create the sorted index list for the list of length of the elements
    id_sort_ele_len = [i[0] for i in sorted(enumerate(ele_len), key=lambda x:x[1], reverse=True)]
    
    # Print the 3 longest elements
    print("The three longest element data")
    for i in id_sort_ele_len[:3]:
        display_text = create_print_elements(ele_db[i], i, type_pros)
        print(display_text)
        


def create_print_elements(data, num_id, type_pros):
    
    id_str = f"ID:{num_id}"
    display_text_l = [":".join([v0, str(v1)]) for v0, v1 in zip(type_pros, data) if v1 != None]
    display_text = ", ".join([id_str, *display_text_l])
    
    return display_text


def input_format_string(message:str, format_func):
    
    while True:
        try:
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