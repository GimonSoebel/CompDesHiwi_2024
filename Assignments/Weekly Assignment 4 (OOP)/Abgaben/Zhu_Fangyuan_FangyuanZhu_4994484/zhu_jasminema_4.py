"""In this assignment, you will design a new pavilion inspired by an existing pavilion or project (it does not have to be an ITECH pavilion :D).

You will use object-oriented programming. The components of the pavilion (e.g. columns, beams, roofs, walls) will be modelled as classes and subclasses.
Each component will have parameters (such as dimensions, material type, fabrication methods) that can influence the overall cost and CO2 emissions of the pavilion.
In addition, cost estimates will be updated based on design decisions such as material selection or changes in dimensions.

1. Create the pavilion class. This is the main class that contains the components of the pavilion and provides methods for estimating the total cost, carbon footprint, etc. 
2. Component classes: Each major component (e.g. column, beam, wall) should have its own class that calculates its individual cost, carbon footprint, etc. 
3. Material subclasses: Materials will have different costs and properties that will affect those of the components. 
4. Be creative
5. Upload your assignment to ILIAS and GitHub

Comment from Jasmine Zhu (author):
The following pavilion is based on the C Shore pavilion on UBC's campus. It is a reclaimed Western Red Cedar pavilion with a corrugated metal roof.
"""


class Pavilion:
    def __init__(self):
        self.components = []
        self.cost = 0
    def add_component(self,component):
        self.components.append(component)
    def calc_cost(self):
        totalcost = 0
        for comp in self.components:            #add comp_cost method for component class(es)
            totalcost += comp.comp_cost()
        return totalcost
    def calc_co2(self):
        totalcarbon = 0
        for comp in self.components:
            totalcarbon += comp.comp_co2()
        return totalcarbon

###########################################################

class Component:
    def __init__(self, material, length, width):
        self.material = material
        self.length = length
        self.width = width
    def co2_by_area(self):
        return self.length*self.width*self.material.co2

class Beam(Component):
    def __init__(self, material, length, width, depth):
        super().__init__(material, length, width)
        self.depth = depth
    def comp_cost(self):
        #volume-based cost
        return round(self.length*self.width*self.depth*self.material.cost, 2)
    def comp_co2(self):
        #volume-based co2 (kg)
        return round(super().co2_by_area()*self.depth, 2)

class Decking(Component):
    #area-based cost
    #flange and web define the profile of the decking (m)
    #length and width are the total dimensions of the deck (m)
    def __init__(self, material, length, width, flange, web):
        super().__init__(material, length, width)
        self.flange = flange
        self.web = web
        #give thickness of corrugated deck in mm
        self.thickness = 0.001 
    def comp_cost(self):
        #area-based cost
        return round(self.length*self.width*self.material.cost, 2)
    def comp_co2(self):
        #area-based co2 (kg)
        return round(super().co2_by_area(), 2)

# class Slab(Component):
#     def __init__(self, length, width, thickness, material):
#         super().__init__(material)
#         self.length = length
#         self.width = width
#         self.thickness = thickness

###########################################################

class Material:
    def __init__(self, density, cost, co2_intensity):
        self.density = density
        self.cost = cost
        self.co2 = co2_intensity

class RedCedar(Material):
    def __init__(self):
        super().__init__(density = 336, cost = 8000, co2_intensity = -590)      #cost per m^3, kg CO2 per m^3

class CorrugatedSteel(Material):
    def __init__(self):
        super().__init__(density = 336, cost = 53.8, co2_intensity = 105)      #cost per m^2, kg CO2 per m^2

###########################################################

beam_wood = RedCedar()
deck_mat = CorrugatedSteel()

c_shore = Pavilion()

#defining the lengths of the beams (could be refined to match existing geometry of C Shore pavilion in UBC, or can take user input, or read data from file)
beam_dims = [#layer 1
             4, 4, 4, 4, 4,
             #layer 2
             4, 1, 1, 1, 4,
             #layer 3
             4, 1, 1, 1, 4,
             #layer 4
             4, 1, 1, 1, 4,
             #layer 5
             4, 1, 1, 1, 4,
             #layer 6
             4, 1, 1, 1, 4,
             #layer 7
             4, 4, 4, 4, 4
            ]

#implement nested list and tab library to format info into table
for dim in beam_dims:
    new_beam = Beam(beam_wood, dim, 0.2, 0.4)
    c_shore.add_component(new_beam)
    print("Beam cost: $", new_beam.comp_cost())
    print("Beam carbon:", new_beam.comp_co2(), "kg CO2")

metaldeck = Decking(deck_mat, 4, 4, 0.005, 0.002)

c_shore.add_component(metaldeck)
print("Deck cost: $", metaldeck.comp_cost())
print("Deck carbon:", metaldeck.comp_co2(), "kg CO2")

print("Pavilion cost: $", c_shore.calc_cost())
print("Pavilion carbon:", c_shore.calc_co2(), "kg CO2")