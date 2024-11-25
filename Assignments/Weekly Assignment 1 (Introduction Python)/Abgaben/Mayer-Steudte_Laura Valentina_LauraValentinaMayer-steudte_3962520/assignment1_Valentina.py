# input ever values one at a time
# width_str = input("Please enter the width of your room in meters: ")
# length_str = input("Please enter the length of your room in meters: ")
# height_str = input("Please enter the height of your room in meters: ")

# input multiple values at once 
width_str, length_str, height_str = input("Please enter the width, length and height of your room in meters ").split()
print("width: ", width_str)
print("length: ", length_str)
print("height: ", height_str)


# convert string to float
width = float(width_str)
length = float(length_str)
height = float(height_str)

# calculate area/volume of room 
area = width * length
volume = area * height

# print the results
print("The area of your room is {} square meters".format(area))
print("The volume of your room is {} cubic meters".format(volume))

# calculate in cubic and square milimeter (*1000)
area_mil = area * 1000000
volume_mil = volume * 1000000000

# print the results
print("The area of your room is {} square millimeters and the volume is {} cubic millimeters".format(area_mil, volume_mil))

# determine the dominant dimension
if width > length:
    if width > height:
        print("The width of your room exceeds both the length and the height.")
    else:
        print ("The height of your room exceeds both the length and the width.")
elif length > width:  
    if length > height:
        print("The length of your room exceeds both the width and the height.")
    else:
        print ("The height of your room exceeds both the length and the width.")
else:
    print("The height, length and width of your room are all the same.")