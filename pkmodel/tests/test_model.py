import unittest
import pkmodel as pk


class ModelTest(unittest.TestCase):
    """
    Tests the :class:`Model` class.
    """
    def test_default_init_attribute_values(self):
        """
        Tests Model creation.
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
        



        


        