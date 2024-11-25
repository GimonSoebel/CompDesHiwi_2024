"""In this assignment, you will design a new pavilion inspired by an existing pavilion or project (it does not have to be an ITECH pavilion :D).

You will use object-oriented programming. The components of the pavilion (e.g. columns, beams, roofs, walls) will be modelled as classes and subclasses.
Each component will have parameters (such as dimensions, material type, fabrication methods) that can influence the overall cost and CO2 emissions of the pavilion.
In addition, cost estimates will be updated based on design decisions such as material selection or changes in dimensions.

1. Create the pavilion class. This is the main class that contains the components of the pavilion and provides methods for estimating the total cost, carbon footprint, etc. 
2. Component classes: Each major component (e.g. column, beam, wall) should have its own class that calculates its individual cost, carbon footprint, etc. 
3. Material subclasses: Materials will have different costs and properties that will affect those of the components. 
4. Be creative
5. Upload your assignment to ILIAS and GitHub"""

import uuid
from classes.Material_cls import*
from classes.MyPavilion_cls import MyPavilion
from classes.Level_cls import*
from classes.Components_cls import Column, Component

""" 

myBeam = Beam(2,2,2, "myBeam")
myBeam.get_name()
print(myBeam.height)
myBeam.height = 0
print(myBeam.height)

MyPavComp.print_class_object(1,2) """

pine = Timber("Pine", 480, 717)        
larch = Timber("Larch", 820, 807)
normalbeton = Concrete("Normalbeton", 2300, 14)
leichtbeton = Concrete("Leichtbeton", 1900, 75)

structural_steel = Steel("B500B Betonstahl", 7850, 1.46, 500, 550, 210, 10-5, 'Moderat')


# # Set the project name once
MyPavilion.set_project_name("Wisdome")

pav = MyPavilion()


groundLevel = Level("Ground Level", 0.00, 2.5)
secondLevel = Level("Second Level", 2.50, 2.50)   

# # Associate levels with the pavilion
pav.add_level(groundLevel)
pav.add_level(secondLevel)


# Columns North Facade
Column_N_01 = Column(2.5, 0.8, 0.8, "Colum Corner N-W", groundLevel, secondLevel, 0, pine)
Column_N_02 = Column(2.5, 0.5, 0.8, "Colum North 01", groundLevel, secondLevel, 0, pine)
Column_N_03 = Column(2.5, 0.5, 0.8, "Colum North 02", groundLevel, secondLevel, 0, pine)
Column_N_04 = Column(2.5, 0.5, 0.8, "Colum North 03", groundLevel, secondLevel, 0, pine)
Column_N_05 = Column(2.5, 0.5, 0.8, "Colum North 04", groundLevel, secondLevel, 0, pine)
Column_N_06 = Column(2.5, 0.5, 0.8, "Colum North 05", groundLevel, secondLevel, 0, pine)
Column_N_07 = Column(2.5, 0.5, 0.8, "Colum North 06", groundLevel, secondLevel, 0, pine)
Column_N_08 = Column(2.5, 0.5, 0.8, "Colum North 07", groundLevel, secondLevel, 0, pine)
Column_N_09 = Column(2.5, 0.8, 0.8, "Colum Corner N-E", groundLevel, secondLevel, 0, pine)

# Columns East Facade
Column_E_01 = Column(2.5, 0.5, 0.8, "Colum East 01", groundLevel, secondLevel, 0, pine)
Column_E_02 = Column(2.5, 0.5, 0.8, "Colum East 02", groundLevel, secondLevel, 0, pine)
Column_E_03 = Column(2.5, 0.5, 0.8, "Colum East 03", groundLevel, secondLevel, 0, pine)
Column_E_04 = Column(2.5, 0.8, 0.8, "Colum Corner E-S", groundLevel, secondLevel, 0, pine)

# Columns South Facade
Column_S_01 = Column(2.5, 0.5, 0.8, "Colum South 01", groundLevel, secondLevel, 0, pine)
Column_S_02 = Column(2.5, 0.5, 0.8, "Colum South 02", groundLevel, secondLevel, 0, pine)
Column_S_03 = Column(2.5, 0.5, 0.8, "Colum South 03", groundLevel, secondLevel, 0, pine)
Column_S_04 = Column(2.5, 0.5, 0.8, "Colum South 04", groundLevel, secondLevel, 0, pine)
Column_S_05 = Column(2.5, 0.5, 0.8, "Colum South 05", groundLevel, secondLevel, 0, pine)
Column_S_06 = Column(2.5, 0.5, 0.8, "Colum South 06", groundLevel, secondLevel, 0, pine)
Column_S_07 = Column(2.5, 0.5, 0.8, "Colum South 07", groundLevel, secondLevel, 0, pine)
Column_S_08 = Column(2.5, 0.8, 0.8, "Colum Corner S-W", groundLevel, secondLevel, 0, pine)

# floor groundlevel
FloorGroundLevel = Floor()



print(Column01.get_material_name())
print(Column01.get_cost())
print(Component.calculate_total_cost())
Column01.get_volume