print("Hello this is an volume calculator created by Simon Göbel (3739585). ")
print("Follow the steps below to get an volume and area of your room. ")

width = float(input("What is the width of the room in meters?: "))
length = float(input("What is the length of the room in meters?: "))
height = float(input("What is the height of the room in meters?: "))

volume_m = width * length * height
area_m = width * length
volume_mm = volume_m * 10**9
area_mm = area_m * 10**6

print("In meters the room has a volume of {0} m³ and an area of {1} m². ".format(volume_m,area_m))
print("In millimeters the room has a volume of {0} mm³ and an area of {1} mm². ".format(volume_mm,area_mm))

if height > length and height > width:
     print("The height of your room surpasses both its width and length. ")
if length > height and length > width:
    print("The length of your room surpasses both its height and width. ")
if width > length and width > height:
    print("The width of your room surpasses both its lenght and height. ")
if height == length > width:
    print("Both the height and length of your room are equal and surpass its width. ")
if height == width > length:
    print("Both the height and width of your room  are equal and surpass its length. ")
if length == width > height:
    print("Both the length and width of your room are equal and surpass its height. ")
if height == length == width:
    print("The length, length, and height of your room are equal. ")
