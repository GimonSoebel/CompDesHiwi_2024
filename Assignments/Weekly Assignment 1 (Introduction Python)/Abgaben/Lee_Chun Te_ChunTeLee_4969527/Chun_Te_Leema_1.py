# Task 01
width= (input ('width of a room in meters'))
length= (input ('length of the room in meters'))
height= (input('height of the room in meters'))

# Task 02
area_m = width * length
volume_m= width * length * height

width_mm = width * 1000
length_mm = length * 1000
height_mm = height * 1000
area_mm = width_mm * length_mm
volume_mm = width_mm * length_mm * height_mm

print("Area of the room", area_m ,"m2")
print("Volume of the room",volume_m,"m3")

print("Area of the room" ,area_mm,"mm2")
print("Volume of the room" ,volume_mm, "mm3")

# # Task 03-GPT assisting
if width > length and width > height:
    dominant = "width"
elif length > width and length > height:
    dominant = "length"
elif height > width and height > length:
    dominant = "height"
else:
    dominant = " more dimensions are equal"

print("The dominant dimension of your room is the {dominant}.")