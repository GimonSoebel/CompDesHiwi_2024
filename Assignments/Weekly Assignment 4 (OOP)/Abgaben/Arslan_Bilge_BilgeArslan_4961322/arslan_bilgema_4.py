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

class Pavilion:
    def __init__(self, ID):
        self.ID = ID
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def total_cost_and_co2(self):
        total_cost = sum(component.cost_calculation() for component in self.components)
        total_co2 = sum(component.co2_calculation() for component in self.components)
        return total_cost, total_co2

class TopPanels(Pavilion):
    def __init__(self, ID, material):
        super().__init__(ID)
        self.material = material
        self.panels = [self.create_panel(i) for i in range(1, 6)]

    def create_panel(self, id):
        return {
            "ID": f"Top Panel_{id:02d}",
            "length": round(random.uniform(6.0, 7.0), 2),
            "width": round(random.uniform(1.0, 2.0), 2),
            "height": round(random.uniform(0.02, 0.1), 2),
        }

    def cost_calculation(self):
        total_cost = sum(
            panel["length"] * panel["width"] * self.material.cost_per_unit
            for panel in self.panels
        )
        return total_cost

    def co2_calculation(self):
        total_co2 = sum(
            panel["length"] * panel["width"] * self.material.co2_per_unit
            for panel in self.panels
        )
        return total_co2

class BottomPanels(Pavilion):
    def __init__(self, ID, material):
        super().__init__(ID)
        self.material = material
        self.panels = [self.create_panel(i) for i in range(1, 6)] 

    def create_panel(self, id):
        return {
            "ID": f"Bottom Panel_{id:02d}",
            "length": round(random.uniform(6.0, 7.0), 2),
            "width": round(random.uniform(1.0, 2.0), 2),
            "height": round(random.uniform(0.02, 0.1), 2),
        }

    def cost_calculation(self):
        total_cost = sum(
            panel["length"] * panel["width"] * self.material.cost_per_unit
            for panel in self.panels
        )
        return total_cost

    def co2_calculation(self):
        total_co2 = sum(
            panel["length"] * panel["width"] * self.material.co2_per_unit
            for panel in self.panels
        )
        return total_co2

class Joints(Pavilion):
    def __init__(self, ID, material):
        super().__init__(ID)
        self.material = material
        self.joints = [self.create_joint(i) for i in range(1, 9)] 

    def create_joint(self, idx):
        return {
            "ID": f"Joint_{idx:02d}",
            "length": round(random.uniform(0.1, 0.2), 2),
            "width": round(random.uniform(0.1, 0.2), 2),
            "height": round(random.uniform(0.1, 0.2), 2),
        }

    def cost_calculation(self):
        total_cost = sum(
            joint["length"] * joint["width"] * self.material.cost_per_unit
            for joint in self.joints
        )
        return total_cost

    def co2_calculation(self):
        total_co2 = sum(
            joint["length"] * joint["width"] * self.material.co2_per_unit
            for joint in self.joints
        )
        return total_co2

class Material:
    def __init__(self, name, cost_per_unit, co2_per_unit):
        self.name = name
        self.cost_per_unit = cost_per_unit
        self.co2_per_unit = co2_per_unit

class Spruce(Material):
    def __init__(self):
        super().__init__("Spruce", 25, 0.6)

class Birch(Material):
    def __init__(self):
        super().__init__("Birch", 30, 0.8)


# Estimation values with Birch

pavilion_birch = Pavilion("Pavilion_birch")

birch = Birch()
top_panels = TopPanels("TopPanels", birch)
bottom_panels = BottomPanels("BottomPanels", birch)
joints = Joints("Joints", birch)

pavilion_birch.add_component(top_panels)
pavilion_birch.add_component(bottom_panels)
pavilion_birch.add_component(joints)

print("\nEstimations with birch:\n")
print("Top Panels Properties:")
for panel in top_panels.panels:
    print(
        f"  {panel['ID']}:\n\tLength: {panel['length']}m, Width: {panel['width']}m, Height: {panel['height']}m"
    )

print("\nBottom Panels Properties:")
for panel in bottom_panels.panels:
    print(
        f"  {panel['ID']}:\n\tLength: {panel['length']}m, Width: {panel['width']}m, Height: {panel['height']}m"
    )

print("\nJoints Properties:")
for joint in joints.joints:
    print(
        f"  {joint['ID']}:\n\tLength: {joint['length']}m, Width: {joint['width']}m, Height: {joint['height']}m"
    )

top_cost = top_panels.cost_calculation()
top_co2 = top_panels.co2_calculation()
bottom_cost = bottom_panels.cost_calculation()
bottom_co2 = bottom_panels.co2_calculation()
joints_cost = joints.cost_calculation()
joints_co2 = joints.co2_calculation()
total_cost, total_co2 = pavilion_birch.total_cost_and_co2()

print(f"\n  Top Panels:\n\tCost = €{top_cost:.2f}, CO2 = {top_co2:.2f} kg CO₂e")
print(f"  Bottom Panels:\n\tCost = €{bottom_cost:.2f}, CO2 = {bottom_co2:.2f} kg CO₂e")
print(f"  Joints:\n\tCost = €{joints_cost:.2f}, CO2 = {joints_co2:.2f} kg CO₂e")
print(f"  Total:\n\tCost = €{total_cost:.2f}, CO2 = {total_co2:.2f} kg CO₂e")


# Estimation values with Spruce

pavilion_spruce = Pavilion("Pavilion_spruce")

spruce = Spruce()
top_panels = TopPanels("TopPanels", spruce)
bottom_panels = BottomPanels("BottomPanels", spruce)
joints = Joints("Joints", spruce)

pavilion_spruce.add_component(top_panels)
pavilion_spruce.add_component(bottom_panels)
pavilion_spruce.add_component(joints)

print("\nEstimations with spruce:\n")
print("Top Panels Properties:")
for panel in top_panels.panels:
    print(
        f"  {panel['ID']}:\n\tLength: {panel['length']}m, Width: {panel['width']}m, Height: {panel['height']}m"
    )

print("\nBottom Panels Properties:")
for panel in bottom_panels.panels:
    print(
        f"  {panel['ID']}:\n\tLength: {panel['length']}m, Width: {panel['width']}m, Height: {panel['height']}m"
    )

print("\nJoints Properties:")
for joint in joints.joints:
    print(
        f"  {joint['ID']}:\n\tLength: {joint['length']}m, Width: {joint['width']}m, Height: {joint['height']}m"
    )

top_cost = top_panels.cost_calculation()
top_co2 = top_panels.co2_calculation()
bottom_cost = bottom_panels.cost_calculation()
bottom_co2 = bottom_panels.co2_calculation()
joints_cost = joints.cost_calculation()
joints_co2 = joints.co2_calculation()
total_cost, total_co2 = pavilion_spruce.total_cost_and_co2()

print(f"\n  Top Panels:\n\tCost = €{top_cost:.2f}, CO2 = {top_co2:.2f} kg CO₂e")
print(f"  Bottom Panels:\n\tCost = €{bottom_cost:.2f} euro, CO2 = {bottom_co2:.2f} kg CO₂e")
print(f"  Joints:\n\tCost = €{joints_cost:.2f}, CO2 = {joints_co2:.2f} kg CO₂e")
print(f"  Total:\n\tCost = €{total_cost:.2f}, CO2 = {total_co2:.2f} kg CO₂e")
