#Mini assignment 01
#Room dimentions
height = float(input("Please enter the height of the room in meters:"))
width = float(input("Please enter the width of the room in meters:"))
length = float(input("Please enter the lenght of the room in meters:"))

#m² + m³
area = width * length 
volume = height * width * length

#mm² + mm³

area_mm2 = area * 1_000_000
volume_mm3 = volume * 1_000_000_000

#results of the dimention

print("Here is the area of the room: {}m²".format(area)) 
print("Here is the volume of the room: {}m³".format(volume))
print("The area of the room: {}mm²".format(area_mm2))
print("The volume of the room: {}mm³".format(volume_mm3))

#dominant dimention

if height > width and height > length:
    dominant_dimension = "height"
elif width > height and width > length:
    dominant_dimension = "width"
else:
    dominant_dimension = "length"

if dominant_dimension == "height":
    print("The largest dominant_dimension in the room height")
elif dominant_dimension == "width":
    print("The largest dominant_dimension in the room width")
elif dominant_dimension == "length":
    print("The largest dominant_dimension in the room length")
else:
    print("Some lengths of the room are equal to each other")
