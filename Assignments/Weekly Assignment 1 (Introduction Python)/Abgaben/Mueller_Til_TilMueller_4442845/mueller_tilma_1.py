a = input ("Please input the width of the room:   ")
b = input ("Also input the lenght of the room:   ")
c = input ("Lastly input the height of the room and enjoy: ")
a = float (a)
b = float (b)
c = float (c)
area = a * b
volume = a * b * c
print ("The area of the room is {} square meters, ".format (area)+"which also is {} square millimeters.".format (area*1000000))
print ("The volume of the room is {} cubic meters, ".format (volume)+"or {} cubic millimeters.".format (volume*1000000000))
if a>b and a>c:
    print ("The width is the dominat dimension of the room")
elif b>a and b>c:
    print ("The lenght is the dominat dimension of the room")
elif c>a and c>b:
    print ("The height is the dominat dimension of the room")
elif a==b and a==c:
    print ("All dimensions are equally dominat")
elif a==b and a!=c:
    print ("Width and Lenght are equally dominat")
elif a==c and b!=c:
     print ("Width and Height are equally dominat")
else:
    print ("Height and Lenght are equally dominat")