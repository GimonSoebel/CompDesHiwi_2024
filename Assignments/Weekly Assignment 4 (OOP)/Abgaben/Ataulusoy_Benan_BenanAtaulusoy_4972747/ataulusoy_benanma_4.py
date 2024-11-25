"""In this assignment, you will design a new pavilion inspired by an existing pavilion or project (it does not have to be an ITECH pavilion :D).

You will use object-oriented programming. The components of the pavilion (e.g. columns, beams, roofs, walls) will be modelled as classes and subclasses.
Each component will have parameters (such as dimensions, material type, fabrication methods) that can influence the overall cost and CO2 emissions of the pavilion.
In addition, cost estimates will be updated based on design decisions such as material selection or changes in dimensions.

1. Create the pavilion class. This is the main class that contains the components of the pavilion and provides methods for estimating the total cost, carbon footprint, etc. 
2. Component classes: Each major component (e.g. column, beam, wall) should have its own class that calculates its individual cost, carbon footprint, etc. 
3. Material subclasses: Materials will have different costs and properties that will affect those of the components. 
4. Be creative
5. Upload your assignment to ILIAS and GitHub"""

#Material, material features and calculation

class Material:
   def __init__(self, name, cost_per_unit, co2_per_unit):
       self.name = name
       self.cost_per_unit = cost_per_unit
       self.co2_per_unit = co2_per_unit
   
class Component:
   def __init__(self, name, length, width, height, quantity=1):
       self.name = name
       self.material = Material("Fiberglass brick", cost_per_unit=2, co2_per_unit=0.005)
       self.length = length
       self.width = width
       self.height = height
       self.quantity = quantity

   def calculate_volume(self):
       return self.length * self.width * self.height

   def calculate_cost(self):
       return self.calculate_volume() * self.material.cost_per_unit * self.quantity

   def calculate_carbon_footprint(self):
       return self.calculate_volume() * self.material.co2_per_unit * self.quantity
   
   def display_info(self):
       print(f"Component: {self.name}")
       print(f"Material: {self.material.name}")
       print(f"Dimensions: {self.length} cm x {self.width} cm x {self.height} cm")
       print(f"Quantity: {self.quantity}")
       print(f"Cost: €{self.calculate_cost():,.2f}")
       print(f"CO2 Emissions: {self.calculate_carbon_footprint():,.2f} kg CO2")
       
#Pavilion

class Pavilion:
   def __init__(self, name):
       self.name = name
       self.components = []
   
   def add_component(self, component):
       self.components.append(component)
   
   #Total cos, total carbon footprint and sustainability details

   def total_cost(self):
       return sum(component.calculate_cost() for component in self.components)
   
   def total_carbon_footprint(self):
       return sum(component.calculate_carbon_footprint() for component in self.components)
   
   def generate_sustainability_report(self):
       print(f"Pavilion: {self.name}")
       print(f"Total Cost: €{self.total_cost():,.2f}")
       print(f"Total CO2 Emissions: {self.total_carbon_footprint():,.2f} kg CO2")
       print("\nComponent Details:")
       for component in self.components:
           component.display_info()
           print()


def main():

   my_pavilion = Pavilion("Serpentine Pavilion")

#Component details
   Module01 = Component("Module01", 50, 40, 120, quantity=800)
   Module02 = Component("Module02", 50, 40, 80, quantity=400)
   Module03 = Component("Module03", 50, 40, 40, quantity=600)

   my_pavilion.add_component(Module01)
   my_pavilion.add_component(Module02)
   my_pavilion.add_component(Module03)
   
#Sustainability summary
   my_pavilion.generate_sustainability_report()


if __name__ == "__main__":
   main()