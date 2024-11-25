
import random

# Initial dictionary of building elements
building_elements = {1: ("wall", "living room", 1.2, 2.7, 0.25)}


# Function to generate a unique ID for each new element
def generate_unique_key(existing_dict: dict[int, any], start=1, end=10000) -> int:
    while True:
        key = random.randint(start, end)
        if key not in existing_dict:
            return key


# Function to add a new element to the dictionary
def add_element():
    print("\nAdding a new element.")
    input_type = input("Enter the type of element (e.g., wall, door): ")
    input_room = input("Enter the room where this element is located (e.g., living room): ")
    input_length = input("Enter the length of the element in meters: ")
    input_height = input("Enter the height of the element in meters: ")
    input_thickness = input("Enter the thickness of the element in meters: ")

    input_id = generate_unique_key(building_elements)
    building_elements[input_id] = (
        input_type, input_room, float(input_length), float(input_height), float(input_thickness))

    print(f"\nElement added successfully with ID {input_id}: {building_elements[input_id]}\n")


# Function to calculate the area of an element
def calculate_area(key: int) -> float:
    if key in building_elements:
        area = building_elements[key][2] * building_elements[key][3]
        print(f"The area of element ID {key} is {area} square meters.")
        return area
    else:
        print(f"Element with ID {key} was not found.")
        return Null


# Function to calculate the volume of an element
def calculate_volume(key: int) -> float:
    if key in building_elements:
        volume = building_elements[key][2] * building_elements[key][3] * building_elements[key][4]
        print(f"The volume of element ID {key} is {volume} cubic meters.")
        return volume
    else:
        print(f"Element with ID {key} was not found.")
        return Null


# Function to find elements by type
def get_elements_by_type(element_type: str) -> list:
    found_element_keys = [
        key for key in building_elements if building_elements[key][0].lower() == element_type.lower()
    ]

    if found_element_keys:
        print(f"Found elements of type '{element_type}': {found_element_keys}")
    else:
        print(f"No elements of type '{element_type}' found.")
    return found_element_keys


# Main menu function
def main_menu():
    while True:
        print("\nWhat would you like to do next?")
        print("1. Add a new element")
        print("2. Calculate the area of an element")
        print("3. Calculate the volume of an element")
        print("4. Search for elements by type")
        print("5. View all elements")
        print("6. Exit")

        choice = input("Enter the number of your choice: ").strip()

        if choice == '1':
            add_element()
        elif choice == '2':
            element_id = int(input("Enter the ID of the element you want to calculate the area for: "))
            calculate_area(element_id)
        elif choice == '3':
            element_id = int(input("Enter the ID of the element you want to calculate the volume for: "))
            calculate_volume(element_id)
        elif choice == '4':
            element_type = input("Enter the type of element you want to search for (e.g., wall, door): ")
            get_elements_by_type(element_type)
        elif choice == '5':
            print("\nCurrent list of building elements:")
            for key, details in building_elements.items():
                print(
                    f"ID {key}: Type={details[0]}, Room={details[1]}, Length={details[2]}m, Height={details[3]}m,"
                    f" Thickness={details[4]}m")
        elif choice == '6':
            print("Exiting the Building Elements Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


# Start the program
print("Welcome to the Building Information Manager!\n")
main_menu()
