def main():

    room_info = {}  # a dictionary of room properties

    # input each property (*the function called "input_number" is defined below.)
    room_info["width"] = input_number("What is the width of a room(m): ")
    room_info["length"] = input_number("What is the length of the room(m): ")
    room_info["height"] = input_number("What is the height of the room(m): ")

    # sort data by values of a dict for determining the dominant dimension
    sorted_room_info = dict(
        sorted(room_info.items(), key=lambda item: item[1], reverse=True)
    )
    room_info_l = list(sorted_room_info.items())
    
    
    # calculate the area and volume of the room
    room_info["area"]= room_info["width"] * room_info["length"]
    room_info["vol" ]= room_info["area"] * room_info["height"]
    
    print(f"Area(m2): {room_info["area"]:,.2f}m2, Volume(m3): {room_info["vol"]:,.2f}m3")
    print(f"Area(mm2): {room_info["area"]*1e6:,.0f}mm2, Volume(mm3): {room_info["vol"]*1e9:,.0f}mm3")


    # Determine the dominant dimension and display the result
    if room_info_l[0][1] == room_info_l[1][1]:
        if room_info_l[0][1] == room_info_l[2][1]:
            print("The height, length and width of your room are the same.")
        else:
            print(
                f"The {room_info_l[0][0]} and {room_info_l[1][0]} of your room"\
                    f" are the same, and they surpass its {room_info_l[2][0]}."
            )
    else:
        print(
            f"The {room_info_l[0][0]} of your room surpasses both "\
                f"its {room_info_l[1][0]} and {room_info_l[2][0]}."
        )


def input_number(message:str):

    while True:
        try:
            value = float(input(message))
            break
        except ValueError:
            print("Please input a number")

    return value


if __name__ == "__main__":
    main()
