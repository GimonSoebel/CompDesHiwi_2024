room_width_str = input("Width (in meters): ")
room_length_str = input("Length (in meters): ")
room_height_str = input("Height (in meters): ")

room_width = float(room_width_str)
room_length = float(room_length_str)
room_height = float(room_height_str)

if room_width <= 0 or room_length <= 0 or room_height <= 0:
    print("All room dimensions must be greater than 0. Try again!")

else:
    area_m = (room_width * room_length)
    volume_m = (area_m * room_height)
    print("Area in m²: {} m²".format(area_m))
    print("Volume in m³: {} m³".format(volume_m))

    area_mm = (area_m * 10**6)
    volume_mm = (area_mm * 10**9)
    print("Area in mm²: {} mm²".format(area_mm))
    print("Volume in mm³: {} mm³".format(volume_mm))

    if room_width > room_length:
        if room_width > room_height:
            print ("The width of your room surpasses both its length and heigth.")
        elif room_width == room_height:
            print ("The width and height of your room are the same and surpass its length.")
        else:
            print ("The height of your room surpasses both its width and length.")
    elif room_length > room_width:
        if room_length > room_height:
            print ("The length of your room surpasses both its width and height.")
        elif room_length == room_height:
            print ("The length and height of your room are the same and surpass its width.")
        else:
            print ("The height of your room surpasses both its width and length.")
    elif room_width == room_length:
        if room_width > room_height:
            print ("The width and length of your room are the same and surpass its heigth.")
        elif room_width < room_height:
            print ("The height of your room surpasses both its width and length.")
        else:
            print ("The width, length and height of your room are the same.")