import random as rd

# Material Classes
class Material:
    def __init__(self, name, unit_price, fabrication_method, co2_emission):
        self.name = name
        self.unit_price = unit_price
        self.fabrication_method = fabrication_method
        self.co2_emission = co2_emission

    def unit_cost(self):
        return self.unit_price

    def unit_emission(self):
        return self.co2_emission

    def __str__(self):
        return (f"Material: {self.name}, Unit Cost: {self.unit_cost():.2f}, "
                f"Fabrication Method: {self.fabrication_method}, "
                f"Unit CO2 Emission: {self.unit_emission():.2f}")


# Component Classes
class Component:
    def __init__(self, name, base_area, height, material):
        self.name = name
        self.base_area = base_area
        self.height = height
        self.material = material

        # Store original cost and emissions
        self.original_cost = self.material.unit_cost() * self.base_area * self.height
        self.original_emission = self.material.unit_emission() * self.base_area * self.height

        # Generate random reduction factors
        self.cost_reduction_factor = round(rd.uniform(0.75, 0.85), 2)  # 75% to 85% of original cost
        self.emission_reduction_factor = round(rd.uniform(0.55, 0.65), 2)  # 55% to 65% of original emission

    def calculate_cost(self):
        # Apply a random cost reduction
        return self.original_cost * self.cost_reduction_factor

    def calculate_emission(self):
        # Apply a random emission reduction
        return self.original_emission * self.emission_reduction_factor

    def cost_reduction_percent(self):
        return ((self.original_cost - self.calculate_cost()) / self.original_cost) * 100

    def emission_reduction_percent(self):
        return ((self.original_emission - self.calculate_emission()) / self.original_emission) * 100

    def __str__(self):
        return (f"Component: {self.name}, Original Cost: {self.original_cost:.2f}, "
                f"Original Emission: {self.original_emission:.2f}, "
                f"Reduced Cost: {self.calculate_cost():.2f} "
                f"(-{self.cost_reduction_percent():.2f}%), "
                f"Reduced Emission: {self.calculate_emission():.2f} "
                f"(-{self.emission_reduction_percent():.2f}%)")


class Roof(Component):
    pass


class Column(Component):
    pass


class Frames(Component):
    pass


class Pavilion:
    def __init__(self, project_name, components):
        self.project_name = project_name
        self.components = components

    def total_original_cost(self):
        return sum(component.original_cost for component in self.components)

    def total_original_emission(self):
        return sum(component.original_emission for component in self.components)

    def total_reduced_cost(self):
        return sum(component.calculate_cost() for component in self.components)

    def total_reduced_emission(self):
        return sum(component.calculate_emission() for component in self.components)

    def cost_reduction_percent(self):
        return ((self.total_original_cost() - self.total_reduced_cost()) / self.total_original_cost()) * 100

    def emission_reduction_percent(self):
        return ((self.total_original_emission() - self.total_reduced_emission()) / self.total_original_emission()) * 100

    def __str__(self):
        original_cost = self.total_original_cost()
        original_emission = self.total_original_emission()
        reduced_cost = self.total_reduced_cost()
        reduced_emission = self.total_reduced_emission()

        cost_savings = original_cost - reduced_cost
        emission_savings = original_emission - reduced_emission

        return (f"Pavilion: {self.project_name}\n"
                f"Total Original Cost: {original_cost:.2f}, Total Reduced Cost: {reduced_cost:.2f}, "
                f"Cost Savings: {cost_savings:.2f} (-{self.cost_reduction_percent():.2f}%)\n"
                f"Total Original Emission: {original_emission:.2f}, Total Reduced Emission: {reduced_emission:.2f}, "
                f"Emission Savings: {emission_savings:.2f} (-{self.emission_reduction_percent():.2f}%)")


# Main Program
if __name__ == "__main__":
    print("Instantiating Materials:")
    timber = Material("ReclaimedTimber", 80, "Recycled", 30)
    print(timber)
    print()

    print("Instantiating Components:")
    components = []

    # Roof
    roof1 = Roof("Roof1", 8, 0.3, timber)
    components.append(roof1)

    # Columns
    for i in range(3):
        column = Column(f"Column{i}", 0.3, round(rd.uniform(3, 4), 2), timber)
        components.append(column)

    # Frames
    for j in range(8):
        frame = Frames(f"Frame{j}", 0.2, round(rd.uniform(0.8, 1.5), 2), timber)
        components.append(frame)

    # Print all components
    for component in components:
        print(component)

    print()
    print("Instantiating Pavilion:")
    pavilion = Pavilion("Reclaimed Timber Pavilion", components)
    print(pavilion)
