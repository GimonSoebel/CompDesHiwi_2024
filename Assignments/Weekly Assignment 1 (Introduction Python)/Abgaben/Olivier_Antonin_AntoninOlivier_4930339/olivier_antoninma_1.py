""" First assignment """

# Asking the user for room dimensions
width = float(input("Please enter the width in meters "))
length = float(input("Please enter the length in meters "))
height = float(input("Please enter the height in meters "))

# Calculate and display the volume and the area of the room
volume_room = width* length * height
surface_room = width* length

# Dimensions rounded off to the nearest mm, as measuring equipment is generally accurate to the nearest mm
print("The volume of the room is " + str(round(volume_room,3)) + " m³" + ", or " + str(int(volume_room * 10**9)) + " mm³")
print("The surface of the room is " + str(round(surface_room,3)) + " m²" + ", or " + str(int(surface_room * 10**6)) + " mm²")

# Determine the largest dimension and print the corresponding message
maximum = max(width,length,height)
if maximum == width:
    print("The width of your room surpasses both its length and height" )
elif maximum == length:
    print("The length of your room surpasses both its width and height" )
else:
    print("The height of your room surpasses both its width and length" )


""" Discovering python """

# Determine the largest dimension and print the corresponding message
# Mapping dimensions to their names
# We have a dictionary where dimension names are keys, and their numeric values are the corresponding values
dimensions = {'width': width, 'length': length, 'height': height}

# Finding the maximum dimension, 
# Using max() with key=dimensions.get: max() goes through the dictionary keys ('width', 'length', 'height') and uses dimensions.get to compare the associated values.
max_dim_name = max(dimensions, key=dimensions.get)

# Getting the two other dimension names
# "name" is just a label, it could have been "key for key ..."
other_dims = [name for name in dimensions if name != max_dim_name]

# Outputting the result
print(f"The {max_dim_name} of your room surpasses both its {other_dims[0]} and {other_dims[1]}.")
