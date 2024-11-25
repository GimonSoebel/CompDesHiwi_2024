width=input("Please enter the width of the room in meters:")
length=input("Please enter the length of the room in meters:")
height=input("Please enter the height of the room in meters:")
volume=float(width)*float(length)*float(height)
print("The volume of the room is",volume,"m³")
area=float(width)*float(length)
print("The area of the room is",area,"m²")
volume=volume*10E9
print("The volume of the room is",volume,"mm³")
area=area*10E6
print("The area of the room is",area,"mm²")
if width>length and width>height :
    print("The width of your room surpasses both its length and height")
elif length>width and length>height :
    print("The length of your room surpasses both its width and height")
elif height>width and height>length :
    print("The height of your room surpasses both its width and length")
else :
    if width==length==height:
        print("All three dimensions of the room are equal")
    elif width==length:
        print("The width and length of the room are equal and surpass its height")
    elif width==height:
        print("The width and height of the room are equal and surpass its length")
    else :
        print("The length and height of the room are equal and surpass its width")