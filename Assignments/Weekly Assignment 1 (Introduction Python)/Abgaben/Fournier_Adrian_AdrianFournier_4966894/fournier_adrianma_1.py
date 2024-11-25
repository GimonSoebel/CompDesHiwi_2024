while True: #this is to catch exceptions in case the user enters non-numbers or negative values
    try:
        width = float(input("Please enter the width of the room in meters \n"))
        length = float(input("Please enter the height of the room in meters \n"))
        height = float(input("Please enter the height of the room in meters \n"))
        if width < 0 or length < 0 or height < 0:
            raise ValueError
        break
    except ValueError:
        print("Please enter only positive values")

unordered= [["width",width],["length", length],["height",height]]  #creating an array to associate variables with their names

#printing area and volume
area = width * length
volume = area * height
print("the area in square meters is: " + str(round(area,1)))
print("the volume in cubic meters is: " + str(round(volume,1)))
print("the area in square millimeters is: " + str(round(area * 10 ** 6)))
print("the volume in cubic millimeters is: " + str(round(volume * 10 ** 9)))

i = 1
max_value = unordered[0]
for i in range(len(unordered)):  # searching for the biggest number in the array and ensuring it's associated with the string for its name
    if(unordered[i][1]>unordered[i-1][1]):
        max_value = unordered[i]
print("The " + str(max_value[0]) + " which equals " + str(max_value[1]) + "m is the dominant dimension")


