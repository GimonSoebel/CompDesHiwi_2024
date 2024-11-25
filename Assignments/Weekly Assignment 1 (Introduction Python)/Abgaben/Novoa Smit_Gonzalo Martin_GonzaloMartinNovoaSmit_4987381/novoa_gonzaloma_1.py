
""""
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


#Inputs and variables of Room Dimensions
width_str = input("Please type the width of the room in meters: ")
width = float (width_str)

lenght_str = input("Please type the lenght of the room in meters: ")
lenght = float (lenght_str)

height_str = input("Please type the height of the room in meters: ")
height = float (height_str)

volume = round ((width * lenght * height),2)
area = round ((width * lenght),2)

#List containing the dimensions, a pararell list with the string of each dimension, the index of the maximum value on the list
dim = [width, lenght, height]
dim_str = ["Width", "Lenght", "Height"]
dim_max_index = dim.index(max(dim))


#Printing Results
print ("")
print ("Volume in meters: " + str (volume) + " m3")
print ("Area in meters: " + str (area) + " m2")

print ("")
print ("Volume in milimiters: " + str (volume * 1000) + " mm3")
print ("Area in milimeters: " + str (area* 1000) + " mm2")

# Dominant Dimension
#TO ADD: If there is more than 1 dominant dimension (equal max values), return all of them.
print ("")
print ("Dominant Dimension: " + str (dim_str[dim_max_index]) + " (" + str (max(dim)) + "m)")
print ("")


