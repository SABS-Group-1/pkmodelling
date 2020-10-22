import unittest
import pkmodel as pk
import numpy as np


class ModelTest(unittest.TestCase):
    """
    Tests the :class:`Model` class.
    """
    def test_default_init_attribute_values(self):
        """
        Tests default values in initialising model are correct.
        """
        test_model = pk.Model()
        default_values = {"clearance_rate": 1,
                        "vol_c": 1,
                        "dose": 1,
                        "subcutaneous_compartment": None,
                        "peripheral_compartments": [],
                        "number_of_compartments": 1,
                        "number_of_peripheral_compartments": 0
                        }
        assert(test_model.clearance_rate == default_values["clearance_rate"])
        assert(test_model.vol_c == default_values["vol_c"])
        assert(test_model.dose == default_values["dose"])
        assert(test_model.subcutaneous_compartment == default_values["subcutaneous_compartment"])
        assert(test_model.peripheral_compartments == default_values["peripheral_compartments"])
        assert(test_model.number_of_compartments == default_values["number_of_compartments"])
        assert(test_model.number_of_peripheral_compartments == default_values["number_of_peripheral_compartments"])

    def test_add_peripheral_compartments(self):
        """
        Tests add_peripheral_compartments adds 1 to object.no_of_peripheral_compartments and object.no_of_compartments
        """
        test_model = pk.Model()

        initial_compartments = [test_model.number_of_peripheral_compartments,  test_model.number_of_compartments]
    
        test_model.add_peripheral_compartment()

        new_compartments = [test_model.number_of_peripheral_compartments,  test_model.number_of_compartments]
        
        
        for i in range(len(initial_compartments)): 
            assert(new_compartments[i] == initial_compartments[i] +1)

    





        


        