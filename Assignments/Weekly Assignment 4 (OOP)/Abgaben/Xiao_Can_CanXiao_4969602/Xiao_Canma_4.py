# Create the pvilion class
class Pavilion:
    def __init__(self):
        self.components=[]
    def add_component(self,component):
        self.components.append(component)
    def estimate_cost(self):
        return sum(component.cost() for component in self.components)
    def estimate_carbon_footprint(self):
        return sum(component.co2_emissions() for component in self.components)

## Create the component class
class Component:
    def __init__(self,material,weight):
        self.material=material
        self.weight=weight
    def cost(self):
        return self.material.cost_per_kg * self.weight
    def co2_emissions(self):
        return self.material.co2_per_kg * self.weight
    
### Create the subclass for component
class Column(Component):
    pass
    
class Beam(Component):
    pass
    
class Roof(Component):
    pass
    
class Wall(Component):
    pass
    
#### Create the material class
class Material:
    def __init__(self,name,cost_per_kg,co2_per_kg):
        self.name=name
        self.cost_per_kg=cost_per_kg
        self.co2_per_kg=co2_per_kg

##### Create the sublass for material    
class Steel(Material):
    pass

class Concrete(Material):
    pass

class Timber(Material):
    pass

###### Create a function for user input
def get_user_input():
    pavilion = Pavilion()
    materials = {
        "Steel": Steel("Steel", cost_per_kg=1.2, co2_per_kg=1.8),
        "Concrete": Concrete("Concrete", cost_per_kg=0.05, co2_per_kg=2.5),
        "Timber": Timber("Timber", cost_per_kg=2, co2_per_kg=0.2),
    }

    print("Enter components (type 'done' to finish):")
    while True:
        component_type = input("Component type (Column/Beam/Roof/Wall): ").strip()
        if component_type.lower() == "done":
            break

        if component_type not in ["Column", "Beam", "Roof", "Wall"]:
            print("Invalid component type. Try again.")
            continue

        material_name = input("Material (Steel/Concrete/Timber): ").strip()
        if material_name not in materials:
            print("Invalid material name. Try again.")
            continue

        try:
            weight = float(input("Weight (kg): "))
        except ValueError:
            print("Invalid weight. Please enter a numeric value.")
            continue

        material = materials[material_name]
        component_class = globals()[component_type]
        component = component_class(material, weight)
        pavilion.add_component(component)

    return pavilion


####### Calculate and output
if __name__ == "__main__":
    pavilion = get_user_input()
    total_cost = pavilion.estimate_cost()
    total_co2 = pavilion.estimate_carbon_footprint()

    print(f"\nTotal Cost: €{total_cost:.2f}")
    print(f"Total CO2 Emissions: {total_co2:.2f} kg")