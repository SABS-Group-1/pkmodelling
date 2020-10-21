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
