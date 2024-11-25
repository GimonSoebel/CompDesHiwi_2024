"""In this assignment, you will design a new pavilion inspired by an existing pavilion or project (it does not have to be an ITECH pavilion :D).

You will use object-oriented programming. The components of the pavilion (e.g. columns, beams, roofs, walls) will be modelled as classes and subclasses.
Each component will have parameters (such as dimensions, material type, fabrication methods) that can influence the overall cost and CO2 emissions of the pavilion.
In addition, cost estimates will be updated based on design decisions such as material selection or changes in dimensions.

1. Create the pavilion class. This is the main class that contains the components of the pavilion and provides methods for estimating the total cost, carbon footprint, etc. 
2. Component classes: Each major component (e.g. column, beam, wall) should have its own class that calculates its individual cost, carbon footprint, etc. 
3. Material subclasses: Materials will have different costs and properties that will affect those of the components. 
4. Be creative
5. Upload your assignment to ILIAS and GitHub"""




'''
PAVILLION: Seed Cathedral (UK pavillion)
Author: Heatherwick Studio
Year: 2010


Generic Components:

Frame:
material = wood
lenght = 16
width = 16
height = 20
thicknes = 0.25

Column:
material = steel
lenght = 0.10
width = 0.10
height = 20
thicknes = 0.01
amount = 4

Beam:
material = steel
lenght = 16
width = 0.10
height = 0.20
thicknes = 0.01
amount = 4

Filament:
material = acrylic
lenght = 7.5
width = 0.04
height = 0.04
thicknes = 0.04
amount = 60000



'''

#UNITS: meters

#USER INPUTS

print ("")
print ("Seed Cathedral Calculator")
print ("")
print ("Units: meters")
print ("")
print ("Input material (wood, steel, concrete, acrylic)")
inp_frame_m = input ('frame material:')
inp_frame_l = input ('frame lenght:')
inp_frame_w = input ('frame width: ')
inp_frame_h = input ('frame height: ')
inp_frame_t = input ('frame thickness: ')
print ("")

print ("Input material (wood, steel, concrete, acrylic)")
inp_column_m = input ('column material:')
inp_column_l =  input ('column lenght:')
inp_column_w =  input ('column width:')
inp_columm_h = input ('column height: ')
inp_columm_t = input ('column thickness: ')
inp_column_amount = input ('column amount: ')
print ("")

print ("Input material (wood, steel, concrete, acrylic)")
inp_beam_m = input ('beam material:')
inp_beam_l = input ('beam lenght:')
inp_beam_w = input ('beam width:')
inp_beam_h = input ('beam height: ')
inp_beam_t = input ('beam thickness: ')
inp_beam_amount = input ('beam amount: ')
print ("")

print ("Input material (wood, steel, concrete, acrylic)")
inp_filament_m = input ('filament material:')
inp_filament_l = input ('filament lenght:')
inp_filament_w = input ('filament width:')
inp_filament_h = input ('filament height: ')
inp_filament_t = input ('filament thickness: ')
inp_filament_amount = input ('filament amount: ')


###Variables

#Price/m3
#C02 emission kg/m3

wood_price = 500
wood_carbon = 30

steel_price = 5495
steel_carbon = 15000

concrete_price = 150
concrete_carbon = 200

acrylic_price = 7140
acrylic_carbon = 5000


###Material Class

class Material:
    'Includes the price and C02 Emission per m3'
    def __init__(self, price, carbon):

        self.price = price
        self.carbon = carbon


###Materials Instances

wood = Material (wood_price, wood_carbon)
steel = Material (steel_price, steel_carbon)
concrete = Material (concrete_price, concrete_carbon)
acrylic = Material (acrylic_price, acrylic_carbon)

material_inst = {'wood':wood, 'steel':steel, 'concrete':concrete, 'acrylic':acrylic}


###Component Class

class Components:
    def __init__(self, lenght, width, height, thickness, material, amount):
        
        self.lenght = lenght
        self.width = width
        self.height = height
        self.thickness = thickness
        self.material = material
        self.amount = amount

    def total_cost (self):

        return (self.material.price * self.amount)
    
    def total_carbon (self):

        return (self.material.carbon * self.amount)
    


#Components Instances

frame = Components (float(inp_frame_l),
                    float (inp_frame_w),
                    float (inp_frame_h),
                    float (inp_frame_t),
                    material_inst[str(inp_frame_m)],
                    1)

column = Components (float (inp_column_l),
                     float (inp_column_w),
                     float(inp_columm_h),
                     float(inp_columm_t),
                     material_inst[str(inp_column_m)],
                     int (inp_column_amount))

beam = Components (float(inp_beam_l),
                  float (inp_beam_w),
                   float (inp_beam_h),
                   float (inp_beam_t),
                   material_inst[str(inp_beam_m)],
                   int (inp_beam_amount))

filament = Components(float(inp_filament_l),
                      float (inp_filament_w),
                      float (inp_filament_h),
                      float (inp_filament_t),
                      material_inst[str(inp_filament_m)],
                      int (inp_filament_amount))



pav_components = [frame, column, beam, filament]
pav_cost = []
pav_carbon_emit = []


###Pavillion Class

class Pavillion:
    'Includes a parameters that reference a list with all the components instances'

    def __init__(self,components):
        
        self.components = components

    def total_cost (self):

       for i in self.components:
            
            m3 = round ((i.lenght * i.width * i.height), 2)

            m3_thick = (m3) - (round ((i.lenght - i.thickness) * (i.width - i.thickness) * (i.height - i.thickness), 2))
           
            pav_cost.append (round((((i.material.price) * m3_thick) * (i.amount)),2))
       
       return sum (pav_cost)
    
    def total_carbon (self):

       for i in self.components:
           
            m3 = round ((i.lenght * i.width * i.height), 2)
            m3_thick = (m3) - (round ((i.lenght - i.thickness) * (i.width - i.thickness) * (i.height - i.thickness), 2))
            pav_carbon_emit.append (round ((((i.material.carbon) * m3_thick) * (i.amount)),2))
       
       return sum (pav_carbon_emit)

           

#Pavilion Instance 
# (Seed Cathedral)

seed_cathedral = Pavillion (pav_components)

#OUTPUT

print ("")
print ("Seed Cathedral Total Cost")
print ('$ ' + str(seed_cathedral.total_cost()))
print ("")
print ("Cost per Component (frame, column, beam, filaments)")
print (pav_cost)
print ("")

print ("Seed Cathedral Total C02 emitions")
print (str(seed_cathedral.total_carbon()) + 'kg')
print ("")
print ("Emissions per Component (frame, column, beam, filaments)")
print (pav_carbon_emit)
print ("")