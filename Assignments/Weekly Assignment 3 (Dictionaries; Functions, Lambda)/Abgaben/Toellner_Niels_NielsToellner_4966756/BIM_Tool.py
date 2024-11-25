# global variable 

catalogue = {}
matching_keys = []

while True:
    while True:

        # bim tool

        # definitions
        # add_element
        def add_element():
    
            print("--- ELEMENT EDITOR ---\n")
            key = input("Please give a new unique Key like (ELMNT-001): ")
            type = input("Please give an Element type like (wall or window): ")
            room = input("Please give the Element Room like (living room): ")
            length = float(input("Please give the Element's length in m like (2.0): "))
            height = float(input("Please give the Element's height in m like (2.0): "))
            thickness = float(input("Please give the Element's thickness in m like (2.0): "))
            
            print("\n- - - - - - - - - - - - -\n")
            print("\n--- ELEMENT SAVED ---\n")
            print(f"- {key} -")
            print(f"Type: {type}")
            print(f"Room: {room}")
            print(f"Length: {length}")
            print(f"Height: {height}")
            print(f"Thickness: {thickness}")
            print("\n- - - - - - - - - - - - -\n")

            # save as dictionary
            
            catalogue[key] = {
                "Type": type,
                "Room": room,
                "Length (m)": length,
                "Height (m)": height,
                "Thickness (m)": thickness
            }

            return catalogue
        
        # print_catalogue
        def print_catalogue():
                print("--- CATALOGUE ---")
                for element, dimensions in catalogue.items():
                    print(f"\n{element}: ")
                    for dimension, value in dimensions.items():
                        print(f"  {dimension}: {value}")

        # area_calculator
        def area_calculator():
            print("\n--- AREA CALCULATOR ---\n")
            key = input("Please Input the Element-ID for Area calculation: ")
            length = catalogue[key]["Length (m)"]
            hight = catalogue[key]["Height (m)"]
            area = float(length) * float(hight)
            print(f"\n{key} has a Area of {area} m2.")

        # volume_calculator
        def volume_calculator():
            print("\n--- VOLUME CALCULATOR ---\n")
            key = input("Please Input the Element-ID for Volume calculation: ")
            length = catalogue[key]["Length (m)"]
            hight = catalogue[key]["Height (m)"]
            thickness = catalogue[key]["Thickness (m)"]
            volume = float(length) * float(hight) * float(thickness)
            print(f"\n{key} has a Volume of {volume} m3.")

        # find_keys_by_type
        def find_keys_by_type(nested_dict, target_type):
          for key, attributes in nested_dict.items():
            if attributes.get("type") == target_type:
                matching_keys.append(key)
                return matching_keys  
        

        print("\n\n--- B I M   T O O L ---")
        print("Welcome to BIM Tool!")
        print("Choose your next Step:")

        # define options

        print("\n1. Store new building part")
        print("\n2. Print Catalogue")
        print("\n3. Calculate Area & Volume by ID")
        print("\n4. Get Elements by Type\n")
        print("\n- - - - - - - - - - - - -\n")

        # call to action

        while True:
            try:
                # Ask for input and convert it to an integer
                user_input = int(input("\nNext step (1 - 4): "))
                
                # Check if the input is within the valid range
                if 1 <= user_input <= 5:
                    print("\n- - - - - - - - - - - - -\n")
                    break  # Exit the loop if input is valid
                else:
                    print("\nInvalid input. Number must be between 1 and 5.")

            except ValueError:
                # Handle the case where the input is not an integer
                print("\nInvalid input. Please enter a number.")

        # check input and start function 

        if user_input == 1: # add element function
            add_element()
            any = input("\ndone? press any key. ")

        elif user_input == 2: # print catalogue
            print_catalogue()
            print("\n- - - - - - - - - - - - -\n")
            any = input("\ndone? press any key. ")
        

        elif user_input == 3: # calculate area & volume
            area_calculator()
            print("\n- - - - - - - - - - - - -\n")
            volume_calculator()
            print("\n- - - - - - - - - - - - -\n")
            any = input("\ndone? press any key. ")



        elif user_input == 4: # get element by type
            print("\n--- KEY BY TYPE ---\n")
            target_type = input("Please give the target type: ")
            result = find_keys_by_type(catalogue, target_type)

            if result:
                print(f"You will find the type '{target_type}' in: {result}")
            else:
                print(f"The type '{target_type}' was not found.")
                print("\n- - - - - - - - - - - - -\n")
                any = input("\ndone? press any key. ")

        else:
            print("error")
