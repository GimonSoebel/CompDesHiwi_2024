"""In this assignment, you will design a new pavilion inspired by an existing pavilion or project (it does not have to be an ITECH pavilion :D).

You will use object-oriented programming. The components of the pavilion (e.g. columns, beams, roofs, walls) will be modelled as classes and subclasses.
Each component will have parameters (such as dimensions, material type, fabrication methods) that can influence the overall cost and CO2 emissions of the pavilion.
In addition, cost estimates will be updated based on design decisions such as material selection or changes in dimensions.

1. Create the pavilion class. This is the main class that contains the components of the pavilion and provides methods for estimating the total cost, carbon footprint, etc. 
2. Component classes: Each major component (e.g. column, beam, wall) should have its own class that calculates its individual cost, carbon footprint, etc. 
3. Material subclasses: Materials will have different costs and properties that will affect those of the components. 
4. Be creative
5. Upload your assignment to ILIAS and GitHub"""

#inspired by the livtMats Biomimimetic Shell
#Components include foundation, shell, glazing

class Pavilion:
    def __init__(self, foundations, shell, glazing):
        self.foundations = foundations
        self.shell = shell
        self.glazing = glazing
    
    def emissions(self):
        emissions = round(self.foundations.emissions() + self.shell.emissions() + self.glazing.emissions(),0)
        return emissions
    
    def cost(self):
        cost = round(self.foundations.cost() + self.shell.cost() + self.glazing.cost(),2)
        return cost    
    
#blueprint for sub-classes
class Component:
    def __init__(self, materials, area, thickness):
        self.materials = materials
        self.area = area
        self.thickness = thickness

    def emissions(self):
        return self.materials.emissions_kg * self.area * self.thickness * self.materials.density
    
    def cost(self):
        return self.materials.cost_kg * self.area * self.thickness * self.materials.density


class Foundations(Component):
    def __init__(self, materials, area, thickness):
        super().__init__(materials, area, thickness)
        self.reinforcement_ratio = 0
        self.reinforcement_mat = ""

    def add_reinforcement(self, materials, reinforcement_ratio): #add reinforcement to foundation material by calling this function
        self.reinforcement_ratio = reinforcement_ratio
        self.reinforcement_mat = materials
        try: 
            if reinforcement_ratio > 1:
                raise ValueError
        except: print("Please provide a reinforcement ratio between 0 and 1.")
    def emissions(self):
        emissions = super().emissions()
        if self.reinforcement_ratio != 0: # if someone has added reinforcement to the foundation, the ratio will be greater than 0 and this should not throw an error.
            emissions += self.reinforcement_mat.emissions_kg *self.reinforcement_mat.density * self.reinforcement_ratio * self.area * self.thickness
        return emissions
    
class Shell(Component):          # because the volume depends on the size of the edge beams and number of panels, we need to extract panel information       
    def __init__(self, materials, area, thickness, typ_panel):
        super().__init__(materials, area, thickness)
        self.typ_panel = typ_panel
        try:
            if thickness < 2 * typ_panel.plate_thickness:
                raise ValueError
        except: print("The plate is thicker than the thickness of the shell.")
        panel_volume = typ_panel.perimeter * typ_panel.edge_beam_width * (thickness - 2 * typ_panel.plate_thickness) + area * typ_panel.panel_area * typ_panel.plate_thickness
        panel_number = area / typ_panel.panel_area
        self.volume = panel_volume * panel_number
    
    def emissions(self):
        return self.materials.emissions_kg * self.materials.density * self.volume
    def cost(self):
        return self.materials.cost_kg * self.materials.density * self.volume    

class Panel:       #this class helps define how much volume is filled in the panel by the edge beam
    def __init__(self, panel_area, panel_perimeter, plate_thickness, edge_beam_width):
        self.panel_area = panel_area
        self.plate_thickness = plate_thickness
        self.edge_beam_width = edge_beam_width
        self.perimeter = panel_perimeter


class Glazing(Component):
    # (glazing material, area m^2, thickness of glass in m, length of perimeter in m, thickness of the frame [m], frame material)
    def __init__(self, materials, area, thickness, perimeter_m, frame_thickness, frame_material):
        super().__init__(materials, area, thickness)
        self.frame_thickness = frame_thickness
        self.frame_material = frame_material
        self.perimeter_m = perimeter_m
    
    def frame_emissions(self):
        return self.frame_thickness * self.thickness * self.perimeter_m * self.frame_material.emissions_kg * self.frame_material.density
    def frame_cost(self):
        return self.frame_thickness * self.thickness * self.perimeter_m * self.frame_material.emissions_kg * self.frame_material.density
    def emissions(self):
        return super().emissions() + self.frame_emissions()
    def cost(self):
        return super().cost() + self.frame_cost()

class Materials:
    #must be fed a string as input
    def __init__(self, type):
        self.type = type
        self.emissions_kg = {"steel": 1.55, "wood": -0.25, "concrete": 0.15, "glass": 1.7, "flax": -0.1}.get(type) #kgCO2/ kg material
        self.density = {"steel": 7850, "wood": 500, "concrete": 2200, "glass": 2500, "flax": 1500}.get(type)    # kg/m^3
        self.cost_kg = {"steel": 1.0, "wood": 1.1, "concrete": 0.4, "glass": 1.2, "flax": 0.3}.get(type)         # euro/kg

# creating the shell
panel = Panel(2.5, 3, 0.01, 0.1)
shell = Shell(Materials("wood"), 45, 0.4, panel)

# creating the foundation
foundation = Foundations(Materials("concrete"), 35, 0.2)
foundation.add_reinforcement(Materials("steel"), 0.02)

#creating the glazing
glazing = Glazing(Materials("glass"), 25, 0.01, 0.2, 20, Materials("steel"))

#assembling the pavilion
pavilion = Pavilion(foundation, shell, glazing)

emissions = pavilion.emissions()

cost = pavilion.cost()

print("The pavilion has a carbon footprint of " + str(emissions) + " kg CO2 and a cost of " + str(cost) + " euros.")


