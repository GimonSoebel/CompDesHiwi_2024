class Material:
    def __init__(self, density, type):
        self.density = density # in kg/m³
        self.type = type

    def get_type(self):
        return self.type

    def get_density(self):
        return self.density
    
    def get_cost_per_m3(self):
        return self.cost_per_m3    
    
class Timber(Material):
    def __init__(self, type, density, cost_per_m3):
        super().__init__(density, type)
        self.name = "Timber_"+self.type
        self.cost_per_m3 = cost_per_m3 # in euro per m^3


class Concrete(Material):
    def __init__(self, type, density, cost_per_m3):
        super().__init__(density, type)
        self.name = "Concrete_"+self.type
        self.cost_per_m3 = cost_per_m3 # in euro per m^3

    def get_type(self):
        return self.type        

class Steel(Material):
    def __init__(self, type, density, cost_per_kg, streckgrenze, bruchfestigkeit, E_modul, waermeausdehnungskoeffizient, korrosionsbestaendigkeit):
        super().__init__(density, type)
        # Dichte Stahl 7850 kg/m³
        self.cost_per_kg = cost_per_kg
        self.streckgrenze = streckgrenze #  Streckgrenze 250 MPa to 500 MPa.
        self.bruchfestigkeit = bruchfestigkeit # Bruchfestigkeit in MPa, higher than yield strength
        self.e_modul = E_modul # Elastizitätsmodul (E-Modul) zwischen 195 - 210 GPa / kN/mm²
        self.waermeausdehnungskoeffizient = waermeausdehnungskoeffizient # Wärmeausdehnung around 12 x 10⁻⁶ /°C.
        # self.ductility = ductility # Duktilität
        self.korrosionsbestaendigkeit = korrosionsbestaendigkeit # Korrosionsbeständigkeit
        self.name = "Steel_" + self.type

    def get_cost_per_m3(self):
        return self.density * self.cost_per_kg   
    
    def get_streckgrenze(self):
        return self.streckgrenze

    def get_bruchfestigkeit(self):
        return self.bruchfestigkeit

    def get_e_modul(self):
        return self.e_modul

    def get_waermeausdehnungskoeffizient(self):
        return self.waermeausdehnungskoeffizient

    def get_korrosionsbestaendigkeit(self):
        return self.korrosionsbestaendigkeit
