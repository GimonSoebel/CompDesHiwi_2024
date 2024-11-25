"""In this assignment, you will design a new pavilion inspired by an existing pavilion or project (it does not have to be an ITECH pavilion :D).

You will use object-oriented programming. The components of the pavilion (e.g. columns, beams, roofs, walls) will be modelled as classes and subclasses.
Each component will have parameters (such as dimensions, material type, fabrication methods) that can influence the overall cost and CO2 emissions of the pavilion.
In addition, cost estimates will be updated based on design decisions such as material selection or changes in dimensions.

1. Create the pavilion class. This is the main class that contains the components of the pavilion and provides methods for estimating the total cost, carbon footprint, etc. 
2. Component classes: Each major component (e.g. column, beam, wall) should have its own class that calculates its individual cost, carbon footprint, etc. 
3. Material subclasses: Materials will have different costs and properties that will affect those of the components. 
4. Be creative
5. Upload your assignment to ILIAS and GitHub"""

"""
Pavilion is inspired by Frida Escobedo Serpentine Pavilion which features concrete tiles, steel rods, steel plates, and polished stainless steel panels
"""

class Pavilion:
  """This class creates a pavilion based on a collection of components"""
  def __init__(self, components: list, pavilion_name: str):
    self.components = components
    self.pavilion_name = pavilion_name

  def total_cost(self):
    pavilion_cost = 0
    for component in self.components:
      pavilion_cost += component.indiv_cost()
    
    pavilion_cost = round(pavilion_cost, 2)
    return pavilion_cost

  def total_carbon_footprint(self):
    pavilion_carbon = 0
    for component in self.components:
      pavilion_carbon += component.indiv_carbon()
    
    pavilion_carbon = round(pavilion_carbon, 2)
    return pavilion_carbon
  
  def total_volume(self):
    pavilion_vol = 0
    for component in self.components:
      pavilion_vol += component.calc_volume()
    
    return pavilion_vol
  
  def print_pavilion(self):
    total_walls = 0
    total_roofs = 0

    for component in self.components:
      if (component.type == 'Wall'):
        total_walls += 1
      elif (component.type == 'Roof'):
        total_roofs += 1
    
    print (f"""
    {self.pavilion_name} is a pavilion with {total_walls} wall(s), {total_roofs} roof(s), and 1 foundation.
    It will cost €{self.total_cost()} to build, and will have a total carbon footprint of {self.total_carbon_footprint()} kg CO2e.
    The total volume of all the components and elements used to build this pavilion is {self.total_volume()} mm^3.
    """)

# -------------------------------------------------------------------------------
# Create Overall class of pavilion components
"""
Structure:
  Component
    Wall
      Tiles
      Rods
      Plates
    Roof
      Panels
    Foundation
      Slabs
"""
class Component:
  """This class creates a Component of the Pavilion to add"""
  def __init__(self, cross_section_area, length, mass):
    self.cross_section_area = cross_section_area
    self.length = length
    self.mass = mass

  def indiv_cost(self):
    pass

  def indiv_carbon(self):
    pass

  def calc_volume(self):
    return self.cross_section_area*self.length
  
# Component Subclasses
class Wall(Component):
  """This class creates a wall made up of a list of tiles, rods, and plates"""
  def __init__(self, cross_section_area, length, mass, element_list: list):
    super().__init__(cross_section_area, length, mass)

    self.element_list = element_list
    self.type = 'Wall'
  
  def indiv_cost(self):
    wall_cost = 0
    for element in self.element_list:
      wall_cost += element.indiv_cost()
    
    return wall_cost

  def indiv_carbon(self):
    wall_carbon = 0
    for element in self.element_list:
      wall_carbon += element.indiv_carbon()
    
    return wall_carbon

  def calc_volume(self):
    wall_volume = 0
    for element in self.element_list:
      wall_volume += element.calc_volume()

    return wall_volume 
    
class Roof(Component):
  """This class creates a roof made up of a list of panels"""
  def __init__(self, cross_section_area, length, mass, element_list: list):
    super().__init__(cross_section_area, length, mass)

    self.element_list = element_list
    self.type = 'Roof'
  
  def indiv_cost(self):
    roof_cost = 0
    for element in self.element_list:
      roof_cost += element.indiv_cost()
    
    return roof_cost

  def indiv_carbon(self):
    roof_carbon = 0
    for element in self.element_list:
      roof_carbon += element.indiv_carbon()
    
    return roof_carbon

  def calc_volume(self):
    roof_volume = 0
    for element in self.element_list:
      roof_volume += element.calc_volume()

    return roof_volume 

class Foundation(Component):
  """This class creates a foundation made up of a list of slabs"""
  def __init__(self, cross_section_area, length, mass, element_list: list):
    super().__init__(cross_section_area, length, mass)

    self.element_list = element_list
    self.type = 'Foundation'
  
  def indiv_cost(self):
    found_cost = 0
    for element in self.element_list:
      found_cost += element.indiv_cost()
    
    return found_cost

  def indiv_carbon(self):
    found_carbon = 0
    for element in self.element_list:
      found_carbon += element.indiv_carbon()
    
    return found_carbon

  def calc_volume(self):
    found_volume = 0
    for element in self.element_list:
      found_volume += element.calc_volume()

    return found_volume

# Component Subclass Elements
class ComponentElement(Component):
  def __init__(self, cross_section_area, length, mass, material_choice):
    super().__init__(cross_section_area, length, mass)

    self.material_choice = material_choice

  def indiv_cost(self):
    return self.material_choice.cost * self.mass
  
  def indiv_carbon(self):
    return self.material_choice.carbon * self.mass

# Wall Elements:
class Tile(ComponentElement):
  def __init__(self, cross_section_area, length, mass, material_choice):
    super().__init__(cross_section_area, length, mass, material_choice)

    self.type = 'Tile'

class Rod(ComponentElement):
  def __init__(self, cross_section_area, length, mass, material_choice):
    super().__init__(cross_section_area, length, mass, material_choice)

    self.type = 'Rod'

class Plate(ComponentElement):
  def __init__(self, cross_section_area, length, mass, material_choice):
    super().__init__(cross_section_area, length, mass, material_choice)

    self.type = 'Plate'

# Roof Elements:
class Panel(ComponentElement):
  def __init__(self, cross_section_area, length, mass, material_choice):
    super().__init__(cross_section_area, length, mass, material_choice)

    self.type = 'Panel'

# Foundation Elements
class Slab(ComponentElement):
  def __init__(self, cross_section_area, length, mass, material_choice):
    super().__init__(cross_section_area, length, mass, material_choice)

    self.type = 'Slab'

# -------------------------------------------------------------------------------
# Create Material classes
class Material():
  """This class defines a material along with its cost per kg, and carbon footprint in (kg co2e per kg of material)"""
  def __init__(self, cost: float):
    self.cost = cost

# Create Material Subclasses
# Source of carbon footprint information: https://legacy.winnipeg.ca/finance/findata/matmgt/documents/2012/682-2012/682-2012_Appendix_H-WSTP_South_End_Plant_Process_Selection_Report/Appendix%207.pdf 
class Concrete(Material):
  def __init__(self, cost: float):
    super().__init__(cost)

    self.carbon = 0.15 #kg CO2e eq per 1 kg of concrete
    self.type = 'Concrete'

class ReinforcedConcrete(Concrete):
  def __init__(self, cost: float):
    super().__init__(cost)

    self.carbon = 0.36 #kg CO2e eq per 1 kg of concrete
    self.type = 'Reinforced Concrete'

class Steel(Material):
  def __init__(self, cost: float):
    super().__init__(cost)

    self.carbon = 1.77 #kg CO2e eq per 1 kg of steel
    self.type = 'Steel'

class StainlessSteel(Steel):
  def __init__(self, cost: float):
    super().__init__(cost)

    self.carbon = 6.15 #kg CO2e eq per 1 kg of steel 
    self.type = 'Stainless Steel'

# -------------------------------------------------------------------------------
# Create Pavilion creation function and helper functions
def create_pavilion(name: str):
  """This function creates your pavilion with all of its subcomponents. Input the name of your pavilion to start."""
  #Booleans for try and except loops.
  walls_inputed = False
  roofs_inputed = False  
  component_list = []

  # Create Walls
  while (walls_inputed == False):
    try:
      total_walls = int(input("How many walls are in this pavilion?: "))
      walls_inputed = True
    except ValueError:
      print("Please input an integer")
  
  for i in range (0, total_walls):
    is_identical = True
    if (i > 0):
      while (is_identical == True):
        repeat_component = input('Is this wall the same as the previous wall?(y/n): ')
        repeat_component = repeat_component.lower()

        if (repeat_component == 'y'):
          new_wall = component_list[-1]
          print('Added copy of previous wall to components list.')
          is_identical = False
        elif (repeat_component == 'n'):
          new_wall = create_wall()
          is_identical = False
        else:
          print("Please input 'y' or 'n'.")
    else:
      new_wall = create_wall()

    component_list.append(new_wall)

  # Create Roofs
  while (roofs_inputed == False):
    try:
      total_roofs = int(input("How many roofs are in this pavilion?: "))
      roofs_inputed = True
    except ValueError:
      print("Please input an integer") 
  
  for i in range (0, total_roofs):
    is_identical = True
    if (i > 0):
      while (is_identical == True):
        repeat_component = input('Is this roof the same as the previous roof?(y/n): ')
        repeat_component = repeat_component.lower()

        if (repeat_component == 'y'):
          new_roof = component_list[-1]
          print('Added copy of previous roof to components list.')
          is_identical = False
        elif (repeat_component == 'n'):
          new_roof = create_roof()
          is_identical = False
        else:
          print("Please input 'y' or 'n'.")
    else:
      new_roof = create_roof()

    component_list.append(new_roof)
  
  # Number of Foundations is assumed to be 1
  # Create Foundation
  new_foundation = create_foundation()
  component_list.append(new_foundation)
  
  print('Created Pavilion!')
  return Pavilion(component_list, name)

# ---------------------------------------------------
def create_wall():
  """This function generates all the walls in the pavilion"""
  # Determine user's desired number of tiles, rods, and plates
  #Booleans for try and except loops
  tiles_inputed = False
  rods_inputed = False
  plates_inputed = False 
  element_list = []

  while (tiles_inputed == False):
    try:
      total_tiles = int(input("How many tiles are in this wall?: "))
      tiles_inputed = True
    except ValueError:
      print("Please input an integer.")
  
  # Create Tiles
  tiles_to_add = create_elements('Tile', total_tiles)
  for tile in tiles_to_add:
    element_list.append(tile)

  
  while (rods_inputed == False):
    try:
      total_rods = int(input("How many rods are in this wall?: "))
      rods_inputed = True
    except ValueError:
      print("Please input an integer.")

  # Create Rods
  rods_to_add = create_elements('Rod', total_rods)
  for rod in rods_to_add:
    element_list.append(rod)

  while (plates_inputed == False):
    try:
      total_plates = int(input("How many plates are in this wall?: "))
      plates_inputed = True
    except ValueError:
      print("Please input an integer.")

  # Create Plates
  plates_to_add = create_elements('Plate', total_plates)
  for plate in plates_to_add:
    element_list.append(plate)
  
  #initialize variables for cross-section, length, and mass
  wall_cross_section = 0
  wall_length = 0
  wall_mass = 0 

  for element in element_list:
    wall_cross_section += element.cross_section_area
    wall_length += element.length
    wall_mass += element.mass

  print('Wall created.')
  return Wall(wall_cross_section, wall_length, wall_mass, element_list)

# ---------------------------------------------------
def create_roof():
  """This function generates all the roofs in the pavilion"""
  # Determine user's desired number of panels
  panels_inputed = False #Boolean for try and except loop
  element_list = []

  while (panels_inputed == False):
    try:
      total_panels = int(input("How many panels make up this roof?: "))
      panels_inputed = True
    except ValueError:
      print("Please input an integer.")
  
  # Create Panels
  panels_to_add = create_elements('Panel', total_panels)
  for panel in panels_to_add:
    element_list.append(panel)
  
  roof_cross_section = 0 
  roof_length = 0
  roof_mass = 0 #initialize variables for cross-section, length, and mass

  for element in element_list:
    roof_cross_section += element.cross_section_area
    roof_length += element.length
    roof_mass += element.mass

  print('Roof created.')
  return Roof(roof_cross_section, roof_length, roof_mass, element_list)

# ---------------------------------------------------
def create_foundation():
  """This function generates all the foundations in the pavilion"""
  # Determine user's desired number of slabs
  slabs_inputed = False #Boolean for try and except loop
  element_list = []

  while (slabs_inputed == False):
    try:
      total_slabs = int(input("How many slabs are in this foundation?: "))
      slabs_inputed = True
    except ValueError:
      print("Please input an integer.")
  
  # Create Slabs
  slabs_to_add = create_elements('Slab', total_slabs)
  for slab in slabs_to_add:
    element_list.append(slab)
  
  #initialize variables for cross-section, length, and mass
  found_cross_section = 0
  found_length = 0
  found_mass = 0 

  for element in element_list:
    found_cross_section += element.cross_section_area
    found_length += element.length
    found_mass += element.mass

  print('Foundation created.')
  return Foundation(found_cross_section, found_length, found_mass, element_list)

# ---------------------------------------------------
def create_elements(element_type: str, total_elements: int):
  """This function creates elements that belong to larger scale components"""
  #Define input parameters for element
  #Booleans for try and except loops
  valid_cross = False 
  valid_length = False 
  valid_mass = False 
  valid_material = False
  valid_cost = False 

  while (valid_cross == False):
    try:
      cross_section = float(input("What is the cross-sectional area of these {}s in sq. mm?: ".format(element_type.lower())))
      valid_cross = True
    except ValueError:
      print("Please input a number or float.")

  while (valid_length == False):
    try:
      length = float(input("What is the length of these {}s in mm?: ".format(element_type.lower())))
      valid_length = True
    except ValueError:
      print("Please input a number or float.")
  
  while (valid_mass == False):
    try:
      mass = float(input("What is the mass of these {}s in kg?: ".format(element_type.lower())))
      valid_mass = True
    except ValueError:
      print("Please input a number or float.")
  
  while (valid_material == False):
    try:
      material_choice = int(input("""
      Choose the material for these {}s:
      1. Concrete
      2. Reinforced Concrete
      3. Steel
      4. Stainless Steel:
      """.format(element_type.lower())))

      if (material_choice < 1 or material_choice > 4):
        print("Please input 1, 2, 3, or 4.")
      else:
        valid_material = True
    except ValueError:
      print("Please input 1, 2, 3, or 4.")
  
  while (valid_cost == False):
    try:
      cost = float(input("What is the cost of this material per kg in Euros?: "))
      cost = round(cost, 2)
      valid_cost = True
    except ValueError:
      print("Please input a number or float")

  # Create material class based on last two inputs
  if (material_choice == 1):
    material_choice = Concrete(cost)
  elif(material_choice == 2):
    material_choice = ReinforcedConcrete(cost)
  elif(material_choice == 3):
    material_choice = Steel(cost)
  else:
    material_choice = StainlessSteel(cost)

  # Create element based off input string
  elements_created = []
  for i in range(0, total_elements):
    if (element_type == 'Tile'):
      new_element = Tile(cross_section, length, mass, material_choice)
    elif (element_type == 'Rod'):
      new_element = Rod(cross_section, length, mass, material_choice)
    elif (element_type == 'Plate'):
      new_element = Plate(cross_section, length, mass, material_choice)
    elif (element_type == 'Panel'):
      new_element = Panel(cross_section, length, mass, material_choice)
    elif (element_type == 'Slab'):
      new_element = Slab(cross_section, length, mass, material_choice)
    
    elements_created.append(new_element)
  
  print("{} {}s created successfully! Each has a cross-section of {} mm^2, a length of {} mm, a mass of {} kg, and are made of {}. Each costs €{}.".format(total_elements, element_type.lower(), cross_section, length, mass, material_choice.type.lower(), round(cost*mass, 2)))
  return elements_created

# -------------------------------------------------------------------------------
name = input("What is the name of your pavilion?: ")
new_pavilion = create_pavilion(name)
new_pavilion.print_pavilion()
