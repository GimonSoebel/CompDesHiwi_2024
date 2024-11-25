import math

class Material:
    pass

class Wood(Material):
    density = 480 #kg/m³
    cost = 1070 #€/m³
    co2_net = 20 #idk
    #longevity?

class Steel(Material):
    density = 7850 #kg/m³
    cost = 370 #€/t
    co2_net = 100
    
class Concrete(Material):
    density = 2.600 #kg/m³
    cost = 150
    co2_emission = 30


class Element:
    pass

class Column(Element):
    def __init__(self, pavilion, material, length, width): #fabrication_method, shape(rect/round)
        self.material = globals()[material.capitalize()]

        bottom_floor_height = pavilion.ground
        top_floor_height = pavilion.height
        self.height = top_floor_height - bottom_floor_height
        self.length = length
        self.width = width
        self.volume = self.height * length * width

        self.weight = self.material.density * self.volume
        self.cost = self.material.cost * self.volume #depends on formula
        print(self.cost, self.volume)

'''
    def dimensions(self, bottom_floor, top_floor, length, width):
        self.height = top_floor - bottom_floor
        self.length = length
        self.width = width
        self.volume = self.height * length * width
        self.weight = self.material.density * self.volume
'''


#
#
#

class Pavilion:
    def __init__(self):
        pass

    ground = 0

    #def determine_floors(self, floor_count):

    def input_general_parameters(self):
        self.height = float(input("Please enter height of pavilion: "))
        while True:
            self.shape = input("Please enter the shape of pavilion(circle, rectangle, triangle): ")
            if self.shape == "circle":
                #could have it's own function here
                self.radius = float(input("Please enter radius of pavilion shape: "))
                self.area = math.pi * self.radius**2
                self.perimeter = 2 * math.pi * self.radius
                return self.radius, round(self.area, 2), round(self.perimeter, 2)
            elif self.shape == "rectangle":
                self.length = float(input("Please enter length of pavilion: "))
                self.width = float(input("Please enter width of pavilion: "))
                self.area = self.length * self.width
                return self.length, self.width, self.area
            elif self.shape == "triangle":
                self.sideA = float(input("Please enter side A of pavilion: "))
                self.sideB = float(input("Please enter side B of pavilion: "))
                self.sideC = float(input("Please enter side C of pavilion: "))
                self.area = 0.5 * (self.sideA * self.sideB)
                return self.sideA, self.sideB, self.sideC, self.area
            elif self.shape == "stop":
                break
            else:
                print("Please re-enter input.")
        return self.height
    
    def input_foundation(self):
        ground = 0
        pass

    def input_column(self):
        column_material = input("Enter material: ")
        column_length = float(input("Enter length in m: "))
        column_width = float(input("Enter width in m: "))
        self.column = Column(self, column_material, column_length, column_width)
        return self.column
    
    def calculate_columns(self):
        column_support_area = 2.5
        amount_of_columns = math.ceil(self.area/column_support_area)
        columns_cost = round(amount_of_columns * self.column.cost, 2)
        columns_cost_txt = (str(columns_cost)+"€")
        return amount_of_columns, columns_cost_txt
    #Problem: attribute is not an instance of Element. I can't check all elements by their class.

    def input_beams():
        pass

    def input_roof():
        pass

    def input_facade():
        pass

    def list_of_all_elements():
        all_elements_list = set()
        pass

    def calculate_total_cost(self):
        total_cost = 0
        for attr_name in dir(self):  # Iterate over attributes
            #print(attr_name)
            attr_value = getattr(self, attr_name)
            if isinstance(attr_value, Element):  # only checks on instance for one element type
                print(attr_value.cost, attr_value.volume)
                total_cost += attr_value.cost
        return total_cost
    


def calculate_columns(area, columns):
    column_support_area = 2.5
    amount_of_columns = math.ceil(area/column_support_area)
    columns_cost = round(amount_of_columns * columns.cost, 2)
    columns_cost_txt = (str(columns_cost)+"€")
    return amount_of_columns, columns_cost_txt

'''
poo = Column(pav01, "wood", 1.5, 2.5)
print(poo.material.density)
print(poo.weight, "kg")
print(poo.cost, "€")
print(poo.height, "m")

print(calculate_columns(pav01.area, poo))
'''

pav = Pavilion()
pav.input_general_parameters()
pav.input_column()
print(pav.column)

total_cost = pav.calculate_total_cost()
print(f"Total cost of all elements: {total_cost}")

print(calculate_columns(pav.area, pav.column))