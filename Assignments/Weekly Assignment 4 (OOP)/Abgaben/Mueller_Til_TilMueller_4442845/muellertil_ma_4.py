## I create the chinese pavillion from Expo 2010, The beams of the pavillion are inspired by the Dou-Gong System typical in chinese Carpentry
## I want to recreate the layering, with every layer of beam rotation 90 degrees and getting longer every layer (good use for a loop)
## https://www.archdaily.com/34037/china-pavillion-for-shanghai-world-expo-2010

# Pavilion Class
class Pavilion:
    def __init__(self):
        self.components = []  # List to store components like beams

    def add_component(self, component):
        """Add a component to the pavilion."""
        self.components.append(component)

    def calculate_cost_total(self):
        """Calculate total cost of all components."""
        return sum(component.cost for component in self.components)

    def calculate_carbon_total(self):
        """Calculate total carbon footprint of all components."""
        return sum(component.carbon for component in self.components)


# Beam Class
class Beam:
    def __init__(self, length, width, height, material):
        """
        Initialize the Beam with dimensions and material.
        
        :param length: Length of the beam.
        :param width: Width of the beam.
        :param height: Height of the beam.
        :param material: Material instance used for the beam.
        """
        self.length = length
        self.width = width
        self.height = height
        self.material = material

        # Calculate properties
        self.volume = self.calculate_volume()
        self.cost = self.calculate_cost()
        self.carbon = self.calculate_carbon()

    def calculate_volume(self):
        """Calculate the volume of the beam."""
        return self.length * self.width * self.height

    def calculate_cost(self):
        """Calculate the cost of the beam based on its volume."""
        return self.volume * self.material.cost_per_cubic_meter

    def calculate_carbon(self):
        """Calculate the carbon footprint of the beam based on its volume."""
        return self.volume * self.material.carbon_per_cubic_meter


# Material Class
class Material:
    def __init__(self, name, cost_per_cubic_meter, carbon_per_cubic_meter):
        """
        Initialize the Material with its properties.
        
        :param name: Name of the material.
        :param cost_per_cubic_meter: Cost of the material per cubic meter.
        :param carbon_per_cubic_meter: Carbon footprint per cubic meter.
        """
        self.name = name
        self.cost_per_cubic_meter = cost_per_cubic_meter
        self.carbon_per_cubic_meter = carbon_per_cubic_meter

    def __repr__(self):
        """String representation of the Material."""
        return f"Material(name={self.name}, cost={self.cost_per_cubic_meter}, carbon={self.carbon_per_cubic_meter})"


# Hardcode materials
timber = Material("Timber", 100, 0)  # Timber: cost=100, carbon=0
steel = Material("Steel", 7000, 1.8)  # Steel: cost=7000, carbon=1.8
concrete = Material("Concrete", 500, 2.0)  # Concrete: cost=500, carbon=2.0

# Print materials for verification
print("Properties of Timber:", timber)
print("Properties of Steel:", steel)
print("Properties of Concrete:", concrete)

# Parameters for the initial layer
initial_length = 5
width = 0.2
height = 0.3
layers = 5
chosen_material = timber  # Choose a material for the beams
growth_per_layer = 1

print("initial proporties of first layer are:", "lenght: ", initial_length, "width x height: ", width, "x", height, "material: ", chosen_material)

# Create the Pavilion instance
pavilion = Pavilion()

# Loop to create stacking beams and add to pavilion
for i in range(layers):
    length = initial_length + i * growth_per_layer  # Beam length increases with each layer
    rotation = 90 * i  # Each layer rotates 90 degrees
    beam = Beam(length, width, height, chosen_material)  # Create the beam
    pavilion.add_component(beam)  # Add beam to the Pavilion

    

# Verify total cost and carbon footprint of the pavilion
print("Total Pavilion Cost:", pavilion.calculate_cost_total())
print("Total Pavilion Carbon Footprint:", pavilion.calculate_carbon_total())