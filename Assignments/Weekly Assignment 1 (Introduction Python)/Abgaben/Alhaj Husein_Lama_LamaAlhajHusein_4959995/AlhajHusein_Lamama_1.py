#Get user inputs for the room dimensions
width = float(input("Insert the room width in meters: "))
length = float(input("Insert the room length in meters: "))
height = float(input("Insert the room height in meters: "))

#Calculate Room's Area (m2) and Volume (m3)
area = width*length
volume = width*length*height

#Disply the Results
print (("Room area is equal to: ")+ format(area)+ " m2")
print (("Room Volume is equal to: ")+ format(volume)+ " m3\n")

#Calculate Room's Area (mm2) and Volume (mm3)
area_mm = area*(10**6)
volume_mm = volume*(10**9)

#Disply the Results
print (("Room area in mm2 is equal to: ")+ format(area_mm) + " mm2")
print (("Room Volume in mm3 is equal to: ")+ format(volume_mm) + " mm3\n")

#Determine the dominent dimension
if width > length and width > height:
    print ("The dominent dimension is the width") 
elif length > width and length > height:
    print ("The dominent dimension is the length")
elif height > width and height > length:
    print ("The dominent dimension is the height")
else:
    print ("All dimensions are equal")
