#1 ask: Ask for Input from the user (Dimensions)
width = float(input("Enter width of the room in meters: "))
length = float(input("Enter length of the room in meters: "))
height = float(input("Enter height of the room in meters: "))

#2.1 calculating: Calculate area and volume
volume_m3 = width * length * height  # in cubic meters
area_m2 = width * length  # in square meters

#2.2 converting: Volume and Area in cubic and square millimeters
volume_mm3 = volume_m3 * 1_000_000_000
area_mm2 = area_m2 * 1_000_000

#print results
print("\nRoom Dimensions Calculations:")
print(f"Volume in cubic meters: {volume_m3} m³")
print(f"Area in square meters: {area_m2} m²")
print(f"Volume in cubic millimeters: {volume_mm3} mm³")
print(f"Area in square millimeters: {area_mm2} mm²")

#3 conditions: statements about dominant dimensions
if width > length and width > height:
    dominant_dimension = "width"
    room_description = "The depth of the room makes it very special."  # additional feedback about depth
elif length > width and length > height:
    dominant_dimension = "length"
    room_description = "This looks like a studio." # additional feedback about length
else:
    dominant_dimension = "height"
    room_description = "High ceilings are considered to be beautiful."  # additional feedback about height

# express results: prin of dominant dimension and additional feedback
print(f"\nThe {dominant_dimension} of your room surpasses both its other dimensions.")
if room_description:
    print(room_description)
