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
    def __init__(self, name, density, co2_intensity, cost_intensity):
  
        self.name = name
        self.density_kg_per_m3 = density
        self.co2_intensity_factor = co2_intensity
        self.cost_intensity_eur_per_kg = cost_intensity

    def __str__(self):
        #String representation of the material.
        return f"{self.name} (Density: {self.density_kg_per_m3} kg/m³, CO₂: {self.co2_intensity_factor} kg/kg, Cost: €{self.cost_intensity_eur_per_kg}/kg)"

# Component Class
class Component:
    def __init__(self, name, volume, material):

        self.name = name
        self.volume = volume
        self.material = material


    def calc_weight(self): #Calculating the weight of the component.
        
        return self.volume * self.material.density_kg_per_m3


    def calc_cost(self):  #Calculating the cost of the component.

        return self.calc_weight() * self.material.cost_intensity_eur_per_kg


    def calc_co2_emissions(self):  #Calculating the CO2 emissions of the component.
        
        return self.calc_weight() * self.material.co2_intensity_factor


    def __str__(self):  #String representation of the component.
        
        return f"{self.name} ({self.volume} m³, Material: {self.material.name})"

# Pavilion Class
class Pavilion:
    def __init__(self, name):
       
        self.name = name
        self.components = []
        self.total_cost = 0
        self.total_co2 = 0
        self.total_weight = 0


    def add_component(self, component):
        #Adds a component to the pavilion and updates totals

        self.components.append(component)
        self.total_cost += component.calc_cost()
        self.total_co2 += component.calc_co2_emissions()
        self.total_weight += component.calc_weight()

    def calc_total_cost(self):   #total cost of all components in the pavilion.
       
        return self.total_cost


    def calc_total_co2(self):  #total CO2 emissions of all components in the pavilion.
        
        return self.total_co2


    def calc_total_weight(self):  #total weight of all components in the pavilion.
        
        return self.total_weight


    def number_of_components(self):  #number of components in the pavilion.
        
        return len(self.components)

    def list_components(self):  #list of all components.
        
        return "\n".join(str(c) for c in self.components)



# Materials Used in BUGA Wood Pavilion
engineered_timber = Material("Engineered Timber", 600, -0.5, 0.6)  # Sustainable timber
glass = Material("Glass", 2500, 0.25, 1.0)                        # Transparent panels
steel_fasteners = Material("Steel Fasteners", 7850, 0.8, 2.0)     # Fastening materials
concrete_foundation = Material("Concrete", 2400, 0.18, 0.05)      # Foundation material
membrane = Material("Membrane", 1200, 0.1, 0.8)                  # Protective covering

# Components of BUGA Wood Pavilion
wood_roof = Component("Roof", 100, engineered_timber)             # 100 m³ of engineered timber for roof structure
glass_panels = Component("Glass Panels", 25, glass)               # 25 m³ of glass
steel_supports = Component("Steel Supports", 5, steel_fasteners)  # 5 m³ of steel fasteners
foundation = Component("Foundation", 50, concrete_foundation)     # 50 m³ of concrete for foundation
membrane_covering = Component("Membrane Covering", 20, membrane)  # 20 m³ of membrane for exterior

# Create Pavilion and Add Components
buga_pavilion = Pavilion("BUGA Wood Pavilion 2019")
buga_pavilion.add_component(wood_roof)
buga_pavilion.add_component(glass_panels)
buga_pavilion.add_component(steel_supports)
buga_pavilion.add_component(foundation)
buga_pavilion.add_component(membrane_covering)

# Display Pavilion Details
print(f"Pavilion Name: {buga_pavilion.name}")
print(f"Number of Components: {buga_pavilion.number_of_components()}")
print(f"Total Weight: {buga_pavilion.calc_total_weight():.2f} kg")
print(f"Total Cost: €{buga_pavilion.calc_total_cost():.2f}")
print(f"Total CO2 Emissions: {buga_pavilion.calc_total_co2():.2f} kg")
print("\n--- Components ---")
print(buga_pavilion.list_components())

