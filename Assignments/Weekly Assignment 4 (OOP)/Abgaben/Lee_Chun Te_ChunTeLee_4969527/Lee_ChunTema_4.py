"""In this assignment, you will design a new pavilion inspired by an existing pavilion or project (it does not have to be an ITECH pavilion :D).

You will use object-oriented programming. The components of the pavilion (e.g. columns, beams, roofs, walls) will be modelled as classes and subclasses.
Each component will have parameters (such as dimensions, material type, fabrication methods) that can influence the overall cost and CO2 emissions of the pavilion.
In addition, cost estimates will be updated based on design decisions such as material selection or changes in dimensions.

1. Create the pavilion class. This is the main class that contains the components of the pavilion and provides methods for estimating the total cost, carbon footprint, etc. 
2. Component classes: Each major component (e.g. column, beam, wall) should have its own class that calculates its individual cost, carbon footprint, etc. 
3. Material subclasses: Materials will have different costs and properties that will affect those of the components. 
4. Be creative
5. Upload your assignment to ILIAS and GitHub"""


# Set up basic componenets

class Pavilion:
    def __init__(ITECH_CD, name):
        ITECH_CD.name = name
        ITECH_CD.components = []

    def add_component(ITECH_CD, component):
        ITECH_CD.components.append(component)

    def total_cost(ITECH_CD):
        return sum(component.calculate_cost() for component in ITECH_CD.components)

    def total_carbon_footprint(ITECH_CD):
        return sum(component.calculate_carbon_footprint() for component in ITECH_CD.components)

    def optimize_materials(ITECH_CD, objective="cost"):#Suggest material substitutions to minimize cost or carbon footprint.
        
        original_cost = ITECH_CD.total_cost()
        original_footprint = ITECH_CD.total_carbon_footprint()

        # Try all material combinations for optimization
        best_config = ITECH_CD.components
        best_cost = original_cost
        best_footprint = original_footprint

         

        for component in ITECH_CD.components:
            alternatives = component.material.get_alternatives()
            for alt_material in alternatives:
                # Swap material and recalculate
                original_material = component.material
                component.material = alt_material

                total_cost = ITECH_CD.total_cost()
                total_footprint = ITECH_CD.total_carbon_footprint()

                if objective == "cost" and total_cost < best_cost:
                    best_cost = total_cost
                    best_config = ITECH_CD.components.copy()

                if objective == "carbon" and total_footprint < best_footprint:
                    best_footprint = total_footprint
                    best_config = ITECH_CD.components.copy()

                # Revert to original material
                component.material = original_material

        ITECH_CD.components = best_config
        print(f"Optimization ({objective}): New cost = ${best_cost:.2f}, New CO2 = {best_footprint:.2f} kg")

    # def life_cycle_analysis(ITECH_CD):#Estimate the lifecycle cost and carbon footprint for the pavilion.( GPT Support lifecycle  )

    #     operational_years = 10
    #     maintenance_cost_factor = 0.025  # 2.5% of initial cost per year
    #     recycling_savings = 0.15  # 15% of initial material cost

    #     initial_cost = ITECH_CD.total_cost()
    #     initial_footprint = ITECH_CD.total_carbon_footprint()

    #     maintenance_cost = initial_cost * maintenance_cost_factor * operational_years
    #     end_of_life_savings = initial_cost * recycling_savings

    #     lifecycle_cost = initial_cost + maintenance_cost - end_of_life_savings
    #     lifecycle_footprint = initial_footprint  # Emissions from fabrication assumed static

    #     return {
    #         "lifecycle_cost": lifecycle_cost,
    #         "lifecycle_carbon_footprint": lifecycle_footprint
    #     }

    def summary(ITECH_CD):
        # lifecycle = ITECH_CD.life_cycle_analysis()
        # GPT Support lifecycle 
        print(f"Pavilion: {ITECH_CD.name}")
        print(f"Total Initial Cost: ${ITECH_CD.total_cost():,.2f}EUR")
        print(f"Total Initial Carbon Footprint: {ITECH_CD.total_carbon_footprint():,.2f} kg CO2")
        # print(f"Lifecycle Cost (10 years): ${lifecycle['lifecycle_cost']:,.2f}EUR")
        # print(f"Lifecycle Carbon Footprint: {lifecycle['lifecycle_carbon_footprint']:,.2f} kg CO2")
        for component in ITECH_CD.components:
            print(f"  - {component}")


class Material:# GPT support to define alternatives material
    def __init__(ITECH_CD, name, cost_per_unit_volume, carbon_footprint_per_unit_volume, alternatives=None):
        ITECH_CD.name = name
        ITECH_CD.cost_per_unit_volume = cost_per_unit_volume
        ITECH_CD.carbon_footprint_per_unit_volume = carbon_footprint_per_unit_volume
        ITECH_CD.alternatives = alternatives or [] 


    def get_alternatives(ITECH_CD):# Return alternative materials for optimization purposes.
        
        return ITECH_CD.alternatives


# Updated Material Definitions
class RecycledBottle(Material):
    def __init__(ITECH_CD):
        super().__init__("Recycled Bottle", cost_per_unit_volume=250, carbon_footprint_per_unit_volume=2)


class Timber(Material):
    def __init__(ITECH_CD):
        super().__init__("Timber", cost_per_unit_volume=5, carbon_footprint_per_unit_volume=5, alternatives=[RecycledBottle()])


class MetalPanel(Material):
    def __init__(ITECH_CD):
        super().__init__("Metal Panel", cost_per_unit_volume=10, carbon_footprint_per_unit_volume=8, alternatives=[Timber()])


# Updated Component Definitions
class Component:
    def __init__(ITECH_CD, name, dimensions, material):
        ITECH_CD.name = name
        ITECH_CD.dimensions = dimensions
        ITECH_CD.material = material

    def calculate_cost(ITECH_CD):
        volume = ITECH_CD.dimensions['length'] * ITECH_CD.dimensions['width'] * ITECH_CD.dimensions['height']
        return volume * ITECH_CD.material.cost_per_unit_volume

    def calculate_carbon_footprint(ITECH_CD):
        volume = ITECH_CD.dimensions['length'] * ITECH_CD.dimensions['width'] * ITECH_CD.dimensions['height']
        return volume * ITECH_CD.material.carbon_footprint_per_unit_volume

    def __str__(ITECH_CD):
        return f"{ITECH_CD.name} ({ITECH_CD.material.name})"


# Display Components
class Column(Component):
    def __init__(ITECH_CD, dimensions, material):
        super().__init__("Column", dimensions, material)


class Beam(Component):
    def __init__(ITECH_CD, dimensions, material):
        super().__init__("Beam", dimensions, material)


class Wall(Component):
    def __init__(ITECH_CD, dimensions, material):
        super().__init__("Wall", dimensions, material)


# Usage Display 
if __name__ == "__main__":
    pavilion = Pavilion(" Eco Pavilion 2024")

    # Define materials
    recycled_bottle = RecycledBottle()
    timber = Timber()
    metal_panel = MetalPanel()

    # Define components
    column1 = Column({'length': 5, 'width': 0.5, 'height': 7.5}, timber)
    wall1 = Wall({'length': 5, 'width': 0.3, 'height': 3}, recycled_bottle)
    beam1 = Beam({'length': 4, 'width': 0.5, 'height': 0.5}, metal_panel)

    # Add components to the pavilion
    pavilion.add_component(column1)
    pavilion.add_component(wall1)
    pavilion.add_component(beam1)

    # Display initial summary
    pavilion.summary()

    # Optimize materials for cost
    pavilion.optimize_materials("cost")
    pavilion.summary()

    # Optimize materials for carbon footprint
    pavilion.optimize_materials("carbon")
    pavilion.summary()
