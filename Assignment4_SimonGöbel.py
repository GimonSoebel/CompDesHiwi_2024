"""
1. Create a base class Shape (empty class) with methods for calculating area and perimeter
These methods are abstract and need to be implemented by child classes.
"""

class Shape :

    def calculate_area(self):
        pass
    
    def calculate_perimeter(self):
        pass

"""
2. Implement specific shapes (e.g., Circle, Rectangle, Triangle) as child classes of Shape and define the attributes needed for each child classes of Shape
using def_init_() method (e.g. for calculating area and perimeter of a circle attribute radius is needed).
Calculate the total area and perimeter of all previous shapes identifying a ShapeCollection class.
"""

class Circle(Shape) :

    def __init__(self, radius) :
        self.radius = radius
    
    def calculate_area(self) :
        return 3.14 * self.radius ** 2
    
    def calculate_perimeter(self) :
        return 2 * 3.14 * self.radius
 
class Rectangle(Shape) :

    def __init__(self, length, width) :
        self.length = length
        self.width = width
    
    def calculate_area(self) :
        return self.length * self.width
    
    def calculate_perimeter(self) :
        return 2 * (self.length + self.width)

class Triangle(Shape) :

    def __init__(self, side1, side2, side3) :
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def calculate_area(self) :
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
    
    def calculate_perimeter(self) :
        return self.side1 + self.side2 + self.side3
    
class ShapeCollection :

    def __init__(self) :
        self.shapes = []
    
    def add_shape(self, shape) :
        self.shapes.append(shape)
    
    def total_area(self) :
        return sum(shape.calculate_area() for shape in self.shapes)
    
    def total_perimeter(self) :
        return sum(shape.calculate_perimeter() for shape in self.shapes)
    
collection = ShapeCollection()

"""
3. Test the defined classes using input() Functions allowing user inputs
"""

print("\nThis a tool for calculating the perimeter and area for different Shapes. ")
print("Please follow the steps below :D ")

while True :

    print("________________________________________________________________________")
    print("\n1. Circle \n2. Rectangle \n3. Triangle \n4. Calculate Total \n5. Exit")
    choice = input("\nEnter your choice (1-5): ")

    if choice == '1' : 
        while True :
            try :
                radius = float(input("\nEnter the radius of the circle in meters: "))
                break
            except ValueError :
                print("Invalid input. Please enter a valid radius (has to be numeric). ")
        collection.add_shape(Circle(radius))
        print(f"Area of the circle: {round(Circle(radius).calculate_area(), 2)} m2. ")
        print(f"Perimeter of the circle: {round(Circle(radius).calculate_perimeter(), 2)} m. ")

    elif choice == '2' :
        while True :
            try :
                length = float(input("\nEnter the length of the rectangle in meters: "))
                break
            except ValueError :
                print("Invalid input. Please enter a valid length (has to be numeric). ")
        while True :
            try :
                width = float(input("Enter the width of the rectangle in meters: "))
                break
            except ValueError :
                print("Invalid input. Please enter a valid width (has to be numeric). ")
        collection.add_shape(Rectangle(length, width))
        print(f"Area of the rectangle: {round(Rectangle(length, width).calculate_area(), 2)} m2. ")
        print(f"Perimeter of the rectangle: {round(Rectangle(length, width).calculate_perimeter(), 2)} m. ")

    elif choice == '3' :
        while True :
            try :
                side1 = float(input("\nEnter the length of side 1 of the triangle in meters: "))
                break
            except ValueError :
                print("Invalid input. Please enter a valid length (has to be numeric). ")
        while True :
            try :
                side2 = float(input("Enter the length of side 2 of the triangle in meters: "))
                break
            except ValueError :
                print("Invalid input. Please enter a valid length (has to be numeric). ")
        while True :
            try :
                side3 = float(input("Enter the length of side 3 of the triangle in meters: "))
                break
            except ValueError :
                print("Invalid input. Please enter a valid length (has to be numeric). ")
        collection.add_shape(Triangle(side1, side2, side3))
        print(f"Area of the triangle: {round(Triangle(side1, side2, side3).calculate_area(), 2)} m2. ")
        print(f"Perimeter of the triangle: {round(Triangle(side1, side2, side3).calculate_perimeter(), 2)} m. ")

    elif choice == '4' :
        print(f"\nTotal Area of all the shapes: {round(collection.total_area(), 2)} m2. ")
        print(f"Total Perimeter of all the shapes: {round(collection.total_perimeter(), 2)} m. ")

    elif choice == '5' :
        break

    else:
        print("\nInvalid choice. Please enter a number between 1 and 5.")