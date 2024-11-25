"""In this assignment, you will design a new pavilion inspired by an existing pavilion or project (it does not have to be an ITECH pavilion :D).

You will use object-oriented programming. The components of the pavilion (e.g. columns, beams, roofs, walls) will be modelled as classes and subclasses.
Each component will have parameters (such as dimensions, material type, fabrication methods) that can influence the overall cost and CO2 emissions of the pavilion.
In addition, cost estimates will be updated based on design decisions such as material selection or changes in dimensions.

1. Create the pavilion class. This is the main class that contains the components of the pavilion and provides methods for estimating the total cost, carbon footprint, etc. 
2. Component classes: Each major component (e.g. column, beam, wall) should have its own class that calculates its individual cost, carbon footprint, etc. 
3. Material subclasses: Materials will have different costs and properties that will affect those of the components. 
4. Be creative
5. Upload your assignment to ILIAS and GitHub

volume*density*co2 intesity
"""
import random


class Pavilion:
    ##main class

    def __init__(self, name):
        self.name = name
        self.components = []
    
    def add_component(self, component):
       self.components.append(component)

    def calc_total_cost(self):
        totalCost = 0
        for i in self.components:
            totalCost += i.individual_cost()
        return totalCost
        
    def calc_total_co2(self):
        totalCo2 = 0
        for i in self.components:
            totalCo2 += i.individual_co2()
        return totalCo2
    
    def __str__(self):
         return f'The pavilion {self.name} has {len(self.components)} components'
    

class Component:
    def __init__(self, name, material):
        self.name = name
        self.material = material


class Column(Component):
    def __init__(self, material, radius, length):
        super().__init__('Column', material)
        self.radius = radius
        self.length = length

    def calc_mass(self):
        #print(self.radius*self.radius*3.14*self.length*self.material.density)
        return self.radius*self.radius*3.14*self.length*self.material.density
    
    def individual_cost(self):
        #print(self.calc_mass() * self.material.cost)
        return self.calc_mass() * self.material.cost
    
    def individual_co2(self):
        #print(self.calc_mass() * self.material.co2)
        return self.calc_mass() * self.material.co2
    
    def __str__(self):
         return f'element name: {self.name} \nmaterial: {self.material.name} \ncost: {round(self.individual_cost(),2)} \nCO2: {round(self.individual_co2(),2)}'


    
class Beam(Component):
    def __init__(self, material, width, thickness, length):
        super().__init__('Beam', material)
        self.width = width
        self.thickness = thickness
        self.length = length

    def calc_mass(self):
        #print(self.width*self.thickness*self.length*self.material.density)
        return self.width*self.thickness*self.length*self.material.density
    
    def individual_cost(self):
        #print(self.calc_mass() * self.material.cost)
        return self.calc_mass() * self.material.cost
    
    def individual_co2(self):
        #print(self.calc_mass() * self.material.co2)
        return self.calc_mass() * self.material.co2
    
    def __str__(self):
         return f'element name: {self.name} \nmaterial: {self.material.name} \ncost: {round(self.individual_cost(),2)} \nCO2: {round(self.individual_co2(),2)}'


class Wall(Component):
    def __init__(self, material, width, thickness, height):
        super().__init__('Wall', material)
        self.width = width
        self.thickness = thickness
        self.height = height

    def calc_mass(self):
        #print(self.width*self.thickness*self.height*self.material.density)
        return self.width*self.thickness*self.height*self.material.density
    
    def individual_cost(self):
        #print(self.calc_mass() * self.material.cost)
        return self.calc_mass() * self.material.cost
    
    def individual_co2(self):
        #print(self.calc_mass() * self.material.co2)
        return self.calc_mass() * self.material.co2
    
    def __str__(self):
         return f'element name: {self.name} \nmaterial: {self.material.name} \ncost: {round(self.individual_cost(),2)} \nCO2: {round(self.individual_co2(),2)}'


class Material:
    def __init__(self, name, density, cost, co2):
        self.name = name
        self.density = density
        self.cost = cost
        self.co2 = co2
    
##density-kg/m3, cost-/kg, co2-/kg
class Wood(Material):
    def __init__(self):
        super().__init__('Wood', density = 700, cost = 30, co2 = 1.5)
    
class Concrete(Material):
    def __init__(self):
        super().__init__('Concrete', density = 2200, cost = 60, co2 = 0.9)

class Steel(Material):
   def __init__(self):
        super().__init__('Steel', density = 7700, cost = 1, co2 = 6.15)


wood = Wood()
concrete = Concrete()
steel = Steel()

material_choice = [wood, concrete, steel]


##creating elements

pavilion = Pavilion('ITECH Pavilion 2025')

num_initial = 4
list_column = []
list_beam = []
list_wall = []

print('Hello! We are now designing a pavilion together!')

for i in range(num_initial):

    example_column = Column(
            random.choice(material_choice), 
            round(random.uniform(0.01, 0.3), 2), 
            round(random.uniform(2.0, 5.0), 2))
    
    list_column.append(example_column)
    pavilion.add_component(example_column)
    print(example_column)
    
    example_beam = Beam(
            random.choice(material_choice), 
            round(random.uniform(0.05, 0.5), 2),
            round(random.uniform(0.05, 0.8), 2),
            round(random.uniform(2.0, 15.0), 2))
    
    list_beam.append(example_beam)
    pavilion.add_component(example_beam)
    print(example_beam)
    
    example_wall =  Wall(
            random.choice(material_choice), 
            round(random.uniform(0.8, 15.0), 2),
            round(random.uniform(0.05, 0.3), 2),
            round(random.uniform(2.0, 15.0), 2))

    list_wall.append(example_wall)
    pavilion.add_component(example_wall)
    print(example_wall)

while True:

    print()
    print(pavilion)
    print()
    #print('\n These are elements we have right now. Would you like to add more?')
    print("1. Add a column")
    print("2. Add a Beam")
    print("3. Add a wall")
    print("4. Calculate total cost and CO2")
    print("5. Exit the program")

    option = input("Choose an option: ")

    if option == "1":
            
        material_input = input("What is its material?(wood, concrete, or steel)")
        if material_input == "wood":
            material = wood
        elif material_input == "concrete":
            material = concrete
        elif material_input == "steel":
            material = steel
        else:
            print("Invalid material. Please choose wood, concrete, or steel.")
            continue

        radius_str = input("what is its radius?") 
        radius = float(radius_str)
        length_str = input("what is its length?") 
        length = float(length_str)
        num = int(input("How many of this column do you want?"))

        for i in range(num):
            new_column = Column(material, radius, length)
            list_column.append(new_column)
            pavilion.add_component(new_column)
        print(new_column)
    
            
    elif option == "2":
        material = input("What is its material?(wood, concrete, or steel)")
        if material_input == "wood":
            material = wood
        elif material_input == "concrete":
            material = concrete
        elif material_input == "steel":
            material = steel
        else:
            print("Invalid material. Please choose wood, concrete, or steel.")
            continue
        width_str = input("what is its width?") 
        width = float(width_str)
        thickness_str = input("what is its thickness?") 
        thickness = float(thickness_str)
        length_str = input("what is its length?") 
        length = float(length_str)
        num = int(input("How many of this beam do you want?"))

        for i in range(num):
            new_beam = Beam(material, width, thickness, length)
            list_beam.append(new_beam)
            pavilion.add_component(new_beam)
        print(new_beam)
            

    elif option == "3":
        material = input("What is its material?(wood, concrete, or steel)")
        if material_input == "wood":
            material = wood
        elif material_input == "concrete":
            material = concrete
        elif material_input == "steel":
            material = steel
        else:
            print("Invalid material. Please choose wood, concrete, or steel.")
            continue
        width_str = input("what is its width?") 
        width = float(width_str)
        thickness_str = input("what is its thickness?") 
        thickness = float(thickness_str)
        height_str = input("what is its height?") 
        height = float(height_str)
        num = int(input("How many of this wall do you want?"))

        for i in range(num):
            new_wall = Wall(material, width, thickness, height)
            list_wall.append(new_wall)
            pavilion.add_component(new_wall)
        print(new_wall)
            
    elif option == "4":

        print('total cost:', round(pavilion.calc_total_cost(),2))
        print('total CO2:', round(pavilion.calc_total_co2(),2))
        
    elif option == "5":

        print("Exiting the program. Thank you so much! Hope to see you soon:)")
        break

    else:
        print("Invalid option. Please try again.\n")


print(pavilion)
#print(list_column)
#print('total cost:', round(pavilion.calc_total_cost(),2))
#print('total CO2:', round(pavilion.calc_total_co2(),2))

"""
column_count = int(input("Enter the number of columns you would like to build: "))
for _ in range(column_count):pavilion.add_component(Column(.5, .5, pavilion_height, m2))
pavilion.add_component()
pavilion.add_component(Column(self, steel, 0.2, 3.0))
"""