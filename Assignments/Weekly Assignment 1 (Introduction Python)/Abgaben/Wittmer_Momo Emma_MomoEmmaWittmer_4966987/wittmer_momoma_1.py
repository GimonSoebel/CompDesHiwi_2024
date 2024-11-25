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

user_input_width = input("Enter the width of a room in meters: ")
user_input_length = input("Enter the length of a room in meters: ")
user_input_hight = input("Enter the hight of a room in meters: ")
area_m2 = float(user_input_width) * float(user_input_length)
volume_m3 = area_m2 * float(user_input_hight)
dimensions = [float(user_input_width), float(user_input_length), float(user_input_hight)]   #make a list of all the values of the dimensions
max_index = dimensions.index(max(dimensions))                                               #get the index of the largest value in that list
dimension_names = ["width", "length", "hight"]                                              #make a list of all the names of the dimensions
print ("The area is {} m² or {} mm².".format(area_m2, area_m2 * 1000000))
print ("The volume is {} m³ or {} mm³.".format(volume_m3, volume_m3 * 1000000000))
print ("The largest dimension is", dimension_names[max_index])                              #get the name at the index of the largest value