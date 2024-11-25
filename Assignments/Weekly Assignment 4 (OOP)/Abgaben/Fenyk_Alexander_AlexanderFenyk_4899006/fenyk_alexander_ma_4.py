# Importing the random module for generating random values
import random
# Importing defaultdict from collections to keep track of component counts
from collections import defaultdict

# Define a class for Material with properties and methods
class Material:
    def __init__(self, name, cost_per_m3, carbon_footprint_per_m3):
        # Initialize the material with its name, cost per cubic meter, and carbon footprint per cubic meter
        self.name = name
        self.cost_per_m3 = cost_per_m3
        self.carbon_footprint_per_m3 = carbon_footprint_per_m3

    def __str__(self):
        # String representation of the material showing its properties
        return (f"{self.name} (Cost: {self.cost_per_m3} €/m³, "
                f"Carbon Footprint: {self.carbon_footprint_per_m3} kgCO2/m³)")

# Define a class to represent a Pavilion containing components
class Pavilion:
    def __init__(self, name):
        # Initialize the pavilion with a name and an empty list of components
        self.name = name
        self.components = []

    def add_component(self, component):
        """Add a component to the pavilion."""
        # Append the given component to the components list
        self.components.append(component)

    def calculate_total_cost(self):
        """Calculate the total cost of the pavilion."""
        # Sum up the costs of all components in the pavilion
        return sum(component.calculate_cost() for component in self.components)

    def calculate_total_carbon_footprint(self):
        """Calculate the total carbon footprint of the pavilion."""
        # Sum up the carbon footprints of all components in the pavilion
        return sum(component.calculate_carbon_footprint() for component in self.components)

    def __str__(self):
        # String representation of the pavilion with its name and number of components
        return f"Pavilion: {self.name}, Components: {len(self.components)}"

# Define a class to represent a component of a pavilion
class Component:
    def __init__(self, name, material, length, width, height):
        # Initialize the component with a name, material, and dimensions (length, width, height)
        self.name = name
        self.material = material
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        """Calculate the volume of the component."""
        # Calculate the volume using length × width × height
        return self.length * self.width * self.height

    def calculate_cost(self):
        """Calculate the cost of the component based on its volume and material cost."""
        # Multiply the volume by the cost per cubic meter of the material
        return self.volume() * self.material.cost_per_m3

    def calculate_carbon_footprint(self):
        """Calculate the carbon footprint of the component."""
        # Multiply the volume by the carbon footprint per cubic meter of the material
        return self.volume() * self.material.carbon_footprint_per_m3

    def __str__(self):
        # String representation of the component with details about its name, material, and calculated properties
        volume = self.volume()
        return (f"Component: {self.name}, Material: {self.material.name}, "
                f"Volume: {volume:.2f} m³, "
                f"Cost: {self.calculate_cost():.2f} €, "
                f"Carbon Footprint: {self.calculate_carbon_footprint():.2f} kgCO2")

# Define a subclass for art installations, inheriting from Component
class ArtInstallation(Component):
    def __init__(self, name, material, length, width, height, artist):
        # Initialize the base component class and add an artist attribute
        super().__init__(name, material, length, width, height)
        self.artist = artist

    def __str__(self):
        # String representation of the art installation with artist and additional details
        volume = self.volume()
        return (f"Art Installation: {self.name}, Artist: {self.artist}, Material: {self.material.name}, "
                f"Volume: {volume:.2f} m³, "
                f"Cost: {self.calculate_cost():.2f} €, "
                f"Carbon Footprint: {self.calculate_carbon_footprint():.2f} kgCO2")

# Predefine a dictionary of materials with their properties
materials = {
    "Concrete": Material("Concrete", 100, 350),
    "Steel": Material("Steel", 500, 2000),
    "Wood": Material("Wood", 150, 50),
    "Glass": Material("Glass", 250, 1000),
    "Flax_Fibre": Material("Flax_Fibre", 300, 100),
    "Carbon_Fibre": Material("Carbon_Fibre", 10000, 30000)
}

# Predefine a list of artist names
artists = [
    "Kurt Schwitters", "Leftyoutthere", "Yayoi Kusama", "Marcel Broodthaers", 
    "Gordon Matta-Clark", "Judy Chicago", "Jason Rhoades", "Kara Walker"
]

# Generate a list of 50 random dimensions for components
dimensions = [(random.uniform(1, 10), random.uniform(0.1, 1), random.uniform(0.1, 1)) for _ in range(50)]

# Create a new Pavilion instance named "Research Demonstrator 2029"
pavilion = Pavilion("Research Demonstrator 2029")

# Use defaultdict to keep track of component counts for naming
component_counters = defaultdict(int)

# Loop to generate 50 components
for _ in range(50):
    # Randomly select a component type (e.g., Beam, Column)
    component_name = random.choice(["Beam", "Column", "Roof", "Foundation", "Art Installation"])
    # Randomly select dimensions from the pre-generated list
    length, width, height = random.choice(dimensions)
    # Create a numbered name for the component based on its type and count
    numbered_name = f"{component_name} {component_counters[component_name]+1}"
    # Increment the count for the selected component type
    component_counters[component_name] += 1

    # Select a material: Foundation always uses Concrete, others use random materials
    material = materials["Concrete"] if component_name == "Foundation" else random.choice(list(materials.values()))

    # If the component is an art installation, assign an artist and create an ArtInstallation instance
    if component_name == "Art Installation":
        artist = random.choice(artists)
        component = ArtInstallation(name=numbered_name, material=material, length=length, width=width, height=height, artist=artist)
    else:
        # Otherwise, create a standard Component instance
        component = Component(name=numbered_name, material=material, length=length, width=width, height=height)

    # Add the generated component to the pavilion
    pavilion.add_component(component)

# Sort the components alphabetically by their name for display
sorted_components = sorted(pavilion.components, key=lambda comp: comp.name)

# Print details about the pavilion
print(pavilion)
print("Total Cost:", pavilion.calculate_total_cost())
print("Total Carbon Footprint:", pavilion.calculate_total_carbon_footprint())

# Print each component in the sorted list
print("\nComponents (sorted by type):")
for component in sorted_components:
    print(component)