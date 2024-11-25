
# Revised with LLM for readability and Documentation

import math

class Pavilion:
    """
    Base class for pavilion elements.
    """

    def __init__(self, material):
        """
        Initialize a Pavilion object.

        Args:
            material (Material): The material used for the pavilion element.
        """
        self.material = material

    def calc_cost_carbon_footprint(self, material, volume, surf_area, a_v_ratio):
        """
        Calculate cost and carbon footprint for the pavilion element.

        Args:
            material (Material): The material used.
            volume (float): Volume of the element.
            surf_area (float): Surface area of the element.
            a_v_ratio (float): Area to volume ratio.

        Returns:
            tuple: Cost volume, cost surface, carbon footprint, and necessary heating.
        """
        cost_surf = surf_area * material.cost_index_surf
        cost_vol = volume * material.cost_index_vol
        carbon_footprint_prim = material.avg_density * volume * material.fab_factor * material.emission_factor
        nec_heating = 50 * volume * (a_v_ratio + 10) / 10
        return cost_vol, cost_surf, carbon_footprint_prim, nec_heating

class Material:
    """
    Represents a building material with its properties.
    """

    def __init__(self, material_name, fab_method, surf_method, cost_surface_per_m2):
        """
        Initialize a Material object.

        Args:
            material_name (str): Name of the material.
            fab_method (str): Fabrication method.
            surf_method (str): Surface treatment method.
            cost_surface_per_m2 (float): Cost per square meter of surface.
        """
        self.material_name = material_name
        self.fab_method = fab_method
        self.surf_method = surf_method
        self.cost_surface_per_m2 = cost_surface_per_m2
        self._set_material_properties()

    def _set_material_properties(self):
        """Set material properties based on the material name."""
        if self.material_name == "Steel":
            self._set_steel_properties()
        elif self.material_name == "Wood":
            self._set_wood_properties()
        elif self.material_name == "Concrete":
            self._set_concrete_properties()
        else:
            raise ValueError(f"Unsupported material: {self.material_name}")
        self._set_surface_properties()

    def _set_steel_properties(self):
        """Set properties specific to steel."""
        self.cost_raw_per_m3 = 6300 / 7.9
        self.avg_density = 7900
        self.emission_factor = 0.35
        valid_methods = {"Welded": 1, "Riveted": 1.4}
        self._set_fab_factor(valid_methods)

    def _set_wood_properties(self):
        """Set properties specific to wood."""
        self.cost_raw_per_m3 = 580 / 2.35
        self.avg_density = 630
        self.emission_factor = 0.31
        valid_methods = {"Modular Construction": 0.7, "Solid": 1.4, "CLT": 1.0}
        self._set_fab_factor(valid_methods)

    def _set_concrete_properties(self):
        """Set properties specific to concrete."""
        self.cost_raw_per_m3 = 80
        self.avg_density = 2600
        self.emission_factor = 0.59
        valid_methods = {"Pouring": 0.8, "Concrete Bricks": 1.0, "Prefabricated": 1.2}
        self._set_fab_factor(valid_methods)

    def _set_fab_factor(self, valid_methods):
        """
        Set fabrication factor based on the fabrication method.

        Args:
            valid_methods (dict): Dictionary of valid fabrication methods and their factors.
        """
        if self.fab_method in valid_methods:
            self.fab_factor = valid_methods[self.fab_method]
        else:
            raise ValueError(f"Invalid fabrication method '{self.fab_method}' for {self.material_name}")
        self.cost_index_vol = self.fab_factor * self.cost_raw_per_m3

    def _set_surface_properties(self):
        """Set surface properties based on the surface method."""
        surf_factors = {"Sanded": 0.7, "Painted": 1, "Plastered": 1.3}
        if self.surf_method in surf_factors:
            surf_factor = surf_factors[self.surf_method]
        else:
            raise ValueError(f"Invalid surface method: {self.surf_method}")
        self.cost_index_surf = surf_factor * self.cost_surface_per_m2

class Columns(Pavilion):
    """
    Represents columns in the pavilion.
    """

    def calc_column_surf_area_volume(self, dim_x, dim_y, dim_z, shape):
        """
        Calculate surface area and volume of a column.

        Args:
            dim_x (float): X dimension.
            dim_y (float): Y dimension.
            dim_z (float): Z dimension (height).
            shape (str): Shape of the column ("Cuboid", "Cylinder", or "Elliptical").

        Returns:
            tuple: Surface area, volume, and area-to-volume ratio.
        """
        if shape == "Cuboid":
            surf_area = 2 * ((dim_x * dim_y) + (dim_z * dim_y) + (dim_x * dim_z))
            volume = dim_x * dim_y * dim_z
        elif shape == "Cylinder":
            radius = dim_x / 2
            surf_area = 2 * math.pi * radius * (dim_z + radius)
            volume = math.pi * (radius ** 2) * dim_z
        elif shape == "Elliptical":
            half_axis_x, half_axis_y = dim_x / 2, dim_y / 2
            surf_area = 2 * math.pi * half_axis_x * dim_z + 2 * math.pi * half_axis_x * half_axis_y
            volume = math.pi * half_axis_x * half_axis_y * dim_z
        else:
            raise ValueError(f"Unsupported shape: {shape}")
        a_v_ratio = surf_area / volume
        return surf_area, volume, a_v_ratio

    def __init__(self, material, dim_x, dim_y, dim_z, shape):
        """
        Initialize a Columns object.

        Args:
            material (Material): Material of the column.
            dim_x (float): X dimension.
            dim_y (float): Y dimension.
            dim_z (float): Z dimension (height).
            shape (str): Shape of the column.
        """
        super().__init__(material)
        self.width = dim_x
        self.depth = dim_y
        self.shape = shape
        self.surf_area, self.volume, self.a_v_ratio = self.calc_column_surf_area_volume(dim_x, dim_y, dim_z, shape)
        self.cost_vol, self.cost_surf, self.carbon_prim, self.nec_heating = self.calc_cost_carbon_footprint(
            material, self.volume, self.surf_area, self.a_v_ratio)

class Beams(Pavilion):
    """
    Represents beams in the pavilion.
    """

    def calc_beam_surf_area_volume(self, long_axis, short_axis, height, shape):
        """
        Calculate surface area and volume of a beam.

        Args:
            long_axis (float): Length of the beam.
            short_axis (float): Width of the beam.
            height (float): Height of the beam.
            shape (str): Shape of the beam ("Cuboid", "Cylinder", or "Elliptical").

        Returns:
            tuple: Surface area, volume, and area-to-volume ratio.
        """
        if shape == "Cuboid":
            surf_area = 2 * ((long_axis * short_axis) + (height * short_axis) + (long_axis * height))
            volume = long_axis * short_axis * height
        elif shape == "Cylinder":
            radius = short_axis / 2
            surf_area = 2 * math.pi * radius * long_axis + 2 * math.pi * radius**2
            volume = math.pi * radius**2 * long_axis
        elif shape == "Elliptical":
            half_axis_min, half_axis_maj = short_axis / 2, height / 2
            avg_radius = math.sqrt((half_axis_min**2 + half_axis_maj**2) / 2)
            curved_surface_area = 2 * math.pi * avg_radius * long_axis
            base_area = math.pi * half_axis_min * half_axis_maj
            surf_area = curved_surface_area + 2 * base_area
            volume = math.pi * half_axis_min * half_axis_maj * long_axis
        else:
            raise ValueError(f"Unsupported shape: {shape}")
        a_v_ratio = surf_area / volume
        return surf_area, volume, a_v_ratio

    def __init__(self, material, long_axis, short_axis, height, shape):
        """
        Initialize a Beams object.

        Args:
            material (Material): Material of the beam.
            long_axis (float): Length of the beam.
            short_axis (float): Width of the beam.
            height (float): Height of the beam.
            shape (str): Shape of the beam.
        """
        super().__init__(material)
        self.length = long_axis
        self.depth = short_axis
        self.surf_area, self.volume, self.a_v_ratio = self.calc_beam_surf_area_volume(long_axis, short_axis, height, shape)
        self.cost_vol, self.cost_surf, self.carbon_prim, self.nec_heating = self.calc_cost_carbon_footprint(
            material, self.volume, self.surf_area, self.a_v_ratio)

class Roofs(Pavilion):
    """
    Represents roofs in the pavilion.
    """

    def calc_roof_surf_area_volume(self, dim_x, dim_y, dim_z, radius, thickness, shape):
        """
        Calculate surface area and volume of a roof.

        Args:
            dim_x (float): X dimension.
            dim_y (float): Y dimension.
            dim_z (float): Z dimension.
            radius (float): Radius for spherical segment.
            thickness (float): Thickness of the roof.
            shape (str): Shape of the roof ("Cuboid" or "Spherical Segment").

        Returns:
            tuple: Surface area, volume, and area-to-volume ratio.
        """
        if shape == "Cuboid":
            surf_area = 2 * ((dim_x * dim_y) + (dim_z * dim_y) + (dim_x * dim_z))
            volume = dim_x * dim_y * dim_z
        elif shape == "Spherical Segment":
            surf_area_outside = math.pi * (2 * radius * dim_z + (dim_x/2)**2)
            surf_area_inside = math.pi * (2 * (radius-thickness) * (dim_z-thickness) + ((dim_x/2)-thickness)**2)
            surf_area = surf_area_outside + surf_area_inside - ((dim_x - thickness)**2 * math.pi)
            volume_outside = (dim_z**2 * math.pi / 3) * (3 * radius - dim_z)
            volume_inside = ((dim_z-thickness)**2 * math.pi / 3) * (3 * (radius-thickness) - (dim_z-thickness))
            volume = volume_outside - volume_inside
        else:
            raise ValueError(f"Unsupported shape: {shape}")
        a_v_ratio = surf_area / volume
        return surf_area, volume, a_v_ratio

    def __init__(self, material, dim_x, dim_y, dim_z, radius, thickness, shape):
        """
        Initialize a Roofs object.

        Args:
            material (Material): Material of the roof.
            dim_x (float): X dimension.
            dim_y (float): Y dimension.
            dim_z (float): Z dimension.
            radius (float): Radius for spherical segment.
            thickness (float): Thickness of the roof.
            shape (str): Shape of the roof.
        """
        super().__init__(material)
        self.width = dim_x
        self.depth = dim_y
        self.shape = shape
        self.surf_area, self.volume, self.a_v_ratio = self.calc_roof_surf_area_volume(dim_x, dim_y, dim_z, radius, thickness, shape)
        self.cost_vol, self.cost_surf, self.carbon_prim, self.nec_heating = self.calc_cost_carbon_footprint(
            material, self.volume, self.surf_area, self.a_v_ratio)

def get_mat(name):
    """
    Get material properties from user input.

    Args:
        name (str): Name of the element (e.g., "Column", "Roof").

    Returns:
        Material: A Material object with the specified properties.
    """
    possible_mats = {"Steel", "Wood", "Concrete"}
    possible_fab_methods = {
        "Steel": {"Welded", "Riveted"},
        "Wood": {"CLT", "Solid", "Modular Construction"},
        "Concrete": {"Pouring", "Concrete Bricks", "Prefabricated"}
    }
    possible_surf_methods = {"Sanded", "Painted", "Plastered"}

    while True:
        mat = input_with_validation(f"What is the Material of {name}", possible_mats)
        fab_method = input_with_validation(f"What is the Fabrication Method of {name}", possible_fab_methods[mat])
        surf_method = input_with_validation(f"What is the Surface process of {name}", possible_surf_methods)
        try:
            surf_cost = float(input("Enter Surface Cost per m² in €: "))
            return Material(mat, fab_method, surf_method, surf_cost)
        except ValueError:
            print("Invalid input for surface cost. Please enter a number.")

def input_with_validation(prompt, valid_options):
    """
    Get user input with validation against a set of valid options.

    Args:
        prompt (str): The prompt to display to the user.
        valid_options (set): Set of valid input options.

    Returns:
        str: The validated user input.
    """
    while True:
        user_input = input(f"{prompt}\nThe possibilities are {valid_options}\nEnter your choice: ")
        if user_input in valid_options:
            return user_input
        print(f"Invalid input. Please choose from {valid_options}")


def complete_pavillion_results(elements):
    """
    Add all results together for the complete Pavillion
    """
    overall_surface_area=0
    overall_volume=0
    overall_a_v_ratio_add=0
    overall_cost_vol=0
    overall_cost_surf=0
    overall_carbon_prim=0
    overall_nec_heating=0

    for element in elements:
        overall_surface_area=overall_surface_area+element.surf_area
        overall_volume=overall_volume+element.volume
        overall_a_v_ratio_add=overall_a_v_ratio_add+element.a_v_ratio
        overall_cost_vol = overall_cost_vol+ element.cost_vol
        overall_cost_surf = overall_cost_surf + element.cost_surf
        overall_carbon_prim=overall_carbon_prim+element.carbon_prim
        overall_nec_heating=overall_nec_heating+element.nec_heating
    
    
    overall_cost= overall_cost_surf+ overall_cost_vol
    overall_a_v_ratio = overall_a_v_ratio_add/len(elements)
    print(f"\n\nOverall Pavillion:")
    print(f"Surface Area: {overall_surface_area:.2f} m²")
    print(f"Volume: {overall_volume:.2f} m³")
    print(f"A/V-Ratio: {overall_a_v_ratio:.2f}")
    print(f"Cost overall: {overall_cost:.2f} €")
    print(f"Primary Carbon Footprint: {overall_carbon_prim:.2f} kg")
    print(f"Heating Energy Required: {overall_nec_heating:.2f} W")
    print("\n")
    


def main():
    """
    Main function to run the pavilion calculation program.
    """
    material_col = get_mat("Column")
    material_roof = get_mat("Roof")

    elements = [
        Columns(material_col, 0.2, 0.2, 4, "Cylinder"),
        Columns(material_col, 0.2, 0.2, 4, "Cylinder"),
        Columns(material_col, 0.2, 0.3, 4, "Elliptical"),
        Columns(material_col, 0.2, 0.3, 4, "Elliptical"),
        Roofs(material_roof, 2, 2, 1, 1, 0.2, "Spherical Segment")
    ]

    for i, element in enumerate(elements, 1):
        if isinstance(element, Columns):
            element_type = "Column" 
        if isinstance(element, Roofs):
            element_type = "Roof" 
        if isinstance(element, Beams):
            element_type = "Beam" 
        
        print(f"\n\nElement Type:{element_type} Element ID:{i}:")
        print(f"Surface Area: {element.surf_area:.2f} m²")
        print(f"Volume: {element.volume:.2f} m³")
        print(f"A/V-Ratio: {element.a_v_ratio:.2f}")
        print(f"Cost overall: {element.cost_vol + element.cost_surf:.2f} €")
        print(f"Primary Carbon Footprint: {element.carbon_prim:.2f} kg")
        print(f"Heating Energy Required: {element.nec_heating:.2f} W")
        print("\n")
    
    complete_pavillion_results(elements)


if __name__ == "__main__":
    main()