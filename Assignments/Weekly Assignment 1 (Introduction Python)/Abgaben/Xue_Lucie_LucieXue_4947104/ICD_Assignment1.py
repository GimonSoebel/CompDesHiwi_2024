#1
room_width = int(input("Please enter the width of a room in meters: "))
room_length = int(input("Please enter the length of a room in meters: "))
room_height = int(input("Please enter the height of a room in meters: "))

#2
room_volume_m = room_width * room_length * room_height
room_area_m = room_width * room_length

room_volume_mm = room_volume_m * 1000000
room_area_mm = room_area_m * 1000

print("The volume of the room is", room_volume_m,"cubic meters.")
print("The area of the room is", room_area_m, "square meters.")
print("The volume of the room is", room_volume_mm,"cubic milimeters.")
print("The area of the room is", room_area_mm, "square milimeters.")

#3
if room_width > room_length:
    if room_width > room_height:
        print("The width of your room surpasses both its length and height.")
    else:
        print("The height of your room surpasses both its length and width.")
elif room_length > room_height:
    print("The length of your room surpasses both its height and width.")
else:
    print("The height of your room surpasses both its length and width.")