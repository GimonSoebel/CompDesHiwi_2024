
"""
Task Description:

Your task is to create a Python code that calculates the area and the volume of a room based on user input for the width, length and height of the room. 
This exercise reinforces the concept of collecting user input, performing calculations, and displaying results.

Requirements:
    Write a Python code that does the following:
    1.
        Asks the user to enter the width of a room in meters.
        Asks the user to enter the length of the room in meters.
        Asks the user to enter the height of the room in meters.
        
    2.
        Calculates and displays the volume and the area of the room in cubic meters and square meters.
        Calculates and displays the volume and the area of the room in cubic milimeters and square milimiters.  
    
    3.
        Determine the dominant dimension and display the result. 
        For instance, you might receive feedback like, 'The height of your room surpasses both its width and length'.
        
"""
from decimal import *

name = input("What is your name?")
print("Hello, " + name + "! We calculate the area and the volume of a room based on your input.")

w_str = input("What is the width in meter?")
width = Decimal(w_str)
l_str = input("What is the length in meter?")
length = Decimal(l_str)
h_str = input("What is the height in meter?")
height = Decimal(h_str)

area = width*length
volume = area*height


if width > length:
    if width > height:
       print ("width is the largest.")
    elif width < height:
       print("height is the largest.")
    else:  ##height==width
       print("width and height are the largest.")
elif length > width:
   if length > height:
      print("length is the largest.")
   elif length < height:
      print("height is the largest.")
   else:   ##length==height
      print("length and height are the largest.")
elif width == length:
   if height > width and height > length:
      print("height is the largest.")
   elif height < width and height < length:
      print("length and width are the largest.")
   else:  ##width==height==length
      print("all three are equal.")



print("The area is",area,"m^2 (",area*1000*1000,"mm^2 ) and the volume is",volume,"m^3 (",volume*1000*1000*1000,"mm^3 ), thank you!")

