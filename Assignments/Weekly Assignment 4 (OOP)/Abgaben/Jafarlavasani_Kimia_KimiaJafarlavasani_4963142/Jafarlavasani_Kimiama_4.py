"""In this assignment, you will design a new pavilion inspired by an existing pavilion or project (it does not have to be an ITECH pavilion :D).

You will use object-oriented programming. The components of the pavilion (e.g. columns, beams, roofs, walls) will be modelled as classes and subclasses.
Each component will have parameters (such as dimensions, material type, fabrication methods) that can influence the overall cost and CO2 emissions of the pavilion.
In addition, cost estimates will be updated based on design decisions such as material selection or changes in dimensions.

1. Create the pavilion class. This is the main class that contains the components of the pavilion and provides methods for estimating the total cost, carbon footprint, etc. 
2. Component classes: Each major component (e.g. column, beam, wall) should have its own class that calculates its individual cost, carbon footprint, etc. 
3. Material subclasses: Materials will have different costs and properties that will affect those of the components. 
4. Be creative
5. Upload your assignment to ILIAS and GitHub"""


#inspired by Austria’s pavilion in Dubai Expo-2020


# Material base class with fundamental attributes: price, fabrication, CO2 impact, and density
class BuildingMaterial:
    def __init__(self, name, price_per_unit, fabrication_method, co2_impact_per_unit, density):
        self.name = name
        self.price_per_unit = price_per_unit
        self.fabrication_method = fabrication_method
        self.co2_impact_per_unit = co2_impact_per_unit
        self.density = density

    # Method to return the material's unit price
    def get_unit_price(self):
        return self.price_per_unit

    # Method to return the material's CO2 impact per unit
    def get_co2_impact(self):
        return self.co2_impact_per_unit

    def __str__(self):
        return f"{self.name}, Price per unit: {self.price_per_unit}, Fabrication method: {self.fabrication_method}, CO2 emission per unit: {self.co2_impact_per_unit}"

# Concrete, used for structural elements like the cones
class ReinforcedConcrete(BuildingMaterial):
    def __init__(self, name, price_per_unit, fabrication_method, co2_impact_per_unit, density):
        super().__init__(name, price_per_unit, fabrication_method, co2_impact_per_unit, density)

    def get_unit_price(self):
        return self.price_per_unit * 1.4  # Adjusted for specific characteristics

    def get_co2_impact(self):
        return self.co2_impact_per_unit * 1.3  # Adjusted for CO2 per unit

# Clay plaster, used for finishes like walls
class ClayPlaster(BuildingMaterial):
    def __init__(self, name, price_per_unit, fabrication_method, co2_impact_per_unit, density):
        super().__init__(name, price_per_unit, fabrication_method, co2_impact_per_unit, density)

    def get_unit_price(self):
        return self.price_per_unit * 1.1  # Adjusted for finish material

    def get_co2_impact(self):
        return self.co2_impact_per_unit * 1.2  # Adjusted for CO2 impact per unit

# Initialize Materials

# Concrete Material for structural components
concrete = ReinforcedConcrete("Reinforced Concrete", 120, "Precast", 250, 2400)
print(f" First material is : {concrete}")

# Clay Plaster Material for finishes
clay_plaster = ClayPlaster("Clay Plaster", 65, "Manual Application", 30, 1800)
print(f" Second material is : {clay_plaster}")

# Components of the Pavilion

class StructuralElement:
    def __init__(self, name, base_area, height, material):
        self.name = name
        self.base_area = base_area
        self.height = height
        self.material = material

    # Calculate cost based on material, area, and height
    def calculate_cost(self):
        return self.material.get_unit_price() * self.base_area * self.height

    # Calculate carbon emission based on material, area, and height
    def calculate_carbon_emissions(self):
        return self.material.get_co2_impact() * self.base_area * self.height

    def __str__(self):
        return f"{self.name}: Cost = {round(self.calculate_cost(), 2)}, CO2 Emission = {round(self.calculate_carbon_emissions(), 2)}"

# Cone Tower Class, representing the unique conical structures
class ConeTower(StructuralElement):
    def __init__(self, name, base_area, height, material):
        super().__init__(name, base_area, height, material)

    # Cost calculation for cone towers with some added complexities
    def calculate_cost(self):
        return (self.material.get_unit_price() + 110) * self.base_area * self.height

# Roof as a separate component
class Roof(StructuralElement):
    def __init__(self, name, base_area, height, material):
        super().__init__(name, base_area, height, material)

    # Cost calculation for roof with special installation cost
    def calculate_cost(self):
        return (self.material.get_unit_price() + 80) * self.base_area * self.height

# Wall as a separate component
class Wall(StructuralElement):
    def __init__(self, name, base_area, height, material):
        super().__init__(name, base_area, height, material)

    def calculate_cost(self):
        return (self.material.get_unit_price() + 55) * self.base_area * self.height


# Instantiate Components for the Pavilion

# Creating a list to hold all components
project_components = []

# Cone Towers (5 towers, varying heights manually specified)
cone_tower_heights = [12.5, 13.0, 14.2, 15.0, 13.5]  # Heights ranging from 12m to 15m
for i, height in enumerate(cone_tower_heights):
    cone_tower = ConeTower(f"Cone Tower {i+1}", 8, height, concrete)
    project_components.append(cone_tower)
    print(cone_tower)

# Roof component (single roof with fixed height)
roof = Roof("Roof", 10, 0.3, clay_plaster)
project_components.append(roof)
print(roof)

# Wall components (4 walls with varying heights manually specified)
wall_heights = [3.5, 4.0, 3.2, 3.8]  # Heights ranging from 3m to 4m
for i, height in enumerate(wall_heights):
    wall = Wall(f"Wall {i+1}", 10, height, clay_plaster)
    project_components.append(wall)
    print(wall)


# Pavilion Class to Aggregate Components

class PavilionProject:
    def __init__(self, name, components):
        self.name = name
        self.components = components

    # Calculate total cost by summing individual component costs
    def calculate_total_cost(self):
        return sum(component.calculate_cost() for component in self.components)

    # Calculate total CO2 emissions by summing individual component emissions
    def calculate_total_carbon_emissions(self):
        return sum(component.calculate_carbon_emissions() for component in self.components)

    def __str__(self):
        return f"Pavilion: {self.name}, Total Cost = {round(self.calculate_total_cost(), 2)}, Total CO2 Emission = {round(self.calculate_total_carbon_emissions(), 2)}"


# Instantiate Pavilion Project

austria_pavilion = PavilionProject("Austria Pavilion - Expo 2020", project_components)
print(austria_pavilion)

