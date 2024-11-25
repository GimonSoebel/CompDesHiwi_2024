import random as rd
# The material property: name, unit price, fabrication method, CO2 emissions
class Material():
    #initialize 
    def __init__(self, name, unit_price, fab_method, CO2_emi):
        self.name = name
        self.unit_price = unit_price
        self.fab_method = fab_method
        self.CO2_emi = CO2_emi
    
    #override
    def unit_cost(self):
        return self.unit_price
    
    def unit_emi(self):
        return self.CO2_emi
    
    def __str__(self):
        return f"The material name is {self.name}, the unit cost is {round(self.unit_cost(),2)}, the fabrication method is {self.fab_method}, and the unit CO2 emission is {round(self.unit_emi(),2)}."

#Timber
class Timber(Material):
    #initialize
    def __init__(self, name, unit_price, fab_method, CO2_emi, timber_type):
        super().__init__(name, unit_price, fab_method,CO2_emi)
        self.timber_type = timber_type

    def unit_cost(self):
        return self.unit_price * 2
    
    def unit_emi(self):
        return self.CO2_emi * 0.9

#Natural-fibre polymer composites
class NFPC(Material):
    #initialize
    def __init__(self, name, unit_price, fab_method,CO2_emi):
        super().__init__(name, unit_price, fab_method,CO2_emi)
    
    #override
    def unit_cost(self):
        return self.unit_price * 3
    
    def unit_emi(self):
        return self.CO2_emi * 0.75

##################Instantiate#####################
print("INSTANTIATING THE MATERIAL>>>>")
timber1 = Timber("timber1",20,"Laser Cutting",30,"Reclaimed Timber")
print(timber1)
timber2 = Timber("timber2",30,"Robotic Milling",30,"Reclaimed Timber")
print(timber2)
nfpc1 = NFPC("nfpc1",80,"Dual Robotic Winding",10)
print(nfpc1)
print()
##################Instantiate#####################

# The component property: name, material's unit cost, dimension; The method: calculate its cost
class Component():
    def __init__(self,name,base_area,height,material):
        self.name = name
        self.base_area = base_area
        self.height = height
        self.material = material

    def CalCost(self):
        calcost = self.material.unit_cost()* self.base_area*self.height
        return calcost

    def CalCarbon(self):
        calCarbon = self.material.unit_emi()*self.base_area*self.height
        return calCarbon
    
    def __str__(self):
        return f"The component name is {self.name}, the cost is {round(self.CalCost(),2)}, and the carbon emission is {round(self.CalCarbon(),2)}."

class Roof(Component):
    def __init__(self, name, base_area, height, material):
        super().__init__(name, base_area, height, material)
    
    #with manual cost during installation
    def CalCost(self):
        calcost = (self.material.unit_cost()+90)*self.base_area*self.height
        return calcost

class Fiber(Component):
    def __init__(self,name,length,material):
        self.name = name
        self.length = length
        self.material = material

    #with loss/waste during tests and electronic/manual cost
    def CalCost(self):
        return (self.material.unit_cost()+70)*self.length*1.5
    
    def CalCarbon(self):
        return self.material.unit_emi()*self.length

class Column(Component):
    def __init__(self, name, base_area, height, material):
        super().__init__(name, base_area, height, material)
    
    #with manual cost during installation
    def CalCost(self):
        return (self.material.unit_cost()+50)*self.base_area*self.height
    
class Frames(Component):
    def __init__(self, name, base_area, height, material):
        super().__init__(name, base_area, height, material)

    #with loss/waste during tests and electronic/manual cost
    def CalCost(self):
        return (self.material.unit_cost()+30)*self.base_area*self.height*1.1

##################Instantiate#####################
print("INSTANTIATING THE COMPONENTS>>>>")
componentList1 = []

roof1 = Roof("roof1",8,0.3,timber1)
componentList1.append(roof1)
print(roof1)
print()
fiber1 = Fiber("fiber1",50,nfpc1)
componentList1.append(fiber1)
print(fiber1)
print()

for i in range(0,3):
    hei = round(rd.uniform(3,4),2)
    columItem = Column(f"column{i}",0.3,hei,timber1)
    print(columItem)
    componentList1.append(columItem)
print()

for j in range(0,8):
    hei = round(rd.uniform(0.8,1.5),2)
    frameItem = Frames(f"frame{j}",0.2,hei,timber2)
    print(frameItem)
    componentList1.append(frameItem)
print()
##################Instantiate#####################


#Create a pavilion class > contains all components and calculates the total co2 emissions
class Pavilion:   
    def __init__(self, project_name,componentList):
        self.projec_name = project_name
        self.componentList = componentList

    def TotalCost(self):
        totalSum = 0
        for item in self.componentList:
            totalSum += item.CalCost()
        return totalSum

    def TotalCarbon(self):
        totalSum = 0
        for item in self.componentList:
            totalSum += item.CalCarbon()
        return totalSum

    def __str__(self):
        return f"The project name is {self.projec_name}, the totalcost is {round(self.TotalCost(),2)}, the total carbon emission is {round(self.TotalCarbon(),2)}."
    
##################Instantiate#####################
print("INSTANTIATING THE PROJECT>>>>")
pavilion1 = Pavilion("Research Pavilion 2024",componentList1)
print(pavilion1)
print()
##################Instantiate#####################