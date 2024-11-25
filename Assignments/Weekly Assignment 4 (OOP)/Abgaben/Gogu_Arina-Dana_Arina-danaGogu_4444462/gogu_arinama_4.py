"""In this assignment, you will design a new pavilion inspired by an existing pavilion or project (it does not have to be an ITECH pavilion :D).

You will use object-oriented programming. The components of the pavilion (e.g. columns, beams, roofs, walls) will be modelled as classes and subclasses.
Each component will have parameters (such as dimensions, material type, fabrication methods) that can influence the overall cost and CO2 emissions of the pavilion.
In addition, cost estimates will be updated based on design decisions such as material selection or changes in dimensions.

1. Create the pavilion class. This is the main class that contains the components of the pavilion and provides methods for estimating the total cost, carbon footprint, etc. 
2. Component classes: Each major component (e.g. column, beam, wall) should have its own class that calculates its individual cost, carbon footprint, etc. 
3. Material subclasses: Materials will have different costs and properties that will affect those of the components. 
4. Be creative
5. Upload your assignment to ILIAS and GitHub"""


# Task 3: Materials values
materials = { # Dictionary with the material data
    1: {'name': 'Concrete', 'density': 2400, 'cost_per_kg': 0.1, 'co2_per_kg': 0.9},  
    2: {'name': 'Wood', 'density': 600, 'cost_per_kg': 1.25, 'co2_per_kg': 0.03},   
    3: {'name': 'Steel', 'density': 7850, 'cost_per_kg': 1.2, 'co2_per_kg': 2.0},     
}

# Task 1: Pavilion class-contains everything
class Pavilion:
    def __init__(self): # __init__ (class constructor)
        self.list_of_components = []

    def add_component(self, new_component):
        self.list_of_components.append(new_component)

    def calculate_total_cost(self):
        return sum(component.calculate_cost() for component in self.list_of_components)

    def calculate_total_co2(self):
        return sum(component.calculate_co2_emissions() for component in self.list_of_components)

    def show_details(self): # Display components
        if not self.list_of_components:
            print("No components have been added yet.")
            return
        for item in self.list_of_components:
            print(item) 

# Task 2: Component class (column, beam, wall)
class Component:
    def __init__(self, name, dimensions, material_id):
        self.name = name
        self.dimensions = dimensions
        self.material_id = material_id
        self.material = materials[material_id]

    def calculate_volume(self):
        length, width, height = self.dimensions
        return length * width * height

    def calculate_weight(self):
        volume = self.calculate_volume()
        return volume * self.material['density']

    def calculate_cost(self):
        weight = self.calculate_weight()
        return weight * self.material['cost_per_kg']

    def calculate_co2_emissions(self):
        weight = self.calculate_weight()
        return weight * self.material['co2_per_kg']

    def __str__(self): # Show the values
        return (f"{self.name}: Dimensions: {self.dimensions}, Material: {self.material['name']}, "
                f"Cost: €{self.calculate_cost():.2f}, CO2: {self.calculate_co2_emissions():.2f} kg")

# main part
my_pavilion = Pavilion() # Instance of the Pavilion class
print("Welcome to the Pavilion Calculator!") 
# To make it more interactive - I create an user interface menu
while True:
    print("\nPavilion Calculator Menu")
    print("1. Add a Component")
    print("2. Show Pavilion Details")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter the component name (e.g., 'Column 1'): ")
        length = float(input("Enter the length (in meters): "))
        width = float(input("Enter the width (in meters): "))
        height = float(input("Enter the height (in meters): "))
        dimensions = (length, width, height)

        print("\nChoose Material:")
        print("1. Concrete")
        print("2. Wood")
        print("3. Steel")
        material_id = int(input("Enter the number corresponding to the material: "))

        input_component = Component(name, dimensions, material_id)
        my_pavilion.add_component(input_component)
        print(f"{name} added successfully!")

    elif choice == "2":
        print("\nPavilion Details:")
        my_pavilion.show_details()

    elif choice == "3":
        print("Exiting the program. Goodbye!")
        exit()

    else:
        print("Invalid choice. Please try again.")
