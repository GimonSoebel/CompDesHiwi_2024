"""In this assignment, you will design a new pavilion inspired by an existing pavilion or project (it does not have to be an ITECH pavilion :D).

You will use object-oriented programming. The components of the pavilion (e.g. columns, beams, roofs, walls) will be modelled as classes and subclasses.
Each component will have parameters (such as dimensions, material type, fabrication methods) that can influence the overall cost and CO2 emissions of the pavilion.
In addition, cost estimates will be updated based on design decisions such as material selection or changes in dimensions.

1. Create the pavilion class. This is the main class that contains the components of the pavilion and provides methods for estimating the total cost, carbon footprint, etc. 
2. Component classes: Each major component (e.g. column, beam, wall) should have its own class that calculates its individual cost, carbon footprint, etc. 
3. Material subclasses: Materials will have different costs and properties that will affect those of the components. 
4. Be creative
5. Upload your assignment to ILIAS and GitHub"""

import random 

# Hi! I decided to go from materials to the pavilion and building each component based on those materials
# and I chose the pavilion for the biennale

# Material class
class Material:
    def __init__(self, name, unit_cost, co2_emission, reuse_status):
        self.name = name 
        self.unit_cost = unit_cost  # Cost in euros per m3
        self.co2_emission = co2_emission  # CO2 emissions in kilograms
        self.reuse_status = reuse_status  # Whether the material is reused or new

    def __str__(self):
        return (f"Material: {self.name}, Cost: {self.unit_cost:.2f} €/m³, "
                f"CO2 Emission: {self.co2_emission:.2f} kg/m³, Status: {self.reuse_status}")

# Component class for parts of the pavilion
class Component:
    def __init__(self, name, volume, material):
        self.name = name 
        self.volume = volume  # Volume in cubic meters
        self.material = material  # Material used for the component

    def calculate_cost(self):
        return self.material.unit_cost * self.volume

    def calculate_emissions(self):
        return self.material.co2_emission * self.volume 

    def __str__(self):
        return (f"Component: {self.name}, Volume: {self.volume:.2f} m³, "
                f"Material: {self.material.name}, Cost: {self.calculate_cost():.2f} €, "
                f"CO2 Emissions: {self.calculate_emissions():.2f} kg")

# Pavilion class to represent the entire project
class Pavilion:
    def __init__(self, name):
        self.name = name  # Pavilion name
        self.components = []  # List of components in the pavilion

    def add_component(self, component):
        self.components.append(component)  # Add a component to the pavilion

    def total_cost(self):
        total = 0
        for component in self.components:
            total += component.calculate_cost()  # Sum up costs for all components
        return total

    def total_emissions(self):
        total = 0
        for component in self.components:
            total += component.calculate_emissions()  # Sum up emissions for all components
        return total

    def __str__(self):
        return (f"Pavilion: {self.name}, Total Cost: {self.total_cost():.2f} €, "
                f"Total CO2 Emissions: {self.total_emissions():.2f} kg")

# Material database (costs in euros per m³, emissions in kg per m³)
materials = [
    Material("Reclaimed Timber", 3000, 500, "Reused"),
    Material("New Timber", 5000, 800, "New"),
    Material("Natural Fiber Composite", 12000, 300, "New"),
    Material("Reclaimed Plastic", 7000, 600, "Reused"),
    Material("Carbon Fiber", 20000, 1000, "New"),
]

# biennaale pavilion
pavilion = Pavilion("Maison Fibre Pavilion")

# Add components
pavilion.add_component(Component("Column A", 0.5, materials[0]))
pavilion.add_component(Component("Column B", 0.4, materials[1]))
pavilion.add_component(Component("Beam A", 0.6, materials[2]))
pavilion.add_component(Component("Roof Panel", 2.0, materials[3]))
pavilion.add_component(Component("Support Frame", 1.2, materials[4]))

# for a short summary
print(pavilion)
print()

# List components in the pavilion
print("Components in the Pavilion:")
for component in pavilion.components:
    print(component)
print()

# List materials
print("Materials Used in the Pavilion:")
for material in materials:
    print(material)
print()

# Ask user to add custom components after showing the final summary
while True:
    user_input = input("Do you want to add a new component? (yes/no): ").lower()
    if user_input == "no":
        break
    elif user_input == "yes":
        component_name = input("Enter the component name: ")
        try:
            volume = float(input("Enter the component volume in m³: "))
        except ValueError:
            print("Invalid volume entered!")
            continue

# Show material options
        print("Choose a material by entering the number:")
        for i, material in enumerate(materials):
            print(f"{i + 1}: {material}")
        try:
            material_choice = int(input("Material number: ")) - 1
            if material_choice < 0 or material_choice >= len(materials):
                print("Invalid material choice. Skipping this component.")
                continue
            selected_material = materials[material_choice]
        except ValueError:
            print("Invalid material choice. Skipping this component.")
            continue

#adding the component
        new_component = Component(component_name, volume, selected_material)
        pavilion.add_component(new_component)
        print(f"Added component: {new_component}")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
print()

# Final summary after additions
print("Final Pavilion Summary:")
print(pavilion)
print()

# Final list of all components
print("Final Components in the Pavilion:")
for component in pavilion.components:
    print(component)

