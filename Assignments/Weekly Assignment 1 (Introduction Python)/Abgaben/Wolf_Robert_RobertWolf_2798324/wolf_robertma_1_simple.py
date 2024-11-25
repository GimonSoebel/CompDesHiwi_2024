
# get Input
width_in_m = float(input("The width of the room in m: "))
length_in_m = float(input("The length of the room in m: "))
height_in_m = float(input("The height of the room in m: "))

# calculate area
area_in_m = width_in_m * length_in_m  # in square meters (m²)
volume_in_m = width_in_m * length_in_m * height_in_m  # in cubic meters (m³)
# m2 to mm2 and m3 to mm3
volume_in_mm=volume_in_m*1000*1000*1000
area_in_mm=area_in_m*1000*1000


#decide dominant dimension
if height_in_m > width_in_m and height_in_m > length_in_m:
    print("The room is higher than it is wide and deep")
    dom_dim= "height"
if width_in_m > height_in_m and width_in_m > length_in_m:
    print("The room is wider than it is high and deep")
    dom_dim= "width"
if length_in_m > height_in_m and length_in_m > width_in_m:
    print("The room is deeper than it is wide and high")
    dom_dim= "lenght"
else:
    print("The room has no dominant dimension")
    dom_dim= "lenght"
    dom_dim = "not clear"


# Print Area and Statement about dominant dimension
print(f"The area of the room is {area_in_m:.2f} square meters (m²) or {area_in_mm:.2f} square millimeters (mm²).")
print(f"The volume of the room is {volume_in_m:.2f} cubic meters (m³) or {area_in_mm:.2f} cubic millimeters (mm³).")
print(f"Dominant dimension of the room: {dom_dim}.")
