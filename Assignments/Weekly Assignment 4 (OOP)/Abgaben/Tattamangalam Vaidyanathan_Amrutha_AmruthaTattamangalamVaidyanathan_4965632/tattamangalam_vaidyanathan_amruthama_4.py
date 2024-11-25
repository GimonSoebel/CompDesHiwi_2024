class Pavilion:
    """
    Main class representing the pavilion.
    Contains components such as columns, beams, roofs, and walls.
    """
    def __init__(self, name):
        self.name = name
        self.components = []  # List to hold components of the pavilion

    def add_component(self, component):
        self.components.append(component)

    def total_cost(self):
        return sum(component.cost for component in self.components)

    def total_carbon_footprint(self):
        return sum(component.carbon_footprint() for component in self.components)

    def display_summary(self):
        print(f"\n--- {self.name} ---")
        print(f"\nTotal Cost: ${self.total_cost():,.2f}")
        print(f"Total CO2 Emissions: {self.total_carbon_footprint():,.2f} kg")
        print("\n--- Components Summary ---")
        for component in self.components:
            print(f"  - {component.name}:")
            print(f"      Material: {component.material.name}")
            print(f"      Weight: {component.weight_kg} kg")
            print(f"      Cost: ${component.cost:.2f}")
            print(f"      CO2 Emissions: {component.carbon_footprint():.2f} kg")
            if isinstance(component, Wall):
                print(f"      Dimensions: {component.height_m}m (Height) x {component.width_m}m (Width)")
            elif isinstance(component, Roof):
                print(f"      Area: {component.area_m2} m²")
            print("")

class Material:
    """
    Represents a material used in a component.
    Attributes:
        name: Name of the material.
        cost_per_kg: Cost of the material per kg.
        co2_per_kg: CO2 emissions of the material per kg.
    """
    def __init__(self, name, cost_per_kg, co2_per_kg):
        self.name = name
        self.cost_per_kg = cost_per_kg
        self.co2_per_kg = co2_per_kg


class Component:
    """
    Base class for a pavilion component (e.g., column, beam, wall).
    """
    def __init__(self, name, material, weight_kg):
        self.name = name
        self.material = material
        self.weight_kg = weight_kg
        self.cost = self.material.cost_per_kg * self.weight_kg

    def carbon_footprint(self):
        return self.material.co2_per_kg * self.weight_kg


# Subclasses for specific components
class Column(Component):
    pass


class Beam(Component):
    pass


class Roof(Component):
    def __init__(self, name, material, weight_kg, area_m2):
        super().__init__(name, material, weight_kg)
        self.area_m2 = area_m2  # Additional attribute specific to roofs


class Wall(Component):
    def __init__(self, name, material, weight_kg, height_m, width_m):
        super().__init__(name, material, weight_kg)
        self.height_m = height_m
        self.width_m = width_m
        self.area_m2 = self.height_m * self.width_m


# Helper Functions for User Input Validation
def get_positive_float(prompt, error_message="Invalid input. Please enter a positive number."):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError(error_message)
            return value
        except ValueError as e:
            print(f"Error: {e}")


def get_non_negative_float(prompt, error_message="Invalid input. Please enter a non-negative number."):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError(error_message)
            return value
        except ValueError as e:
            print(f"Error: {e}")


# Function to create the sample pavilion
def create_sample_pavilion():
    fiberglass = Material("Fiberglass", cost_per_kg=4.0, co2_per_kg=2.0)
    steel = Material("Steel", cost_per_kg=5.0, co2_per_kg=1.8)

    pavilion = Pavilion("Serpentine Pavilion 2016")
    pavilion.add_component(Wall("Wall 1", fiberglass, weight_kg=800, height_m=3, width_m=10))
    pavilion.add_component(Wall("Wall 2", fiberglass, weight_kg=600, height_m=3, width_m=7))
    pavilion.add_component(Wall("Wall 3", fiberglass, weight_kg=700, height_m=3, width_m=9))
    pavilion.add_component(Roof("Roof 1", fiberglass, weight_kg=1000, area_m2=90))
    pavilion.add_component(Column("Column 1", steel, weight_kg=300))
    pavilion.add_component(Column("Column 2", steel, weight_kg=300))

    return pavilion


# Function to create a pavilion from user input
def create_pavilion_from_user_input():
    name = input("\nEnter the name of your pavilion: ")
    pavilion = Pavilion(name)

    while True:
        print("\n--- Adding a New Component ---")

        component_name = input("Enter the component name: ").strip()
        material_name = input("Enter the material name: ").strip()

        cost_per_kg = get_positive_float(f"Enter the cost per kg of {material_name}: ")
        co2_per_kg = get_non_negative_float(f"Enter the CO2 emissions per kg of {material_name}: ")
        weight_kg = get_positive_float("Enter the weight of the component in kg: ")

        material = Material(material_name, cost_per_kg, co2_per_kg)

        while True:
            component_type = input("Is this a Wall, Roof, Column, or Beam? ").strip().lower()
            if component_type in {"wall", "roof", "column", "beam"}:
                break
            else:
                print("Invalid component type. Please enter one of the following: Wall, Roof, Column, or Beam.")

        if component_type == "wall":
            height_m = get_positive_float("Enter the height of the wall in meters: ")
            width_m = get_positive_float("Enter the width of the wall in meters: ")
            pavilion.add_component(Wall(component_name, material, weight_kg, height_m, width_m))
        elif component_type == "roof":
            area_m2 = get_positive_float("Enter the area of the roof in square meters: ")
            pavilion.add_component(Roof(component_name, material, weight_kg, area_m2))
        elif component_type == "column":
            pavilion.add_component(Column(component_name, material, weight_kg))
        elif component_type == "beam":
            pavilion.add_component(Beam(component_name, material, weight_kg))

        continue_choice = input("\nDo you want to add another component? (y/n): ").strip().lower()
        if continue_choice != 'y':
            break

    return pavilion


# Main program
if __name__ == "__main__":
    # Sample pavilion display
    print("\n--- Sample Pavilion ---")
    sample_pavilion = create_sample_pavilion()
    sample_pavilion.display_summary()

    # User pavilion creation
    print("\n--- Create Your Pavilion ---")
    user_pavilion = create_pavilion_from_user_input()

    # Display user pavilion summary
    print("\n--- Your Pavilion Summary ---")
    user_pavilion.display_summary()
    
print("\n--- End of Program ---")