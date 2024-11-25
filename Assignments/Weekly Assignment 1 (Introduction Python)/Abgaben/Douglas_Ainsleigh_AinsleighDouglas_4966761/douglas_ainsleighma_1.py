# Determine the dimensions of the room
width_string = input("What is the width of the room in meters? ")
width = float(width_string)
length_string = input("What is the length of the room in meters? ")
length = float(length_string) 
height_string = input("What is the height of the room in meters? ")
height = float(height_string) 

# Calculate the volume and area in meters
volume = width * length * height
area = width * length
print ("the room has the volume of {} cubic meters ".format(volume)+"and area of {} square meters".format(area))
# Calculate the volume and area in millimeters
volume_mm = (volume * 1000000000)
area_mm = (area * 1000000)
print ("the room has the volume of {} cubic millimeters ".format(volume_mm)+"aand area of {} square millimeters".format(area_mm))

# Determining the dominant dimensions
# if all values are equal
if (width == length == height):
        print ("all measurements are equal")

# if some values are equal
if width == length:
    if width > height:
        print ("Width and length are equal and surpass the height")

if height == length:
    if height > width:
        print ("Height and length are equal and surpass the width")


if height == width:
    if height > length:
        print ("Height and width are equal and surpass the length")


# if no values are equal
if width > length:
    if width > height:
        print ("The width of your room surpasses both its height and length")
    else:
        print ("The height of your room surpasses both its width and length")
elif length > width:
    if length > height:
        print ("The length of your room surpasses both its height and width")
    else:
        print ("The height of your room surpasses both its width and length")



