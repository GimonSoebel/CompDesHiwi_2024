import math
from InquirerPy import inquirer

def float_input(user_input):
    while True:
        try:
            number = float(user_input)
            return number
        except ValueError:
            user_input = input("Please enter a valid number: ")

class Material:
    density = 0
    cost = 0
    co2_emissions = 0


class Wood(Material):
    density = 480  # kg/m³
    cost = 1070  # €/m³
    co2_emissions = 110  # kg/m³


class Steel(Material):
    density = 7850  # kg/m³
    cost = 7700  # €/m³
    co2_emissions = 18500  # kg/m³


class Concrete(Material):
    density = 2600  # kg/m³
    cost = 150  # €/m³
    co2_emissions = 635  # kg/m³

#
#
#

class Element:
    def __init__(self):
        self.name = ""
        self.material = None
        self.volume = 0
        self.mass = 0
        self.cost = 0
        self.emissions = 0

    @staticmethod
    def choose_material():
        list_materials = [cls.__name__ for cls in Material.__subclasses__()]
        answer = inquirer.select(
            message="Choose the material:",
            choices=list_materials,
        ).execute()
        return globals()[answer.capitalize()]

    def __repr__(self):
        return self.name


class Foundation(Element):
    def input_dimensions(self, pavilion):
        self.name = f"{pavilion.pavilion_elements_index:02}_{self.__class__.__name__}"
        self.material = self.choose_material()
        self.area = pavilion.area
        self.thickness = float_input(input("Enter depth/thickness in m: "))
        self.volume = self.area * self.thickness
        self.mass = self.material.density * self.volume
        self.cost = round((self.material.cost * self.volume), 2)
        self.emissions = round((self.material.co2_emissions * self.volume), 2)
        print(f"The foundation has a volume of {self.volume} m³ and a cost of {self.cost} €.")

class Column(Element): #automatically takes height from pavilion dimensions
    def input_dimensions(self, pavilion):
        self.name = (f"{pavilion.pavilion_elements_index:02}_{self.__name__}")
        self.material = self.choose_material()
        self.length = float_input(input("Enter length in cm: "))
        self.width = float_input(input("Enter width in cm: "))
        bottom_floor_height = pavilion.ground
        top_floor_height = pavilion.height
        self.height = top_floor_height - bottom_floor_height
        self.volume = self.height * self.length*0.01 * self.width*0.01
        self.mass = self.material.density * self.volume
        self.cost = round((self.material.cost * self.volume), 2)
        self.emissions = round((self.material.co2_emissions * self.volume), 2)
        print("Cost:", self.cost, "Volume:", self.volume)


class Roof(Element):
    roof_shapes_circle = ['flat', 'dome', 'polygonal']
    roof_shapes_rectangle = ['flat', 'hip', 'gable', 'pyramid']
    roof_shapes_triangle = ['flat', 'polygonal']

    def choose_roof_shape(self, pavilion):
        print("Warning: Certain roof types aren't available with certain pavilion shapes.")
        print(pavilion.shape)
        if pavilion.shape == "circle":
            roof_answer = inquirer.select(
                message = "Choose a roof shape:",
                choices = self.roof_shapes_circle,
            ).execute()
        elif pavilion.shape == "rectangle":
            roof_answer = inquirer.select(
                message = "Choose a roof shape:",
                choices = self.roof_shapes_rectangle,
            ).execute()
        elif pavilion.shape == "triangle":
            roof_answer = inquirer.select(
                message = "Choose a roof shape:",
                choices = self.roof_shapes_triangle,
            ).execute()
        else:
            "Some roof types are not possible with certain shapes."
        return roof_answer
    
    def input_dimensions(self, pavilion):
        roof_answer = self.choose_roof_shape(pavilion)

        if roof_answer == "flat":
            self.area = pavilion.area

        elif roof_answer == "hip": # assuming it's symmetrical
            print(f"A reminder: Your pavilion dimensions are {pavilion.length}m and {pavilion.width}m.")
            #could probably generate something with overhang
            self.length = float_input(input("Length of roof in m: "))
            self.span = float_input(input("Span(width) of roof in m: "))
            self.height = float_input(input("Height of roof in m: ")) #or ask for pitch
            while True:
                self.ridge_length = float_input(input("Length of roof ridge in m: "))
                if self.ridge_length > self.length:
                    print("Ridge of roof cannot exceed length of roof. Try again:")
                else:
                    break
            length_height = math.sqrt(((self.span/2)**2) * self.height)
            span_height = math.sqrt(((self.length/2)**2) * self.height)
            trapezoid_area = (self.length + self.ridge_length)/2 * length_height
            triangle_area = (self.span * span_height)/2
            self.area = trapezoid_area*2 + triangle_area*2

        elif roof_answer == "gable": #could just combine with hip
            print(f"A reminder: Your pavilion dimensions are {pavilion.length}m and {pavilion.width}m.")
            self.length = float_input(input("Length of roof in m: "))
            self.span = float_input(input("Span(width) of roof in m: "))
            self.height = float_input(input("Height of roof in m: "))
            length_height = math.sqrt(((self.span/2)**2) * self.height)
            self.area = (self.length * length_height)*2 + (self.span * self.height)*2

        elif roof_answer == "dome":
            print(f"A reminder: Your pavilion has a diameter of {pavilion.radius*2}m.")
            self.height = float_input(input("Height of dome in m: "))
            self.area = 2 * pavilion.radius * self.height * math.pi
            
        else:
            print("We're still working on that...") #have to start from beginning again

        self.name = (f"{pavilion.pavilion_elements_index:02}_{self.__name__}")
        self.material = self.choose_material()
        self.thickness = float_input(input("Enter thickness of roof in m: "))
        self.area = round(self.area, 2)
        self.volume = round(self.area * self.thickness, 2)
        self.mass = round(self.material.density * self.volume, 2)
        self.cost = round((self.material.cost * self.volume), 2)
        self.emissions = round((self.material.co2_emissions * self.volume), 2)
        print(f"The {roof_answer} roof has a surface are of {self.area}m2 and a volume of {self.volume}m3")

#
#
#

class Pavilion:
    def __init__(self):
        self.ground = 0
        self.height = 0
        self.shape = ""
        self.radius = 0
        self.length = 0
        self.width = 0
        self.area = 0
        self.pavilion_elements = []
        self.pavilion_elements_index = 0
        self.possible_shapes = ["circle", "rectangle", "triangle"]

    def input_general_parameters(self):
        print("Inputting: General Parameters...")
        self.height = float_input(input("Please enter the clear height of the pavilion: "))
        self.shape = inquirer.select(
            message="Please choose the shape of the pavilion:",
            choices=self.possible_shapes,
        ).execute()
        if self.shape == "circle":
            self.radius = float_input(input("Please enter the radius of the pavilion shape in m: "))
            self.area = round((math.pi * self.radius**2), 2)
        elif self.shape == "rectangle":
            self.length = float_input(input("Please enter the length of the pavilion in m: "))
            self.width = float_input(input("Please enter the width of the pavilion in m: "))
            self.area = round((self.length * self.width), 2)
        elif self.shape == "triangle":
            base = float_input(input("Please enter the base of the triangle in m: "))
            height = float_input(input("Please enter the height of the triangle in m: "))
            self.area = round((0.5 * base * height), 2)
        else:
            raise ValueError("Invalid shape.")
        print(f"Your {self.shape} pavilion is {self.height} m high and has an area of {self.area} m².\n")

    def input_building_elements(self):
        list_elements = [cls.__name__ for cls in Element.__subclasses__()]
        answer = inquirer.select(
            message="What element do you want to add?",
            choices=list_elements,
        ).execute()
        print("You chose:", answer)
        element_class = globals()[answer]
        if any(isinstance(x, element_class) for x in self.pavilion_elements):
            print(f"Careful! You already have a {answer}. Do you want to add a new one or go back?")
            confirm = inquirer.confirm(message="Yes for proceed, No for go back.").execute()
            if confirm == True:
                element_instance = element_class()
                element_instance.input_dimensions(self)
        else:
            element_instance = element_class()
            element_instance.input_dimensions(self)
        self.pavilion_elements.append(element_instance)
        self.pavilion_elements_index += 1
        print(f"You created: {element_instance.name}")

    def calculate_total_cost(self):
        return sum(element.cost for element in self.pavilion_elements)

    def calculate_total_emissions(self):
        return sum(element.emissions for element in self.pavilion_elements)


### Run the Program
if __name__ == "__main__":
    print("Generating pavilion...")
    pav = Pavilion()
    pav.input_general_parameters()
    print("Inputting: Building Elements...")
    while True:
        confirm = inquirer.confirm(message="Do you want to add another building element?").execute()
        if confirm:
            pav.input_building_elements()
            print("")
        else:
            break
    print("Finishing... List of all elements:", pav.pavilion_elements)
    total_cost = pav.calculate_total_cost()
    total_emissions = pav.calculate_total_emissions()
    print(f"Total cost of all elements: {total_cost}€")
    print(f"Total emissions of all elements: {total_emissions}kg CO₂")
