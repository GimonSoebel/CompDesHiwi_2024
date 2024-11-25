"""In this assignment, you will design a new pavilion inspired by an existing pavilion or project (it does not have to be an ITECH pavilion :D).

You will use object-oriented programming. The components of the pavilion (e.g. columns, beams, roofs, walls) will be modelled as 
classes and subclasses.
Each component will have parameters (such as dimensions, material type, fabrication methods) that can influence the overall cost 
and CO2 emissions of the pavilion.
In addition, cost estimates will be updated based on design decisions such as material selection or changes in dimensions.

1. Create the pavilion class. This is the main class that contains the components of the pavilion and provides methods for estimating 
the total cost, carbon footprint, etc. 
2. Component classes: Each major component (e.g. column, beam, wall) should have its own class that calculates its individual cost, 
carbon footprint, etc. 
3. Material subclasses: Materials will have different costs and properties that will affect those of the components. 
"""
class Material:
    def __init__(self, material, unit, cost):
        self.material = material
        self.unit = unit
        self.cost = cost

# Define Materials
m1 = Material("Wood", "m", 32)
m2 = Material("Steal", "m²", 100)
m3 = Material("Concret", "m³", 50)
m4 = Material("Fabric", "m²", 24)

class Element:
    def __init__(self, element, material, unit, cost, length, height, thickness):
        self.element = element
        self.material = material
        self.unit = unit
        self.cost = cost
        self.length = length
        self.height = height
        self.thickness = thickness
        self.area = None
        self.volume = None

    def calculation(self):
        print(f"The Pavillons Element is a {self.element}. The Elements material is {self.material}.")
        self.area = self.length * self.height
        self.volume = self.length * self.height * self.thickness

        # Print details depending on the unit type
        if self.unit == "m":
            print(f"The length of the {self.element} is {self.length} m. The Material cost is {self.cost} Euros per meter.")
        elif self.unit == "m²":
            print(f"The area of the {self.element} is {self.area} m². The Material cost is {self.cost} Euros per square meter.")
        elif self.unit == "m³":
            print(f"The volume of the {self.element} is {self.volume} m³. The Material cost is {self.cost} Euros per cubic meter.")

# Create Element instances
column = Element("Column", m1.material, m1.unit, m1.cost, 0.5, 3.5, 0.5)
beam = Element("Beam", m2.material, m2.unit, m2.cost, 4.0, 0.6, 0.4)
foundation = Element("Foundation", m3.material, m3.unit, m3.cost, 1, 1, 0.8)
roof = Element("Roof", m4.material, m4.unit, m4.cost, 3.2, 5.3, 0)

# Pavillon class to calculate and display the properties for multiple elements
class Pavillon:
    def __init__(self, element, amount, unit):
        self.element = element  # This should be the actual Element object
        self.amount = amount
        self.unit = unit
        self.total_length = None
        self.total_area = None
        self.total_volume = None

    def pavillon_properties(self):

        # Ensure calculations are performed
        self.element.calculation()

        # Depending on the unit, calculate totals and costs
        if self.unit == "m":
            self.total_length = self.element.length * self.amount
            total_cost = self.total_length * self.element.cost
            print(
                f"In total, the pavillon has {self.amount} {self.element.element}s. "
                f"This results in a total {self.element.material} length of {self.total_length} m. "
                f"The total cost for Columns is {total_cost} Euros."
            )

        elif self.unit == "m²":
            self.total_area = self.element.area * self.amount
            total_cost = self.total_area * self.element.cost
            print(
                f"In total, the pavillon has {self.amount} {self.element.element}s. "
                f"This results in a total {self.element.material} area of {self.total_area} m². "
                f"The total cost for Beams is {total_cost} Euros."
            )

        elif self.unit == "m³":
            self.total_volume = self.element.volume * self.amount
            total_cost = self.total_volume * self.element.cost
            print(
                f"In total, the pavillon has {self.amount} {self.element.element}s. "
                f"This results in a total {self.element.material} volume of {self.total_volume} m³. "
                f"The total cost for Foundations is {total_cost} Euros."
            )



# Create Pavillon instances for each element
column_pavillon = Pavillon(column, 4, column.unit)
beam_pavillon = Pavillon(beam, 12, beam.unit)
foundation_pavillon = Pavillon(foundation, 4, foundation.unit)
roof_pavillon = Pavillon(roof, 1, roof.unit)

# Calculate and display properties for each Pavillon component






print("\nColumn Properties:")
column_pavillon.pavillon_properties()

print("\nBeam Properties:")
beam_pavillon.pavillon_properties()

print("\nFoundation Properties:")
foundation_pavillon.pavillon_properties()

print("\nRoof Properties:")
roof_pavillon.pavillon_properties()

