"""In this assignment, you will design a new pavilion inspired by an existing pavilion or project (it does not have to be an ITECH pavilion :D).

You will use object-oriented programming. The components of the pavilion (e.g. columns, beams, roofs, walls) will be modelled as classes and subclasses.
Each component will have parameters (such as dimensions, material type, fabrication methods) that can influence the overall cost and CO2 emissions of the pavilion.
In addition, cost estimates will be updated based on design decisions such as material selection or changes in dimensions.

1. Create the pavilion class. This is the main class that contains the components of the pavilion and provides methods for estimating the total cost, carbon footprint, etc. 
2. Component classes: Each major component (e.g. column, beam, wall) should have its own class that calculates its individual cost, carbon footprint, etc. 
3. Material subclasses: Materials will have different costs and properties that will affect those of the components. 
4. Be creative
5. Upload your assignment to ILIAS and GitHub"""



### Pavilion class - includes total cost and carbon emission 
class Pavilion:
    def __init__(self, name):
        self.name = name
        self.components = []
        self.total_cost = 0
        self.total_co2 = 0

    #list of components
    def add_component(self, component):
        self.components.append(component)
        self.total_cost += component.calculate_cost()
        self.total_co2 += component.calculate_co2()

    def pavilion_type(self):
        print(f'''
              The pavilion {self.name} has {len(self.components)} components
              The total cost is {self.total_cost} euros and the total carbon emissions are {self.total_co2} kgCO2e
              ''')

### Material class - determines cost, embodied carbon and density at a per unit scale
class Material:
    def __init__(self, name, cost_kg, carbon_kg, kg_m3):
        self.name = name
        self.cost_kg = cost_kg
        self.carbon_kg = carbon_kg
        self.kg_m3 = kg_m3

### Component class - includes total cost and carbon emission 
class Component:
    def __init__(self, name, length, width, depth, material):
        self.name = name
        self.length = length
        self.width = width
        self.depth = depth
        self.material = material
    
    #calculates volume based on component length, width, depth
    def calculate_volume(self):
        return self.length * self.width * self.depth
    
    #calculates mass based on calculated volume and per unit density from material
    def calculate_mass(self):
        return self.calculate_volume() * self.material.kg_m3

    #calculates cost based on mass and cost per unit from material
    def calculate_cost(self):
        return self.calculate_mass() * self.material.cost_kg

    #calculates carbon emission based on mass and embodied per unit from material
    def calculate_co2(self):
        return self.calculate_mass() * self.material.carbon_kg

### Component subclasses
class Beam(Component):
    def __init__(self, length, width, depth, material):
        super().__init__("Beam", length, width, depth, material)

class Column(Component):
    def __init__(self, length, width, depth, material):
        super().__init__("Column", length, width, depth, material)

class Floor(Component):
    def __init__(self, length, width, depth, material):
        super().__init__("Floor", length, width, depth, material)

class Roof(Component):
    def __init__(self, length, width, depth, material):
        super().__init__("Roof", length, width, depth, material)

class Wall(Component):
    def __init__(self, length, width, depth, material):
        super().__init__("Wall", length, width, depth, material)

class Window(Component):
    def __init__(self, length, width, depth, material):
        super().__init__("Window", length, width, depth, material)


### Specific Materials 
#name, cost_kg, carbon_kg, kg_m3
m1 = Material("Steel", 0.85, 1.55, 7850)
m2 = Material("Timber", 2.24, 0.82, 400)
m3 = Material("Concrete", 0.40, 0.138, 2400)
m4 = Material("Glass", 7.50, 1.63, 2200)
m5 = Material("CLT", 0.94, -1.20, 480)

# User Input Pavilion name 
pavilion_name = input("Enter the name of the pavilion: ")
pavilion = Pavilion(pavilion_name)

# User Input Pavilion dimensions 
pavilion_length = float(input("Enter the length of the pavilion (meters): "))
pavilion_width = float(input("Enter the width of the pavilion (meters): "))
pavilion_height = float(input("Enter the height of the pavilion (meters): "))

## User Input Pavilion components using for loop
# name, length, width, depth, material
beam_count = int(input("Enter the number of beams you would like to build: "))
for _ in range(beam_count):pavilion.add_component(Beam(3, .15 , .2, m1))
column_count = int(input("Enter the number of columns you would like to build: "))
for _ in range(column_count):pavilion.add_component(Column(.5, .5, pavilion_height, m2))
wall_count = int(input("Enter the number of walls you would like to build: "))
for _ in range(wall_count):pavilion.add_component(Wall(2.2, 2.6, pavilion_height, m2))
window_count = int(input("Enter the number of windows you would like to build: "))
for _ in range(window_count):pavilion.add_component(Window(.61, .9, .02, m4))

## Specific components
# name, length, width, depth, material
pavilion.add_component(Roof(pavilion_length, pavilion_width, 2, m5))
pavilion.add_component(Floor(pavilion_length, pavilion_width, .02, m3))

pavilion.pavilion_type()

