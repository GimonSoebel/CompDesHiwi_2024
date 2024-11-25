class Material:
    def __init__(self, name, cost_per_unit, carbon_per_unit):
        self.name = name
        self.cost_per_unit = cost_per_unit  # cost per cubic meter (or other relevant unit)
        self.carbon_per_unit = carbon_per_unit  # CO2 emissions per unit

class Component:
    def __init__(self, material, dimensions):
        self.material = material  # Instance of Material class
        self.dimensions = dimensions  # dimensions as a dictionary 

    def calculate_volume(self):
        # Override this method in subclasses to calculate the correct volume
        raise NotImplementedError("Please implement this method in the subclass.")

    def calculate_cost(self):
        volume = self.calculate_volume()
        return volume * self.material.cost_per_unit

    def calculate_carbon_footprint(self):
        volume = self.calculate_volume()
        return volume * self.material.carbon_per_unit

class Column(Component):
    def __init__(self, material, height, diameter):
        super().__init__(material, {'height': height, 'diameter': diameter})

    def calculate_volume(self):
        # Volume of a cylinder: π * r² * h
        import math
        radius = self.dimensions['diameter'] / 2
        return math.pi * (radius ** 2) * self.dimensions['height']

class Beam(Component):
    def __init__(self, material, length, width, height):
        super().__init__(material, {'length': length, 'width': width, 'height': height})

    def calculate_volume(self):
        # Volume of a rectangular prism: l * w * h
        return self.dimensions['length'] * self.dimensions['width'] * self.dimensions['height']

class Wall(Component):
    def __init__(self, material, length, height, thickness):
        super().__init__(material, {'length': length, 'height': height, 'thickness': thickness})

    def calculate_volume(self):
        # Volume of a rectangular prism: l * h * t
        return self.dimensions['length'] * self.dimensions['height'] * self.dimensions['thickness']

class Pavilion:
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def estimate_total_cost(self):
        total_cost = sum(component.calculate_cost() for component in self.components)
        return total_cost

    def estimate_total_carbon_footprint(self):
        total_carbon = sum(component.calculate_carbon_footprint() for component in self.components)
        return total_carbon

# Example material classes
class Wood(Material):
    def __init__(self):
        super().__init__(name="Wood", cost_per_unit=300, carbon_per_unit=0.1)

class Steel(Material):
    def __init__(self):
        super().__init__(name="Steel", cost_per_unit=700, carbon_per_unit=1.0)

class Concrete(Material):
    def __init__(self):
        super().__init__(name="Concrete", cost_per_unit=200, carbon_per_unit=0.15)

# Example usage of the classes
if __name__ == "__main__":
    pavilion = Pavilion()

    # Create materials
    wood = Wood()
    steel = Steel()
    concrete = Concrete()

    # Add components to the pavilion
    pavilion.add_component(Column(material=steel, height=3, diameter=0.3))
    pavilion.add_component(Beam(material=wood, length=6, width=0.15, height=0.3))
    pavilion.add_component(Wall(material=concrete, length=4, height=3, thickness=0.2))

    # Estimate total cost and carbon footprint
    total_cost = pavilion.estimate_total_cost()
    total_carbon_footprint = pavilion.estimate_total_carbon_footprint()

    print(f"Total Cost of Pavilion: ${total_cost:.2f}")
    print(f"Total Carbon Footprint of Pavilion: {total_carbon_footprint:.2f} tons CO2")