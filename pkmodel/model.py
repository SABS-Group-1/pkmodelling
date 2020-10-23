#
# Model class
#

class Model:
    """A Pharmokinetic (PK) model.
    Defaults to Intravenous Bolus.
    Adding subcutaneous compartment changes model type
    """

    def __init__(self, clearance_rate=1, vol_c=1, dose=1):
        """Initialise model object param values

        :param clearance_rate: int/float describing drug elim rate
                               from central compartment [ml/h]
        :param vol_c: int/float describing volume of central compartment [ml]
        :param dose: int/float dosing function [ng/h]
        :arg subcutaenous_compartment: int/float describes absorption rate [/h]
                                       Assume IVB model so defaults to None
        :arg peripheral_compartments: initialised as empty list
        :arg number_of_compartments: int initialised to 1
                                     for central compartment only
        :arg number_of_peripheral_compartments: int initialised to 0
        :return: ---
        """
        self.clearance_rate = clearance_rate
        self.vol_c = vol_c
        self.dose = dose
        self.subcutaneous_compartment = None
        self.peripheral_compartments = []
        self.number_of_compartments = 1
        self.number_of_peripheral_compartments = 0

        # check model param values are physically valid
        if self.clearance_rate <= 0 or self.vol_c <= 0 or self.dose <= 0:
            raise ValueError("Inputted negative number")

        # check model param types
        if not isinstance(self.clearance_rate, (int, float)):
            raise TypeError("Clearance rate must be an int or float")
        if not isinstance(self.vol_c, (int, float)):
            raise TypeError("Central volume must be an int or float")
        if not isinstance(self.dose, (int, float)):
            raise TypeError("Dose must be an int or float")
        if not (isinstance(self.subcutaneous_compartment, (int, float))
                or self.subcutaneous_compartment is None):
            raise TypeError("SC compart. abs. rate must be None, int or float")
        if not isinstance(self.peripheral_compartments, list):
            raise TypeError("Peripheral compartment data must be list")
        if not isinstance(self.number_of_compartments, int):
            raise TypeError("Total number of compartments must be an int")
        if not isinstance(self.number_of_peripheral_compartments, int):
            raise TypeError("Total no. of peripheral compartments must be int")

    def add_subcutaneous_compartment(self, absorption_rate=1):
        '''Adds subcutaneous compartment to model with absorption rate specified.

        :param absorption_rate: int/float describing absorp. rate for SC [/h]
        :return: ---
        '''
        if self.subcutaneous_compartment:
            raise AttributeError("There can only be one SC compartment")
        else:
            self.subcutaneous_compartment = absorption_rate
            self.number_of_compartments += 1

    def add_peripheral_compartment(self, pc_name=None, vol_p=1, q_p=1):
        '''Adds peripheral compartment to model.
        Valid for both IVB and SC.

        :param vol_p: int/float describing volume of per comp [ml]
        :param q_p: int/float describing drug quantiyin  per comp [ng]
        :return: ---
        '''
        if not pc_name:
            pc_name = "Peripheral Compartment {}".format(
                self.number_of_peripheral_compartments + 1)
        self.peripheral_compartments.append(
            {"name": pc_name, "vol_p": vol_p, "q_p": q_p})
        self.number_of_compartments += 1
        self.number_of_peripheral_compartments += 1
