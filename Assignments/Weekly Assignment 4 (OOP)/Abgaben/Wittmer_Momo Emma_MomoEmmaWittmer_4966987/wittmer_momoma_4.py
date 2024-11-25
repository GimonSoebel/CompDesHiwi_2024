"""In this assignment, you will design a new pavilion inspired by an existing pavilion
 or project (it does not have to be an ITECH pavilion :D).

You will use object-oriented programming. The components of the pavilion 
(e.g. columns, beams, roofs, walls) will be modelled as classes and subclasses.
Each component will have parameters (such as dimensions, material type, fabrication methods) 
that can influence the overall cost and CO2 emissions of the pavilion.
In addition, cost estimates will be updated based on design decisions such as material selection or changes in dimensions.

1. Create the pavilion class. This is the main class that contains the components
 of the pavilion and provides methods for estimating the total cost, carbon footprint, etc. 
2. Component classes: Each major component (e.g. column, beam, wall) should have its own
 class that calculates its individual cost, carbon footprint, etc. 
3. Material subclasses: Materials will have different costs and properties that will affect those of the components. 
4. Be creative
5. Upload your assignment to ILIAS and GitHub"""

#class definitions

class Pavilion:
    def __init__(self, name, components):
        self.name = name
        self.components = components

    def calc_total_co2(self):
        a = 0
        for x in self.components:
            a = a + x.calc_co2_emissions()
        return(a)
            
    def calc_total_cost(self):
        b = 0
        for x in self.components:
            b = b + x.calc_cost()
        return(b)

    def calc_total_weight(self):
        c = 0
        for x in self.components:
            c = c + x.calc_weight()
        return(c)

    def number_of_components(self):
        d = 0
        for x in self.components:
            d = d + 1
        return(d)       

class Component:
    def __init__(self, name, volume, material):
        self.name = name
        self.volume = volume
        self.material = material

    def calc_co2_emissions(self):
        return(self.material.co2_intensity_factor * self.calc_weight())

    def calc_cost(self):
        return(self.calc_weight() * self.material.cost_intensity_eur_per_kg)

    def calc_weight(self):
        return(self.material.density_kg_per_m3 * self.volume)

class Wall(Component):
    pass

class Column(Component):
    pass

class Slab(Component):
    pass
  
class Material:
    def __init__(self, name, density, co2_intensity, cost_intensity):
        self.name = name
        self.density_kg_per_m3 = density
        self.co2_intensity_factor = co2_intensity
        self.cost_intensity_eur_per_kg = cost_intensity


#actually using the classes by making all the objects

conc1 = Material("concrete", 2400, 0.18, 0.05)
wood1 = Material("wood", 600, -0.5, 0.38)
steel1 = Material("steel", 7850, 0.8, 1)

wall1 = Wall("w1", 5, wood1)
wall2 = Wall("w2", 6, wood1)
wall3 = Wall("w3", 2, wood1)
wall4 = Wall("w4", 4, wood1)

column1 = Column("c1", 1, steel1)
column2 = Column("c2", 1, steel1)
column3 = Column("c3", 1, steel1)
column4 = Column("c4", 1, steel1)

slab1 = Slab("s1", 12, conc1)
slab2 = Slab("s2", 10, conc1)

all_components = [wall1, wall2, wall3, wall4, column1, column2, column3, column4, slab1, slab2]

my_pavilion = Pavilion("Housy McHouseface", all_components)

#TESTING

print(f"{my_pavilion.name} consists of {my_pavilion.number_of_components()} individual components,")
print(f"has a total CO2 footprint of {my_pavilion.calc_total_co2()} kg")
print(f"and costs {my_pavilion.calc_total_cost()} €")
print(f"at a total weight of {my_pavilion.calc_total_weight()} kg")