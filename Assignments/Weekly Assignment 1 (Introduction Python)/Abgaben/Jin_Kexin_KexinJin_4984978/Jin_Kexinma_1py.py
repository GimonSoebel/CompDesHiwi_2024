def room_calculator():
    # Collect input for width, length, and height in meters
    width = float(input("Enter the width of the room in meters: "))
    length = float(input("Enter the length of the room in meters: "))
    height = float(input("Enter the height of the room in meters: "))
    
    # Calculate area and volume in meters
    area_m2 = width * length  # area in square meters
    volume_m3 = width * length * height  # volume in cubic meters
    
    # Convert to millimeters (1 meter = 1000 millimeters)
    width_mm = width * 1000
    length_mm = length * 1000
    height_mm = height * 1000
    area_mm2 = width_mm * length_mm  # area in square millimeters
    volume_mm3 = width_mm * length_mm * height_mm  # volume in cubic millimeters
    
    # Display area and volume
    print(f"\nArea in square meters: {area_m2:.2f} m²")
    print(f"Volume in cubic meters: {volume_m3:.2f} m³")
    print(f"Area in square millimeters: {area_mm2:.2f} mm²")
    print(f"Volume in cubic millimeters: {volume_mm3:.2f} mm³")
    
    # Determine and display the dominant dimension
    if width > length and width > height:
        dominant = "width"
    elif length > width and length > height:
        dominant = "length"
    elif height > width and height > length:
        dominant = "height"
    else:
        dominant = "There is no single dominant dimension; two or more dimensions are equal."
    
    print(f"\nThe dominant dimension of your room is: {dominant}")

# Run the room calculator function
room_calculator()