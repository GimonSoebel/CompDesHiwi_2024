"""
In this assignment, you will design a new pavilion inspired by an existing pavilion or project (it does not have to be an ITECH pavilion :D).

You will use object-oriented programming. The components of the pavilion (e.g. columns, beams, roofs, walls) will be modelled as classes and subclasses.
Each component will have parameters (such as dimensions, material type, fabrication methods) that can influence the overall cost and CO2 emissions of the pavilion.
In addition, cost estimates will be updated based on design decisions such as material selection or changes in dimensions.

1. Create the pavilion class. This is the main class that contains the components of the pavilion and provides methods for estimating the total cost, carbon footprint, etc. 
2. Component classes: Each major component (e.g. column, beam, wall) should have its own class that calculates its individual cost, carbon footprint, etc. 
3. Material subclasses: Materials will have different costs and properties that will affect those of the components. 
4. Be creative
5. Upload your assignment to ILIAS and GitHub
"""

"""
For the task use object-oriented programming. A Pavillion should be created. The components of the pavilion (columns, beams, roofs, walls) will be modelled as classes and subclasses.
Each component will have parameters (such as dimensions, material type, fabrication methods) that can influence the total cost and total CO2 emissions of the pavilion.
In addition, total cost estimates will be updated based on design decisions such as material selection or changes in dimensions.

1. Create the pavilion class. This is the main class that contains the components of the pavilion and provides methods for estimating the total cost and total carbon footprint. 
2. Component classes: Each major component (column, beam, wall, roof) should have its own class that calculates its individual cost, carbon footprint, etc. 
3. Material subclasses: Materials will have different costs and properties that will affect those of the components. Materials that should be used are timber, concrete and steel
the user should be prompted to choose the material
"""

# components -> classes and subclasses
# each component has parameters (dimensions, material type, fabrication methods) that influence overall cost and co2 emissions
# cost estimate based on design decisions, material selection and dimensions

# pavilion class main class
## contains components
## provides methods for estimating total cost, carbon fp, etc
### component classes
### component, column, wall, beam, have its own class -> calcs individual cost, carbon footprint, etc
#### material subclasses
#### different costs and properties that will effect those of components

class Pavilion:
    def __init__(self, name):
        self.name = name
        self.components = []  #list to store the components

    def add_component(self, component):
        self.components.append(component)

    # calculates the total cost from all the individual costs in the component list
    def total_cost(self):
        return round(sum(component.individual_cost() for component in self.components), 2)
    
    # calculates the total emissions from all the individual emissions in the component list
    def total_emissions(self):
        return round(sum(component.individual_emissions() for component in self.components), 2)
    
    def __str__(self):
        return (f"Pavilion: {self.name}\n"
                f"Total Cost: {self.total_cost()}\n"
                f"Total CO2 Emissions: {self.total_emissions()}\n"
                f"Components: {len(self.components)}")
    

class Component:
    def __init__(self, name, material, length, width, height):
        self.name = name
        self.material = material
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def individual_cost(self):
        return self.volume() * self.material.cost_per_m3

    def individual_emissions(self):
        return self.volume() * self.material.emissions_per_m3

    def __str__(self):
        return (f"Component: {self.name}\n"
                f"Material: {self.material.name}\n"
                f"Volume: {self.volume()} m³\n"
                f"Cost: {self.individual_cost()} units\n"
                f"Emissions: {self.individual_emissions()} kg\n")
    
class Column(Component):
    pass


class Wall(Component):
    pass


class Roof(Component):
    pass
        

class Material:
    def __init__(self, name, cost_per_m3, emissions_per_m3):
        self.name = name
        self.cost_per_m3 = cost_per_m3
        self.emissions_per_m3 = emissions_per_m3

    def __str__(self):
        return (f"Material: {self.name}\n"
                f"Cost per m³: {self.cost_per_m3}\n"
                f"Emissions per m³: {self.emissions_per_m3}\n")
    
# materials

wood = Material("Wood", 1000, 100)
steel = Material("Steel", 10000, 20000)
concrete = Material("Concrete", 300, 500)

# components (self, name, material, length, width, height)

# columns

column_1 = Column("Column 1", steel, 0.1, 0.1, 2.00)
column_2 = Column("Column 2", steel, 0.1, 0.1, 2.25)
column_3 = Column("Column 3", steel, 0.1, 0.1, 2.50)
column_4 = Column("Column 4", steel, 0.1, 0.1, 2.75)
column_5 = Column("Column 5", steel, 0.1, 0.1, 3.00)

# walls

wall_1 = Wall("Wall 1", wood, 2.0, 0.1, 2.0)
wall_2 = Wall("Wall 2", wood, 3.0, 0.2, 1.0)
wall_3 = Wall("Wall 3", wood, 1.0, 0.15, 2.5)
wall_4 = Wall("Wall 4", wood, 2.5, 0.1, 1.5)

# roof

roof_1 = Roof("Roof 1", concrete, 4.0, 3.0, 0.2)

# adding them to the list

pavilion_1 = Pavilion("Pavilion Test")

pavilion_1.add_component(column_1)
pavilion_1.add_component(column_2)
pavilion_1.add_component(column_3)
pavilion_1.add_component(column_4)
pavilion_1.add_component(column_5)

pavilion_1.add_component(wall_1)
pavilion_1.add_component(wall_2)
pavilion_1.add_component(wall_3)
pavilion_1.add_component(wall_4)

pavilion_1.add_component(roof_1)

print(pavilion_1)