from .MyPavilion_cls import MyPavilion
from .Level_cls import Level


class Component(MyPavilion):
    elements = []  # Class attribute to store all elements
    def __init__(self, height: float, width: float, length: float, name, material, reference_level: 'Level', vertical_offset):
        super().__init__()
        self.height = height
        self.width = width
        self.length = length
        self.name = name
        self.material = material
        self.reference_level = reference_level
        self.vertical_offset = vertical_offset
        Component.elements.append(self)  

    def get_position_height(self):
       # Calculate the starting height from 0.00 based on the reference level and the vertical offset 
       return self.reference_level.baseheight + self.vertical_offset
    
    def get_name(self):
        print(self.name)
    
    def set_name(self, new_name):
        self.name = new_name

    def get_material_name(self):
        return self.material.name    

    def get_cost(self):
        volume = self.get_volume()
        material_cost = self.material.get_cost_per_m3()
        cost = volume * material_cost
        return cost

    def get_volume(self):
        volume = self.height*self.length*self.width
        return volume
    
    def get_weight(self):
        volume = self.get_volume()
        material_density = self.material.get_density()
        return volume * material_density            
    
    @classmethod
    def calculate_total_cost(cls):
        """Calculate the total cost of all elements in the pavilion."""
        total_cost = 0
        for element in cls.elements:
            total_cost += element.get_cost()
        return total_cost
    
class Column(Component):
    def __init__(self, height: float, width: float, length: float, name, reference_level: 'Level', targetlevel: 'Level', vertical_offset, material):
        super().__init__(height, width, length, name, material, reference_level, vertical_offset)
        self.targetlevel = targetlevel
    
    def return_(self):
        print(self.name + "_test")

    def get_base_height(self):
        return self.reference_level.baseheight

class Beam(Component):
    def __init__(self, height: float, width: float, length: float, name, material, reference_level: 'Level', vertical_offset):
        super().__init__(height, width, length, name, material, reference_level, vertical_offset)
        self.reference_level = reference_level
    
    def return_(self):
        print(self.name + "_test")

    def get_base_height(self):
        return self.reference_level.baseheight
    
class Floor(Component):
    def __init__(self, height, width, length, name, material, reference_level, vertical_offset):
        super().__init__(height, width, length, name, material, reference_level, vertical_offset)
