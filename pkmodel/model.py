#
# Model class
#

class Model:
    """A Pharmokinetic (PK) model

    Parameters: specifying the model type
    ----------
    value: numeric, optional
        an example paramter
    """

    def __init__(self, clearance_rate=1, vol_c=1, dose=1):
        self.clearance_rate = clearance_rate
        self.vol_c = vol_c
        self.dose = dose
        self.subcutaneous_compartment = None
        self.peripheral_compartments = []
        self.number_of_compartments = 1
        self.number_of_peripheral_compartments = 0
            
        if self.clearance_rate <= 0 or self.vol_c <= 0 or self.dose <= 0:
            raise ValueError("Inputted negative number")


        # check model param types
        if not isinstance(self.clearance_rate, (int,float)):
            raise TypeError("Clearance rate must be an int or float")
        if not isinstance(self.vol_c, (int,float)):
            raise TypeError("Central volume must be an int or float")
        if not isinstance(self.dose, (int,float)):
            raise TypeError("Dose must be an int or float")
        if not (isinstance(self.subcutaneous_compartment, (int,float)) or self.subcutaneous_compartment == None):
            raise TypeError("Subcutaneous compartment absorption rate must be None, int, or float")
        if not isinstance(self.peripheral_compartments, list):
            raise TypeError("Peripheral compartment data must be int the form of a list")
        if not isinstance(self.number_of_compartments, int):
            raise TypeError("Total number of compartments must be an int")
        if not isinstance(self.number_of_peripheral_compartments, int):
            raise TypeError("Total number of peripheral compartments must be an int")

    def add_subcutaneous_compartment(self, absorption_rate=1):
        if self.subcutaneous_compartment:
            raise AttributeError("There can only be one subcutaneous compartment.")
        else:
            self.subcutaneous_compartment = absorption_rate
            self.number_of_compartments += 1

    def add_peripheral_compartment(self, vol_p=1, q_p=1):  
        self.peripheral_compartments.append({"vol_p":vol_p, "q_p": q_p})
        self.number_of_compartments += 1
        self.number_of_peripheral_compartments += 1


if __name__ == "__main__":
    model = Model()
    model.add_peripheral_compartment(1,1)
    model.add_peripheral_compartment(2,2)
    print(model.peripheral_compartments[0]["q_p"], model.peripheral_compartments[1]["q_p"])
