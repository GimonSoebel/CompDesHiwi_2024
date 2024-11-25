"""
reference: https://www.blumer-lehmann.com/en/references/referencetimber-free-form-timber-pavilion-into-the-woods.html

Summary of classes
    Pavilion class
            
    Component class
        subclass: Column, Beam, Roof, Basement
        
    Material class
        subclass: Wood, Concrete, Membrane
        
    Fabrication class
        subclass: Cutting(Wood, Membrane), Welding(Membrane), Casting(Concrete)
"""


def main(params):

    # parameters
    pavilion_name, comp_dicts = params

    # create a pavilion instance with a pavilion name
    pav = Pavilion(pavilion_name)

    get_dict_items = lambda dict_, keys: {k: dict_[k] for k in keys}

    for label, props in comp_dicts.items():
        for props_ in props:
            # create a component class instance
            comp_model = globals()[label](
                **get_dict_items(props_, ["length", "height", "width"])
            )

            # calculate component area and volume
            comp_model.calc_area()
            comp_model.calc_vol()

            # create a material class instance
            material = globals()[props_["material"].capitalize()](vol=comp_model.vol)
            material.calc_weight()

            fab_method = []
            for fab_name in props_["fab_method"]:

                # define the process name for the fabrication class input
                pre_proc_name = [v.lower() for v in [fab_name, props_["material"]]]
                proc_name = " ".join(pre_proc_name)

                # create and add a fabrication class instance to the fab_method list
                fab_method.append(
                    globals()[fab_name.capitalize()](proc_name, comp_model, material.w)
                )

            # assign the material class instance and the fabrication class instance(s) to the component class instance
            comp_model.mat, comp_model.fab_method = material, fab_method
            pav.add_components(comp_model)

    # calculate the sum of CO2 emission and cost
    pav.calc_cost()
    pav.calc_co2()

    # Show the result of CO2 emission and cost
    print(f"----- Element info -----\n{"-"*120}")
    for comp in pav.comps:
        comp.display_properties()

    print(f"----- Pavilion Cost and The Overall CO2 Emission Info -----")
    pav.display_cost_co2()



class Pavilion:

    def __init__(self, name):

        self.name = name # Pavilion name
        self.comps = []  # List of components in the pavilion

    def add_components(self, component):
        self.comps.append(component)

    def calc_cost(self):
        self.cost = sum([comp.calc_cost() for comp in self.comps])

    def calc_co2(self):
        self.co2 = sum([comp.calc_co2() for comp in self.comps])

    def display_cost_co2(self):

        print(
            f"{"-"*120}\nName: {self.name}\n The overall cost: €{self.cost:,.2f}"
            f"\n The overall CO2 emission: {self.co2:,.2f}kg CO2\n{"-"*120}"
        )


class Component:
    def __init__(self, name, length, width, height, material, fab_method):
        self.name = name              # Component name
        self.length = length          # Length (m)
        self.width = width            # Width  (m)
        self.height = height          # Height  (m)
        self.mat = material           # Instance of material class 
        self.fab_method = fab_method  # List of fabrication instances

    def calc_area(self):
        self.area = self.length * self.width

    def calc_vol(self):
        self.vol = self.length * self.width * self.height

    def calc_cost(self):
        total_fab_cost = sum([method.calc_cost() for method in self.fab_method])
        self.cost = self.mat.calc_cost() + total_fab_cost
        return self.cost

    def calc_co2(self):
        total_fab_co2 = sum([method.calc_co2() for method in self.fab_method])
        self.total_co2 = self.mat.calc_carbon() + total_fab_co2
        return self.total_co2

    def display_properties(self):

        fab_method_name = ", ".join([method.proc_name for method in self.fab_method])

        print(
            f"Element name: {self.name}\n"
            f" Length: {self.length:,.2f}, Width: {self.width:,.2f}, Height: {self.height:,.2f}\n"
            f" Material:{self.mat.name}, Fabrication method:{fab_method_name}\n"
            f" The cost: €{self.cost:,.2f}, The CO2 emission: {self.total_co2:,.2f}kg CO2\n{"-"*120}"
        )


class Column(Component):

    def __init__(
        self,
        name="column",
        length=1.0,
        width=1.0,
        height=1.0,
        mat_type=None,
        fab_method=[],
    ):
        super().__init__(name, length, width, height, mat_type, fab_method)

    def calc_area(self):
        self.area = self.length * self.height


class Beam(Component):

    def __init__(
        self,
        name="beam",
        length=1.0,
        width=1.0,
        height=1.0,
        mat_type=None,
        fab_method=[],
    ):
        super().__init__(name, length, width, height, mat_type, fab_method)

    def calc_area(self):
        self.area = self.length * self.height


class Roof(Component):

    def __init__(
        self,
        name="roof",
        length=1.0,
        width=1.0,
        height=1.0,
        mat_type=None,
        fab_method=[],
    ):
        super().__init__(name, length, width, height, mat_type, fab_method)

    def calc_area(self):
        self.area = self.length * self.width


class Basement(Component):

    def __init__(
        self,
        name="basement",
        length=1.0,
        width=1.0,
        height=1.0,
        mat_type=None,
        fab_method=[],
    ):
        super().__init__(name, length, width, height, mat_type, fab_method)


class Material:

    def __init__(self, name, vol, density, co2_per_weight, cost_per_unit):
        self.name = name                   # material name
        self.vol = vol                     # volume (m3) 
        self.density = density             # density  (kg/m3)
        self.co2_per_w = co2_per_weight    # co2 per weight  (kg co2 per kg)
        self.cost_per_unit = cost_per_unit # cost per unit (€/m³)

    def calc_weight(self):
        self.w = self.vol * self.density

    def calc_carbon(self):
        self.embodied_carbon = self.w * self.co2_per_w

        return self.embodied_carbon

    def calc_cost(self):
        self.cost = self.vol * self.cost_per_unit

        return self.cost


class Wood(Material):

    def __init__(
        self, name="wood", vol=1.0, density=600, co2_per_weight=-0.9, cost_per_unit=500
    ):
        super().__init__(name, vol, density, co2_per_weight, cost_per_unit)


class Concrete(Material):

    def __init__(
        self,
        name="concrete",
        vol=1.0,
        density=2400,
        co2_per_weight=0.15,
        cost_per_unit=120,
    ):
        super().__init__(name, vol, density, co2_per_weight, cost_per_unit)


class Membrane(Material):
    # PTFE (Polytetrafluoroethylene)
    def __init__(
        self,
        name="membrane",
        vol=1.0,
        density=2200,
        co2_per_weight=6.0,
        cost_per_unit=4000,
    ):
        super().__init__(name, vol, density, co2_per_weight, cost_per_unit)


class Fabrication:

    def __init__(
        self,
        proc_name,
        material_weight,
        component,
        proc_emission_factor,
        proc_energy_consumption,
        proc_cost_per_unit,
        energy_source_emission_factor,
    ):

        self.proc_name = proc_name    # Fabrication process name
        self.mat_w = material_weight  # Material weight (kg) from Material class
        self.comp = component         # Instance of Component class
        self.proc_emission_factor = proc_emission_factor       # Emission factor (kg CO₂/kg)
        self.proc_energy_consumption = proc_energy_consumption # Energy consumption (kWh/kg)
        self.proc_cost_per_unit = proc_cost_per_unit           # Cost per unit (€/unit)
        self.energy_source_emission_factor = energy_source_emission_factor  # Energy source emission factor (kg CO₂/kWh)

    def calc_cost(self):

        self.cost = self.comp.proc_unit * self.proc_cost_per_unit

        return self.cost

    def calc_co2(self):

        process_emissions = self.mat_w * self.proc_emission_factor
        energy_emissions = (
            self.mat_w
            * self.proc_energy_consumption
            * self.energy_source_emission_factor
        )
        self.co2 = process_emissions + energy_emissions

        return self.co2


class Cutting(Fabrication):

    def __init__(
        self,
        proc_name="cutting wood",
        component=None,
        material_weight=1.0,
        proc_emission_factor=0.02,
        proc_energy_consumption=0.1,
        proc_cost_per_m2=0.05,
        energy_source_emission_factor=0.4,
    ):

        if proc_name == "cutting membrane":
            proc_emission_factor = 0.02
            proc_energy_consumption = 0.1
            proc_cost_per_m2 = 2.0
            energy_source_emission_factor = 0.4

        super().__init__(
            proc_name,
            material_weight,
            component,
            proc_emission_factor,
            proc_energy_consumption,
            proc_cost_per_m2,
            energy_source_emission_factor,
        )

    def calc_cost(self):

        self.cost = self.comp.area * self.proc_cost_per_unit

        return self.cost


class Welding(Fabrication):

    def __init__(
        self,
        proc_name="welding membrane",
        component=None,
        material_weight=1.0,
        proc_emission_factor=0.25,
        proc_energy_consumption=0.8,
        proc_cost_per_m=5.0,
        energy_source_emission_factor=0.4,
    ):
        super().__init__(
            proc_name,
            material_weight,
            component,
            proc_emission_factor,
            proc_energy_consumption,
            proc_cost_per_m,
            energy_source_emission_factor,
        )

    def calc_cost(self):

        self.cost = self.comp.length * self.proc_cost_per_unit

        return self.cost


class Casting(Fabrication):

    def __init__(
        self,
        proc_name="casting concrete",
        component=None,
        material_weight=1.0,
        proc_emission_factor=0.15,
        proc_energy_consumption=0.4,
        proc_cost_per_m3=0.08,
        energy_source_emission_factor=0.4,
    ):
        super().__init__(
            proc_name,
            material_weight,
            component,
            proc_emission_factor,
            proc_energy_consumption,
            proc_cost_per_m3,
            energy_source_emission_factor,
        )

    def calc_cost(self):

        self.cost = self.comp.vol * self.proc_cost_per_unit

        return self.cost


if __name__ == "__main__":

    # parameters
    pavilion_name = "Into the woods"

    # setting properties for each component
    column_props = {
        "length": 2.0,
        "height": 0.4,
        "width": 0.2,
        "material": "Wood",
        "fab_method": ["Cutting"],
        "num_eles": 12,
    }
    beam_props = {
        "length": 2.5,
        "height": 0.4,
        "width": 0.2,
        "material": "Wood",
        "fab_method": ["Cutting"],
        "num_eles": 8,
    }
    roof_props = {
        "length": 5,
        "height": 0.0006,
        "width": 5,
        "material": "Membrane",
        "fab_method": ["Cutting", "Welding"],
        "num_eles": 3,
    }
    base_props = {
        "length": 1.2,
        "height": 0.3,
        "width": 1.2,
        "material": "Concrete",
        "fab_method": ["Casting"],
        "num_eles": 4,
    }

    # A dictionary includes properties of all components
    comp_dicts = {
        "Column": [column_props for _ in range(column_props["num_eles"])],
        "Beam": [beam_props for _ in range(beam_props["num_eles"])],
        "Roof": [roof_props for _ in range(roof_props["num_eles"])],
        "Basement": [base_props for _ in range(base_props["num_eles"])],
    }

    params = pavilion_name, comp_dicts
    main(params)
