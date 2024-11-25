# Step 1: Collect user inputs for room dimensions
print("Hello user! We will calculate the volume & area of a room now!")
w = float(input("Enter the width of the room in meters: "))
l = float(input("Enter the length of the room in meters: "))
h = float(input("Enter the height of the room in meters: "))

# Step 2: Calculating the area and volume
# Volume in cubic meters
volume_m = w * l * h
# Area in square meters (floor area)
area_m = w * l

# Step 3: Converting to cubic millimeters and square millimeters
volume_mm = volume_m * 1000000000  
area_mm = area_m * 1000000  

# Displaying results in cubic and square meters and millimeters
print(f"Volume of the room: {volume_m} cubic meters ({volume_mm} cubic millimeters)")
print(f"Area of the room: {area_m} square meters ({area_mm} square millimeters)")

# Step 4: Determining and displaying the dominant dimension
if w >= l and w >= h:
    dominant_dimension = "width"
elif l >= w and l >= h:
    dominant_dimension = "length"
else:
    dominant_dimension = "height"

print(f"The dominant dimension of the room is the {dominant_dimension}.")