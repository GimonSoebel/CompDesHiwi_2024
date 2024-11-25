#Main Pavilion Class
class Pavilion:
    def __init__(self, name):
        self.name = name
        self.components = []

    #Add Components to the Pavilion
    def add_components(self, component):
        self.components.append(component)

    #Calculate total Cost of the Pavilion
    def total_cost(self):
        total_cost = 0
        for component in self.components:
            total_cost += component.calculate_cost() 
        return total_cost

    #Calculate total Carbon Footprint of the Pavilion
    def total_carbon_footprint(self):
        total_carbon_footprint = 0
        for component in self.components:
            total_carbon_footprint += component.calculate_carbon_footprint()
        return total_carbon_footprint
    
    #Display Pavilion's total Cost and total Carbon Footprint
    def details(self):
        print(f"The Pavilion is called: {self.name}")
        print(f"\nBuilding Components of {self.name} are:" )
        for component in self.components:
            print (component)
        print(f"\nTotal Cost of the Pavilion: {self.total_cost():,.2f} Euro")
        print(f"Total Carbon Footprint of the Pavilion: {self.total_carbon_footprint():,.2f} units")
        print(f"Number of Components in {self.name}: {len(self.components)} components.\n")

#Materials Classes
class Material:
    def __init__(self, name, cost_per_m3, carbonemission_per_m3):
        self.name = name
        self.cost_per_m3 = cost_per_m3
        self.carbonemission_per_m3 = carbonemission_per_m3

#Fabrication method Classes
class FabMethod:
    def __init__(self, name, cost_per_method, carbonemission_per_method):
        self.name = name
        self.cost_per_method = cost_per_method
        self.carbonemission_per_method = carbonemission_per_method

#Components Classes 
class Components:
    def __init__(self, name, material, dimensions, fab_method):
        self.name = name
        self.material = material
        self.dimensions = dimensions
        self.fab_method = fab_method
    
    #Calculate Component's Volume
    def calculate_volume(self):
        volume = self.dimensions['height'] * self.dimensions['width'] * self.dimensions['thickness']
        return volume

    #Calculate Component's cost based on Volume and Fabrication Method
    def calculate_cost(self):
        volume = self.calculate_volume()
        total_cost = volume * self.material.cost_per_m3 * self.fab_method.cost_per_method
        return total_cost
    
    #Calculate Component's Carbon Footprint based on Volume and Fabrication Method
    def calculate_carbon_footprint(self):
        volume = self.calculate_volume()
        total_carbon = volume * self.material.carbonemission_per_m3 * self.fab_method.carbonemission_per_method
        return total_carbon
    
    #String representation of the Components
    def __str__(self):
        return (f"{self.name}: (Material used: {self.material.name}, Volume: {self.calculate_volume():.2f} m³, "
                f"Total Cost: {self.calculate_cost():,.2f} Euro, Total Carbon Emission: {self.calculate_carbon_footprint():,.2f} unit, "
                f"Fabrication Method: {self.fab_method.name})")

#Components "Child" Classess from Components "Parent" Class
class Column(Components):
    def __init__(self, name, material, dimensions, fab_method):
        super().__init__(name, material, dimensions, fab_method)

class Beam(Components):
    def __init__(self, name, material, dimensions, fab_method):
        super().__init__(name, material, dimensions, fab_method)

class Wall(Components):
    def __init__(self, name, material, dimensions, fab_method):
        super().__init__(name, material, dimensions, fab_method)

# Example Usage
if __name__ == "__main__":
    # Define Materials
    concrete = Material("Concrete", cost_per_m3=200, carbonemission_per_m3=1000)
    steel = Material("Steel", cost_per_m3=300, carbonemission_per_m3=2000)
    wood = Material("wood", cost_per_m3=100, carbonemission_per_m3=100)
    bricks = Material("bricks", cost_per_m3=50, carbonemission_per_m3=50)

    # Define Fabrication method
    robotic_fab = FabMethod("Robotic Fabrication", cost_per_method=3.0, carbonemission_per_method=0.5 )
    pre_fabrication = FabMethod("Pre_fabrication", cost_per_method=2.0, carbonemission_per_method=1.5)
    onsite_construction = FabMethod("Onsite Construction", cost_per_method=1.0, carbonemission_per_method=1.0)
    welding = FabMethod("Welding", cost_per_method=1.5, carbonemission_per_method=2.0)

    # Define components with its attributes
    column = Components("Column", material=concrete, dimensions={'height': 3, 'width': 0.3, 'thickness': 0.2}, fab_method=pre_fabrication)
    beam = Components("Beam", material=steel, dimensions={'height': 1, 'width': 0.5, 'thickness': 0.3}, fab_method=welding)
    wall = Components("Wall", material=bricks, dimensions={'height': 2.2, 'width': 2, 'thickness': 0.25}, fab_method=robotic_fab)
    roof = Components("roof", material=wood, dimensions={'height': 3.0, 'width': 3.0, 'thickness': 0.3}, fab_method=onsite_construction)

    # Define pavilion and add components
    pavilion = Pavilion("Lama's Pavilion")
    pavilion.add_components(column)
    pavilion.add_components(beam)
    pavilion.add_components(wall)
    pavilion.add_components(roof)

    # Print Pavilion Details (Name, Cost, Carbon Footprint)
    pavilion.details()