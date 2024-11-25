
#User Ipouts
print("Room Dimensions:")

width_room = float(input("Please enter the width of the room in meters. "))
length_room = float(input("Please enter the length of the room in meters. "))
height_room = float(input("Please enter the height of the room in meters. "))

#Area & volume calculation rounded upto 3 decimal places
area_room = round(width_room * length_room, 3)
volume_room = round(area_room * height_room, 3)

print(f'Room area = {area_room} sq.m. \nRoom volume = {volume_room} cu.m.')

#area and volume in milimeters based on user input
area_room_mm = area_room * 10**6
volume_room_mm = volume_room * 10**9

convert_unit = str(input("Convert units to millimeters? Press y or n "))

if convert_unit == ("y"):
    print(f'Room area = {area_room_mm} sq.mm. \nRoom volume = {volume_room_mm} cu.mm.')
else:
    print()

#remarks on the dimensions
if length_room > width_room and length_room > height_room:
    print("Length of the room surpasses both width and height.")

elif height_room > length_room and height_room > width_room:
    print("Height of the room surpasses both length and width.")

elif width_room > length_room and width_room > height_room:
    print("Width of the room surpasses both length and height.")

elif length_room == width_room == height_room:
    print("Room is a cube.")

elif length_room == width_room:
    print("Room is a square in terms of floor dimensions.")

else:
    print("No dimension is significantly larger than the others.")

