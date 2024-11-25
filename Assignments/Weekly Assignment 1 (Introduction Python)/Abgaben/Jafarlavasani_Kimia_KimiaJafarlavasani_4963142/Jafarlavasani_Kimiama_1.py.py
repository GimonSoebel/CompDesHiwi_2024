# Function to calculate area and volume of a room
def calculate_room_dimensions():
    # Get user input
    width = float(input("Enter the width of the room in meters: "))
    length = float(input("Enter the length of the room in meters: "))
    height = float(input("Enter the height of the room in meters: "))
    
    # Calculate area and volume in meters
    area_m2 = width * length
    volume_m3 = width * length * height
    
    # Calculate area and volume in millimeters
    area_mm2 = area_m2 * 1_000_000  # 1 m^2 = 1,000,000 mm^2
    volume_mm3 = volume_m3 * 1_000_000_000  # 1 m^3 = 1,000,000,000 mm^3

    # Display results
    print("Area of the room = {} square meters". format (area_m2))
    print("Area of the room = {} square millimeters". format (area_mm2))
    print("volume of the room = {} cubice meters". format (volume_m3))
    print("volume of the room = {} cubice millimeters". format (volume_mm3))
   
    # Determine the dominant dimension
    dominant_dimension = max(width, length, height)
    if dominant_dimension == height:
        print("The height of your room surpasses both its width and length.")
    elif dominant_dimension == width:
        print("The width of your room surpasses both its length and height.")
    else:
        print("The length of your room surpasses both its width and height.")

# Run the function
calculate_room_dimensions()