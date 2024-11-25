"""In this assignment, you will design a new pavilion inspired by an existing pavilion or project (it does not have to be an ITECH pavilion :D).

You will use object-oriented programming. The components of the pavilion (e.g. columns, beams, roofs, walls) will be modelled as classes and subclasses.
Each component will have parameters (such as dimensions, material type, fabrication methods) that can influence the overall cost and CO2 emissions of the pavilion.
In addition, cost estimates will be updated based on design decisions such as material selection or changes in dimensions.

1. Create the pavilion class. This is the main class that contains the components of the pavilion and provides methods for estimating the total cost, carbon footprint, etc. 
2. Component classes: Each major component (e.g. column, beam, wall) should have its own class that calculates its individual cost, carbon footprint, etc. 
3. Material subclasses: Materials will have different costs and properties that will affect those of the components. 
4. Be creative
5. Upload your assignment to ILIAS and GitHub"""

# Material Class
class Material:
    def __init__(self, name, cost_per_unit, co2_per_unit, reusable):
        self.name = name
        self.cost_per_unit = cost_per_unit
        self.co2_per_unit = co2_per_unit
        self.reusable = reusable


# Specific Materials
class FrenchPine(Material):
    def __init__(self):
        super().__init__("French Pine", 12, 4, True)


class CLT(Material):
    def __init__(self):
        super().__init__("CLT", 25, 8, True)


# Component Class
class Component:
    def __init__(self, name, material, dimensions, fabrication_method):
        self.name = name
        self.material = material
        self.dimensions = dimensions  # [length, width, height]
        self.fabrication_method = fabrication_method

    def calculate_volume(self):
        return self.dimensions[0] * self.dimensions[1] * self.dimensions[2]

    def calculate_cost(self):
        fabrication_multiplier = 1.2 if self.fabrication_method == "machine_cut" else 1.0
        return self.calculate_volume() * self.material.cost_per_unit * fabrication_multiplier

    def calculate_co2(self):
        fabrication_multiplier = 1.3 if self.fabrication_method == "machine_cut" else 1.0
        return self.calculate_volume() * self.material.co2_per_unit * fabrication_multiplier


# Specific Components
class Pole(Component):
    def __init__(self, material, length, diameter, fabrication_method):
        super().__init__("Pole", material, [length, diameter / 2, diameter / 2], fabrication_method)


class Floor(Component):
    def __init__(self, material, length, width, thickness, fabrication_method):
        super().__init__("Floor", material, [length, width, thickness], fabrication_method)


# Pavilion Class
class Pavilion:
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def calculate_total_cost(self):
        return sum([c.calculate_cost() for c in self.components])

    def calculate_total_co2(self):
        return sum([c.calculate_co2() for c in self.components])

    def is_reusable(self):
        return all(c.material.reusable for c in self.components)


# Example: Build the Pavilion
if __name__ == "__main__":
    # Pavilion Initialization
    pavilion = Pavilion()

    # Materials
    french_pine = FrenchPine()
    clt = CLT()

    # Add 200 Poles
    for _ in range(200):
        pole = Pole(french_pine, length=3, diameter=0.1, fabrication_method="machine_cut")
        pavilion.add_component(pole)

    # Add CLT Floor
    floor = Floor(clt, length=10, width=5, thickness=0.2, fabrication_method="machine_cut")
    pavilion.add_component(floor)

    # Output Results
    print("Pavilion Details:")
    print(f"Total Cost: ${pavilion.calculate_total_cost():.2f}")
    print(f"Total CO2 Emissions: {pavilion.calculate_total_co2():.2f} kg")
    print(f"Reusable Pavilion: {'Yes' if pavilion.is_reusable() else 'No'}")
