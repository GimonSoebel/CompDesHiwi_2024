
# Generic Classes
class Material:
    def __init__(self, material, cost, carbon_footprint, material_weight):
        self.material = material
        self.cost = cost
        self.carbon_footprint = carbon_footprint
        self.material_weight = material_weight

# Dimensions Class
class Dimensions:
    def __init__(self, width=1, height=1, length=1):
        self.width = width
        self.height = height
        self.length = length
        self.volume = width * height * length

#-------------------------------------------------------------------------------------------------
# Main Pavilion Class
class Pavilion:
    def __init__(self):
        self.elements = []
    
    def add_element(self, element):
        self.elements.append(element)
    
    def get_all_items(self):
        return [element for element in self.elements]
    
    def delete_all_items(self):
        self.elements.clear()
        return "All elements deleted successfully."
    
    def calculate_totals(self):
        total_cost = sum(el.calculate_cost() for el in self.elements)
        total_carbon = sum(el.calculate_carbon_footprint() for el in self.elements)
        total_weight = sum(el.calculate_weight() for el in self.elements)
        return total_cost, total_carbon, total_weight

#-------------------------------------------------------------------------------------------------
# Parent Class
class Element:
    def __init__(self, material, dimensions, num_elements):
        self.name = self.__class__.__name__
        self.fab_method = "Default Method"
        self.material = material
        self.dimensions = dimensions
        self.num_elements = num_elements

    def calculate_cost(self):
        weight_of_element = self.dimensions.volume * self.material.material_weight
        return self.num_elements * weight_of_element * self.material.cost

    def calculate_carbon_footprint(self):
        weight_of_element = self.dimensions.volume * self.material.material_weight
        return self.num_elements * weight_of_element * self.material.carbon_footprint

    def calculate_weight(self):
        return self.num_elements * self.dimensions.volume * self.material.material_weight

#-------------------------------------------------------------------------------------------------
# Subclasses for Structural Elements
class Column(Element):
    def __init__(self, material, dimensions, num_elements):
        super().__init__(material, dimensions, num_elements)
        self.fab_method = "Casting and Extrusion"

class Segment(Column):
    def __init__(self, material, dimensions, num_elements):
        super().__init__(material, dimensions, num_elements)

class Winding(Segment):
    def __init__(self, material, dimensions, num_elements, turns):
        super().__init__(material, dimensions, num_elements)
        self.turns = turns
        self.fab_method = "3D-Printing and Winding"

class Latch(Segment):
    def __init__(self, material, dimensions, num_elements):
        super().__init__(material, dimensions, num_elements)
        self.fab_method = "Metal Punching and Extrusion"

#-------------------------------------------------------------------------------------------------
# Subclasses for Roof Elements
class Cladding(Element):
    def __init__(self, material, dimensions, num_elements):
        super().__init__(material, dimensions, num_elements)

class AcrylicTile(Cladding):
    def __init__(self, material, dimensions, num_elements):
        super().__init__(material, dimensions, num_elements)
        self.fab_method = "Casting"

class Rafter(Cladding):
    def __init__(self, material, dimensions, num_elements):
        super().__init__(material, dimensions, num_elements)
        self.fab_method = "Metal-Extrusion"

#-------------------------------------------------------------------------------------------------
# Subclasses for Foundation Elements
class Foundation(Element):
    def __init__(self, material, dimensions, num_elements):
        super().__init__(material, dimensions, num_elements)

class Concrete(Foundation):
    def __init__(self, material, dimensions, num_elements):
        super().__init__(material, dimensions, num_elements)
        self.fab_method = "In-situ Casting"

class Reinforcement(Foundation):
    def __init__(self, material, dimensions, num_elements):
        super().__init__(material, dimensions, num_elements)
        self.fab_method = "Metal-Extrusion"

class AnchorSupport(Foundation):
    def __init__(self, material, dimensions, num_elements):
        super().__init__(material, dimensions, num_elements)
        self.fab_method = "Cast Iron"

#-------------------------------------------------------------------------------------------------
# Predefined Materials
materials = [
    Material("Steel", cost=2, carbon_footprint=900, material_weight=1500),
    Material("Concrete", cost=0.2, carbon_footprint=2160, material_weight=2400),
    Material("Acrylic", cost=2, carbon_footprint=3300, material_weight=1180),
    Material("Flax fibre", cost=20, carbon_footprint=900, material_weight=1500),
]

# Function to check if input is a valid number (either integer or float)
def is_valid_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

#-------------------------------------------------------------------------------------------------
# Main menu with numeric input
def main_menu():
    pavilion = Pavilion()
    while True:
        print("\n" + "="*50)
        print("livMatS Pavillion Program")
        print("="*50)
        print("1. Create New Pavilion")
        print("2. Create Example Pavilion")  
        print("3. View and Edit Pavilion")  
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_pavilion(pavilion)
        elif choice == '2':
            create_example_pavilion(pavilion)
        elif choice == '3':
            view_and_edit_pavilion(pavilion)
        elif choice == '4':
            print("Exiting. Thank you for using my program!")
            break
        else:
            print("Invalid choice. Please try again.")
#---------------------------------------------------------------------------
# Create Example Pavilion
def create_example_pavilion(pavilion):
    print("\nCreating an example pavilion...")
    example_elements = [
        Winding(materials[3], Dimensions(1, 0.01, 0.01), 2000, turns=3),
        Concrete(materials[1], Dimensions(5, 1.5), 5),
        AcrylicTile(materials[2], Dimensions(1, 1, 0.05), 75),
        Rafter(materials[0], Dimensions(4, 0.05, 0.05), 50),
        Reinforcement(materials[0], Dimensions(0.1, 0.02, 0.02), 50),
        AnchorSupport(materials[0], Dimensions(0.3, 0.3, 0.3), 35),
        Latch(materials[0], Dimensions(0.02, 0.02, 0.01), 100)
    ]

    # Add example elements to the pavilion
    for el in example_elements:
        pavilion.add_element(el)
    print("Example pavilion created!")
    
# Pavilion Creation
def create_pavilion(pavilion):
    print("\nCreating a new pavilion...")
    subclasses = [Winding, Latch, AcrylicTile, Rafter, Concrete, Reinforcement, AnchorSupport]
    for cls in subclasses:
        print(f"\nCreating {cls.__name__} elements.")
        num_elements = input("Enter the number of elements (or 'c' to cancel): ")
        if num_elements.lower() == 'c':
            print("Creation cancelled.")
            return
        if not is_valid_number(num_elements) or float(num_elements) <= 0:
            print("Invalid input. Please enter a positive number.")
            continue
        num_elements = int(num_elements)
        width = input("Enter width: ")
        if not is_valid_number(width) or float(width) <= 0:
            print("Invalid input. Please enter a positive number for width.")
            continue
        height = input("Enter height: ")
        if not is_valid_number(height) or float(height) <= 0:
            print("Invalid input. Please enter a positive number for height.")
            continue
        length = input("Enter length: ")
        if not is_valid_number(length) or float(length) <= 0:
            print("Invalid input. Please enter a positive number for length.")
            continue

        dimensions = Dimensions(
            width=float(width),
            height=float(height),
            length=float(length)
        )
        print("Choose a material:")
        for i, mat in enumerate(materials): #enumerate is a built-in function. It iterates through a list while keeping track of the index 
            print(f"{i+1}. {mat.material}") # Showing all Material options
        mat_choice = int(input("Enter your choice: ")) - 1
        material = materials[mat_choice]

        if cls == Winding:
            turns = input("Enter the number of turns for Winding: ")
            if not is_valid_number(turns) or int(turns) <= 0:
                print("Invalid input. Please enter a positive integer for turns.")
                continue
            pavilion.add_element(cls(material, dimensions, num_elements, int(turns)))
        else:
            pavilion.add_element(cls(material, dimensions, num_elements))
    print("Pavilion creation complete!")

# View and Edit Pavilion
def view_and_edit_pavilion(pavilion):
    while True:
        print("\n" + "="*50)
        print("View and Edit Pavilion")
        print("="*50)
        print("1. Show All Elements")
        print("2. Edit Element")
        print("3. Delete All Elements")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            if not pavilion.elements:
                print("No elements to display.")
            else:
                unique_elements = set(el.__class__.__name__ for el in pavilion.get_all_items()) # get all component names 
                for i, element_name in enumerate(unique_elements):
                    print(f"{i+1}. {element_name}")
            print_totals(pavilion)
        elif choice == '2':
            edit_element(pavilion)
        elif choice == '3':
            pavilion.delete_all_items()
            print("All elements deleted successfully.")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

# Edit Element
def edit_element(pavilion):
    if not pavilion.elements:
        print("No elements to edit.")
        return
    print("\nSelect an element to edit:")
    for i, el in enumerate(pavilion.get_all_items()):
        print(f"{i+1}. {el.__class__.__name__}")
    choice = int(input("Enter your choice: ")) - 1
    if 0 <= choice < len(pavilion.elements):#checks if theres elements to edit
        element = pavilion.elements[choice]
        print("Editing element:", element.__class__.__name__)

        #change number of elements
        new_num_elements = input("Enter new number of elements: ")
        if not is_valid_number(new_num_elements) or float(new_num_elements) <= 0:
            print("Invalid input. Please enter a positive number.")
            return
        element.num_elements = int(new_num_elements)

        #change material
        print("Choose a new material:")
        for i, mat in enumerate(materials):
            print(f"{i+1}. {mat.material}")
        mat_choice = int(input("Enter your choice: ")) - 1
        element.material = materials[mat_choice]
        
        # chenge dimensions
        print("Enter new dimensions:")
        new_width = input("Width: ")
        if not is_valid_number(new_width) or float(new_width) <= 0:
            print("Invalid input. Please enter a positive number for width.")
            return
        new_height = input("Height: ")
        if not is_valid_number(new_height) or float(new_height) <= 0:
            print("Invalid input. Please enter a positive number for height.")
            return
        new_length = input("Length: ")
        if not is_valid_number(new_length) or float(new_length) <= 0:
            print("Invalid input. Please enter a positive number for length.")
            return
        element.dimensions = Dimensions(
            width=float(new_width),
            height=float(new_height),
            length=float(new_length)
        )

        print("Element updated successfully.")
    else:
        print("Invalid choice.")

# Displays information for total building
def print_totals(pavilion):
    total_cost, total_carbon, total_weight = pavilion.calculate_totals()
    print("\n" + "-"*50)
    print("Pavilion Totals")
    print("-"*50)
    print(f"Total Cost: €{total_cost:.2f}")
    print(f"Total Carbon Footprint: {total_carbon:.2f} kgCO2e")
    print(f"Total Weight: {total_weight:.2f} kg")
    print("-"*50)

# runs main menu function
main_menu()
