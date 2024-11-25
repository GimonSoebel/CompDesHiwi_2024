# Dictionary to hold building elements
building_elements = {}

# Function to add new building element
def add_element(key, element_type, room, length, height, thickness):
    """
    Adds a new building element to the building_elements dictionary.
    
    Parameters:
        key (str): Unique key for the element.
        element_type (str): Type of the element like wall, window, etc.
        room (str): Room name where the element is.
        length (float): Length in meters.
        height (float): Height in meters.
        thickness (float): Thickness in meters.
    """
    building_elements[key] = {
        "type": element_type,
        "room": room,
        "length": length,
        "height": height,
        "thickness": thickness
    }
    print(f"Added element '{key}' successfully.")

# Functions to calculate area and volume
def calculate_area(key):
    """
    Calculates area of a building element in square meters.
    
    Parameters:
        key (str): Unique key of the building element.
        
    Returns:
        float: Area of the element in m², or None if not found.
    """
    if key in building_elements:
        element = building_elements[key]
        return element["length"] * element["height"]
    else:
        print(f"Key '{key}' not found.")
        return None

def calculate_volume(key):
    """
    Calculates volume of a building element in cubic meters.
    
    Parameters:
        key (str): Unique key of the building element.
        
    Returns:
        float: Volume of the element in m³, or None if not found.
    """
    if key in building_elements:
        element = building_elements[key]
        return element["length"] * element["height"] * element["thickness"]
    else:
        print(f"Key '{key}' not found.")
        return None

# Function to get elements by their type
def get_elements_by_type(element_type):
    """
    Returns a list of keys for all building elements of a given type.
    
    Parameters:
        element_type (str): Type of element to search for.
        
    Returns:
        list: List of keys for elements of specified type.
    """
    element_keys = []
    for key, details in building_elements.items():
        if details["type"] == element_type:
            element_keys.append(key)
    return element_keys

# Sample data and usage
# Adding a few elements
add_element("Wall1", "wall", "Living Room", 5.0, 3.0, 0.3)
add_element("Win1", "window", "Kitchen", 1.5, 1.2, 0.1)
add_element("Door1", "door", "Bedroom", 0.9, 2.0, 0.05)

# Calculate area and volume for an element
print("Area of Wall1:", calculate_area("Wall1"))  # Example output: 15.0 m²
print("Volume of Wall1:", calculate_volume("Wall1"))  # Example output: 4.5 m³

# Get elements by type
print("List of all 'wall' elements:", get_elements_by_type("wall"))
print("List of all 'window' elements:", get_elements_by_type("window"))