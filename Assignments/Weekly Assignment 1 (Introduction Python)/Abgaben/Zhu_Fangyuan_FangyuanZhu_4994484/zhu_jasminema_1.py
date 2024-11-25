# Assignment 1: Volume Calculator
"""
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
#1
l = input("Length of Room (m):")
go = True
while (go):
    try:
        l = float(l)
        go = False
    except ValueError:
        print("Sorry, that's not a valid float")
        l = input("Length of Room (m):")

w = input("Width of Room (m):")
go = True
while (go):
    try:
        w = float(w)
        go = False
    except ValueError:
        print("Sorry, that's not a valid float")
        w = input("Length of Room (m):")

h = input("Height of Room (m):")
go = True
while (go):
    try:
        h = float(h)
        go = False
    except ValueError:
        print("Sorry, that's not a valid float")
        h = input("Length of Room (m):")

#2
a_m = round(l*w, 3)
v_m = round(l*w*h, 3)
a_mm = round(a_m*1000000, 3)
v_mm = round(v_m*1000000000, 3)

print("Area: ", a_m, "m^2/", a_mm, "mm^2")
print("Volume: ", v_m, "m^3/", v_mm, "mm^3")

#3
if(l==w==h):
    print("All dimensions are equal") 

#two or more dimensions are equal
elif(l==w):
    #check if h is greater
    if(h>l):
        print("The height is the greatest dimension.")
    else:
        print("The length and width are the same and both are greater than the height.")
elif(l==h):
    #check if w is greater
    if(w>l):
        print("The width is the greatest dimension.")
    else:
        print("The length and height are the same and both are greater than the width.")
elif(w==h):
    #check if l is greater
    if(l>w):
        print("The length is the greatest dimension.")
    else: 
        print("The width and height are the same and both are greater than the length.")

#none of the elements are equal
else:
    if(l>w):
        if(l>h):
            print("The length is the greatest dimension.")
        else:
            print("The height is the greatest dimension.")
    else:
        if(w>h):
            print("The width is the greatest dimension.")
        else:
            print("The height is the greatest dimension.")