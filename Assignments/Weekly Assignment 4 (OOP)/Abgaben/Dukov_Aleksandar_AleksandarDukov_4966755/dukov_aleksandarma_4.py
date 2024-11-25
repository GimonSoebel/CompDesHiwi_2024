class Pavilion:
    def __init__(self, name):
        self.name = name 
        self.components = []

    def add_components(self, *components):
        self.components.extend(components)    

    def total_cost(self):
        return sum(component.cost() for component in self.components)

    def total_carbon_footprint(self):
        return sum(component.carbon_footprint() for component in self.components)
    
    def __str__(self):
        return (f"Pavilion's name: {self.name}\n"
                f"Pavilion's Cost: {self.total_cost():,.2f} Euro\n"
                f"Pavilion's Carbon Footprint: {self.total_carbon_footprint():,.2f} kg CO2\n")
    
class Component:
    def __init__(self, name, length, width, height, material):
        self.name = name
        self.length = length
        self.width = width 
        self.height = height
        self.material = material 

    def volume(self):
        return self.length*self.width*self.height

    def cost(self):
        return self.volume()*self.material.cost_per_unit

    def carbon_footprint(self):
        return self.volume() * self.material.carbon_per_unit 

class Material:
    def __init__(self, name, cost_per_unit, carbon_per_unit):
        self.name = name 
        self.cost_per_unit = cost_per_unit
        self.carbon_per_unit = carbon_per_unit

class Column(Component):
    pass

class Beam(Component):
    pass

class Slab(Component):
    pass

class Foundation(Component):
    pass

#Creating several elements with the same dimensions 
def create_columns(count, name, length, width, height, material):
    return [Column(f"{name} {i+1}", length, width, height, material) for i in range(count)]

def create_beams(count, name, length, width, height, material):
    return [Beam(f"{name} {i+1}", length, width, height, material) for i in range(count)]

def create_slabs(count, name, length, width, height, material):
    return [Slab(f"{name} {i+1}", length, width, height, material) for i in range(count)]

def create_foundations(count, name, length, width, height, material):
    return [Foundation(f"{name} {i+1}", length, width, height, material) for i in range(count)]

# Ensuring that the script are executed only when the script is run directly
if __name__ == "__main__":
    concrete = Material("Concrete", 75, 100)
    wood = Material("Wood", 50, 35)
    steel = Material("Steel", 65, 85)

    columns = create_columns(4, "Column", 0.12, 0.12, 3.3, steel)
    beams = create_beams(4, "Beam", 6, 0.3, 0.3, wood)
    slabs = create_slabs(2, "Slab", 6, 6, 0.08, concrete)
    foundation = create_foundations(4, "Foundation", 0.5, 0.5, 0.5, concrete)

    pavilion = Pavilion("Pavilion 1")
    pavilion.add_components(*columns, *beams, *slabs, *foundation) #unpacking the objects columns, beams, slabs and foundation, because they contain a list of entries, which are then added to the class Pavillion and calculated there  

    # Print summary
    print(pavilion)
