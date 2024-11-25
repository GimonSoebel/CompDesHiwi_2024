"""In this assignment, you will design a new pavilion inspired by an existing pavilion or project (it does not have to be an ITECH pavilion :D).

You will use object-oriented programming. The components of the pavilion (e.g. columns, beams, roofs, walls) will be modelled as classes and subclasses.
Each component will have parameters (such as dimensions, material type, fabrication methods) that can influence the overall cost and CO2 emissions of the pavilion.
In addition, cost estimates will be updated based on design decisions such as material selection or changes in dimensions.

1. Create the pavilion class. This is the main class that contains the components of the pavilion and provides methods for estimating the total cost, carbon footprint, etc. 
2. Component classes: Each major component (e.g. column, beam, wall) should have its own class that calculates its individual cost, carbon footprint, etc. 
3. Material subclasses: Materials will have different costs and properties that will affect those of the components. 
4. Be creative
5. Upload your assignment to ILIAS and GitHub"""

# Define Material Classes
class Material:
    def __init__(self, name, cost_per_unit, co2_per_unit):
        self.name = name
        self.cost_per_unit = cost_per_unit  # Cost in €/m³
        self.co2_per_unit = co2_per_unit  # CO2 emissions in kg/m³


class Concrete(Material):
    pass


class Wood(Material):
    pass


class Steel(Material):
    pass


# Define Component Classes
class Component:
    def __init__(self, name, material, dimensions):
        self.name = name
        self.material = material
        self.dimensions = dimensions 
        
    def calculate_cost(self):
        volume = self.dimensions['length'] * self.dimensions['width'] * self.dimensions['height']
        return volume * self.material.cost_per_unit

    def calculate_co2(self):
        volume = self.dimensions['length'] * self.dimensions['width'] * self.dimensions['height']
        return volume * self.material.co2_per_unit

    def __str__(self):
        return f"{self.name} made of {self.material.name}"


class Column(Component):
    pass


class Beam(Component):
    pass


# Define Pavilion Class
class Pavilion:
    def __init__(self, name):
        self.name = name
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def calculate_total_cost(self):
        return sum(component.calculate_cost() for component in self.components)

    def calculate_total_co2(self):
        return sum(component.calculate_co2() for component in self.components)

    def __str__(self):
        return f"Pavilion '{self.name}' with {len(self.components)} components."


# Main Program Logic
def main():
    # Get Pavilion Details from the User
    pavilion_name = input("Enter the name of the pavilion: ")
    area_to_cover = float(input("Enter the total area to be covered by the pavilion (in square meters): "))
    num_columns = int(input("Enter the number of columns required: "))
    num_beams = int(input("Enter the number of beams required: "))

    # Create Pavilion
    pavilion = Pavilion(pavilion_name)

    # Choose Material for Components
    print("\nChoose material for components:")
    print("1. Concrete (€100/m³, 100 kg CO2/m³)")
    print("2. Wood (€500/m³, 10 kg CO2/m³)")
    print("3. Steel (€2000/m³, 2000 kg CO2/m³)")
    material_choice = int(input("Enter your choice (1, 2, or 3): "))

    if material_choice == 1:
        material = Concrete(name="Concrete", cost_per_unit=100, co2_per_unit=100)
    elif material_choice == 2:
        material = Wood(name="Wood", cost_per_unit=500, co2_per_unit=10)
    elif material_choice == 3:
        material = Steel(name="Steel", cost_per_unit=2000, co2_per_unit=2000)
    else:
        print("Invalid choice! Defaulting to Concrete.")
        material = Concrete(name="Concrete", cost_per_unit=100, co2_per_unit=100)

    # Define Dimensions for Columns and Beams
    column_height = 3.0  # meters
    column_base_area = area_to_cover / (num_columns * 10)3
    beam_length = (area_to_cover / num_beams) ** 0.5
    beam_width = 0.3  # meters
    beam_height = 0.2  # meters

    # Create and Add Columns to Pavilion
    for i in range(num_columns):
        column = Column(
            name=f"Column {i + 1}",
            material=material,
            dimensions={'length': column_base_area ** 0.5, 'width': column_base_area ** 0.5, 'height': column_height}
        )
        pavilion.add_component(column)

    # Create and Add Beams to Pavilion
    for i in range(num_beams):
        beam = Beam(
            name=f"Beam {i + 1}",
            material=material,
            dimensions={'length': beam_length, 'width': beam_width, 'height': beam_height}
        )
        pavilion.add_component(beam)

    # Display Results
    print("\nPavilion Summary:")
    print(pavilion)
    print(f"Total Cost: €{pavilion.calculate_total_cost():,.2f}")
    print(f"Total CO2 Emissions: {pavilion.calculate_total_co2():,.2f} kg")


if __name__ == "__main__":
    main()
