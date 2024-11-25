#Assignment 29.10.2024 Arina Gogu

####Task1####

width = float(input("How wide is your room in meters?:"))
print(width,"meters wide")
length = float(input("How long is the room in meters?:"))
print(length,"meters long")
height = float(input("How high is the room in meters?:"))
print(height,"meters high")

####Task2####

area = width*length
print("Your room has an area of {} m^2" .format(area))

volume = width*length*height
print("Your room has a volume of {} m^3" .format(volume))

area_mm=width*length*1000*1000
volume_mm=width*length*height*1000*1000*1000
# how to use {}.format() to display in float format: 4e6 instead of 4000000 ?
print("That corresponds to an area of {} mm^2, and a volume of {} mm^3" .format(area_mm, volume_mm))

####Task3####

dominant=max(width,length,height)

if dominant==width:
    comparison="The width surpasses both the length and the height of your room"
elif dominant==length:
    comparison="The length surpasses both the width and the height of your room"
else:
    comparison="The height surpasses both the length and the width of your room"

print(comparison)


#### a small bonus ####
if height == width: 
    print('You have a beautiful room!')

if height == width == length: 
    print('You live in a cube! :D')

