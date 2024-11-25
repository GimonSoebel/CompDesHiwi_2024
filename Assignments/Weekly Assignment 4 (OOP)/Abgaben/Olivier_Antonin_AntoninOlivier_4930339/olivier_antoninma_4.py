"""In this assignment, you will design a new pavilion inspired by an existing pavilion or project (it does not have to be an ITECH pavilion :D).

You will use object-oriented programming. The components of the pavilion (e.g. columns, beams, roofs, walls) will be modelled as classes and subclasses.
Each component will have parameters (such as dimensions, material type, fabrication methods) that can influence the overall cost and CO2 emissions of the pavilion.
In addition, cost estimates will be updated based on design decisions such as material selection or changes in dimensions.

1. Create the pavilion class. This is the main class that contains the components of the pavilion and provides methods for estimating the total cost, carbon footprint, etc. 
2. Component classes: Each major component (e.g. column, beam, wall) should have its own class that calculates its individual cost, carbon footprint, etc. 
3. Material subclasses: Materials will have different costs and properties that will affect those of the components. 
4. Be creative
5. Upload your assignment to ILIAS and GitHub"""

class pavilion:
    """ Creating the class pavilion"""
    def __init__(self, name, components):
        self.name = name
        self.components = components
    
    def CO2_emission(self):
        tot_CO2_emission = 0
        for x in self.components:
            tot_CO2_emission += x.calc_CO2_emission() # additioning the CO2 emission of each component
        return round(tot_CO2_emission,3)

    def cost(self):
        tot_cost = 0
        for x in self.components:
            tot_cost += x.calc_cost() # calculating the total cost
        return round(tot_cost,3)
    
    def __str__(self):
        component_details = "\n".join(str(c) for c in self.components)
        return (f"Pavilion: {self.name}\n"
                f"Components:\n{component_details}\n"
                f"{'='*30} CO2 Emission,Cost  {'='*30}\n"
                f"Total CO2 Emission: {self.CO2_emission()} kg CO2\n"
                f"Total Cost: {self.cost()} EUR")

class columns:
    def __init__(self, name, number, material, calcul_unit_value, method):
        self.name = name
        self.number = number
        self.material = material
        self.calcul_unit_value = calcul_unit_value
        self.calcul_unit = material.calcul_unit
        self.method = method
        
    def calc_cost(self):  
        return self.number * self.material.cost * self.calcul_unit_value

    def calc_CO2_emission(self): 
        return self.number * self.material.emission * self.calcul_unit_value

    def __str__(self):
        return (f"{'='*30} {self.name.upper()} {'='*30}\n"
                f"  Quantity: {self.number}\n"
                f"  Material: {self.material.name}\n"
                f"  Unit Value: {self.calcul_unit_value:.2f}\n"
                f"  Unit: {self.calcul_unit}\n"
                f"  Method: {self.method}")
    
class panels(columns):
    pass

class ossature(columns):
    pass

class structural_works(columns):
    pass
    
class material:
    def __init__(self, name, calcul_unit, cost, CO2_emission):
        self.name = name
        self.cost = cost
        self.emission = CO2_emission
        self.calcul_unit = calcul_unit

    def __str__(self):
        return (f"Cost = {self.cost} EUR/{self.calcul_unit}\n"
                f"Emission = {self.emission} kg CO2/{self.calcul_unit}")
       
# Materials
m1 = material("IPN 200", "lm", 100, 1.65 ) # 100 kg/lm for IPN200, 1.65 kgCO2/kg
m2 = material("double glazing", "m²", 190, 11.50)
m3 = material("steel struts", "lm", 10, 1.65)
m4 = material("concrete", "m³", 130, 300)
m5 = material("HEA 300", "lm", 280, 1.65 )
m6 = material("HA 32", "kg", 0.71, 1.65 )

# Components
c1 = columns("roof support", 6, m5, 4, "galvanised steel")
c2 = ossature("steel struts", 120, m3, 2.26, "bolted struts" ) # hollow lattice cubes, 2.26m square
c3 = panels("glazing", 25, m2, 2.26**2, "")
c4 = panels("facade enamel plates", 34, m2, 2.26**2, "welded in factory")
c5 = structural_works("stairs(concrete)", 3, m4, 1.5, "wooden formwork")
c6 = structural_works("stairs(rebars)", 3, m6, 150, "concrete spacers")

# Pavilion
all_components= [c1,c2,c3,c4,c5,c6]
mon_pavilion = pavilion("Le Corbusier, Zurich", all_components)

print(mon_pavilion)

