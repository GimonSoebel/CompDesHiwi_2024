
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

#first step
user_width = input('Enter the width of a room in meters:')
user_length = input('Enter the length of the room in meters:')
user_height = input('Enter the height of the room in meters:')

width = int(user_width)
length = int(user_length)
height = int(user_height)

#second step
area_m = width * length
volume_m = area_m * height
area_mm = area_m * (10 ** 6)
volume_mm = volume_m * (10 ** 9)

print('\n')
print('The area of the room in meters: {} square meters'.format(area_m))
print('The volume of the room in meters: {} cubic meters'.format(volume_m))
print('\n')
print('The area of the room in milimeters: {} square milimeters'.format(area_mm))
print('The volume of the room in milimeters:{} cubic milimeters'.format(volume_mm))
print('\n')

#third step
if width > length and width > height:
    print ('The width of your room surpasses both its lenght and height.')
elif length > width and length > height:
    print ('The length of your room surpasses both its width and height.')
elif height > width and height > length:
    print ('The height of your room surpasses both its width and length.')
else:
    print ('All dimensions of your room equal to each other.')