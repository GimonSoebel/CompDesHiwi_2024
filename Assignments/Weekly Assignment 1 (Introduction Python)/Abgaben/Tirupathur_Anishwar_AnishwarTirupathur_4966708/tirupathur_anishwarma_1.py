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
# Create and assign variables for width, length, and height using user input

def input_measurement(dimension_str):
    # Use while loop to make sure user input is a number
    test_bool = False

    while (test_bool == False):
        try:
            dimension = float(input('What is the {} of your room in meters?: '.format(dimension_str)))
            test_bool = True
            return dimension
        
        except ValueError:
             print('Invalid, please input a number')

width_meters = input_measurement('width')
length_meters = input_measurement('length')
height_meters = input_measurement('height')

#Convert dimensions to millimeters and store them into new variables
width_millimeters = width_meters*1000
length_millimeters = length_meters*1000
height_millimeters = height_meters*1000

#Calculate volume and area with each units
area_meters = width_meters*length_meters
area_millimeters = width_millimeters*length_millimeters

volume_meters = area_meters*height_meters
volume_millimeters = area_millimeters*height_millimeters

print("The area of the room is {} square meters, and the volume of the room is {} cubic meters".format(area_meters, volume_meters))
print("The area of the room is {} square millimeters, and the volume of the room is {} cubic millimeters".format(area_millimeters, volume_millimeters))

# Check for a dominant dimension
dominant_bool = False

while (dominant_bool == False):
    if (width_meters == length_meters):
        if (width_meters == height_meters):
            print ('Your room is a cube!')
            dominant_bool = True
        elif (width_meters < height_meters):
            print("The height of your room surpasses both its width and length") 
            dominant_bool = True
        else:
            print ('Your floor is a square!')
            dominant_bool = True
    elif (width_meters == height_meters and width_meters > length_meters):
        print ('The width and height are equal')
        dominant_bool = True
    elif (length_meters == height_meters and length_meters > width_meters):
        print ('The length and height are equal')
        dominant_bool = True
    elif (width_meters > length_meters and width_meters > height_meters): 
        print("The width of your room surpasses both its height and length")
        dominant_bool = True
    elif (length_meters > width_meters and length_meters > height_meters): 
        print("The length of your room surpasses both its height and width")
        dominant_bool = True
    elif (height_meters > length_meters and height_meters > width_meters):
        print("The height of your room surpasses both its width and length") 
        dominant_bool = True
