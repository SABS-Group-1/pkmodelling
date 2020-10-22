import unittest
import pkmodel as pk
import numpy as np
from parameterized import parameterized


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


    def test_add_peripheral_compartments_increases_compartments(self):
        """
        Tests add_peripheral_compartments adds 1 to object.no_of_peripheral_compartments and object.no_of_compartments
        """
        test_model = pk.Model()
        initial_compartments = [test_model.number_of_peripheral_compartments,  test_model.number_of_compartments]
        assert(len(test_model.peripheral_compartments) == test_model.number_of_peripheral_compartments)

        test_model.add_peripheral_compartment()
        new_compartments = [test_model.number_of_peripheral_compartments,  test_model.number_of_compartments]
        assert(len(test_model.peripheral_compartments) == test_model.number_of_peripheral_compartments)

        for i in range(len(initial_compartments)): 
            assert(new_compartments[i] == initial_compartments[i] +1)


    def test_vol_and_quantity_peripheral_compartments(self):
        '''
        Test that the vol & drug quantity in a peripheral compartment are uploaded correctly
        '''
        test_model = pk.Model()

        vol_p, q_p = 10, 20
        test_model.add_peripheral_compartment(vol_p, q_p)
        assert(test_model.peripheral_compartments[0]["vol_p"] == vol_p)
        assert(test_model.peripheral_compartments[0]["q_p"] == q_p)

        vol_p, q_p = 30, 40
        test_model.add_peripheral_compartment(vol_p, q_p)
        assert(test_model.peripheral_compartments[1]["vol_p"] == vol_p)
        assert(test_model.peripheral_compartments[1]["q_p"] == q_p)

    def test_subcutaneous_compartment_equals_absorption(self):

        '''
        Test subcutaneous compartment equals absorption rate
        '''

        test_model_default = pk.Model()
        test_model = pk.Model()

        assert(test_model.subcutaneous_compartment == None)
        assert(test_model_default.subcutaneous_compartment == None)

        test_model_default.add_subcutaneous_compartment()
        assert(test_model_default.subcutaneous_compartment == 1)

        abs_rate = 10
        test_model.add_subcutaneous_compartment(absorption_rate = abs_rate)
        assert(test_model.subcutaneous_compartment == abs_rate)


    def test_add_subcutaneous_compartments_increases_compartments(self): 

        '''
        Test add_subcutaneous_compartments adds 1 to object.no_of_compartments
        '''
        test_model = pk.Model()

        initial_no_of_compartments = test_model.number_of_compartments

        test_model.add_subcutaneous_compartment()
        assert(test_model.number_of_compartments == initial_no_of_compartments + 1)

            
    def test_cannot_add_more_than_1_sc_compartment(self):
        '''
        Adding more than one SC compartment should raise Attribute Error.
        '''    
        test_model = pk.Model()
        assert(test_model.subcutaneous_compartment == None)

        test_model.add_subcutaneous_compartment()
        assert(test_model.subcutaneous_compartment != None)

        with self.assertRaises(AttributeError):
            test_model.add_subcutaneous_compartment()


    @parameterized.expand([
        ([100], TypeError),
        ("10", TypeError),
        ])      
    def test_model_params_valid_type(self, input, expected):

        '''
        Test TypeErrors are raised for invalid model params
        '''
        with self.assertRaises(expected):
            test_model = pk.Model(clearance_rate = input)
        with self.assertRaises(expected):
            test_model = pk.Model(vol_c = input)
        with self.assertRaises(expected):
            test_model = pk.Model(dose = input)


    @parameterized.expand([
        (-1, ValueError)
        ])
    def test_default_values_positivity(self, input, expected):
        '''
        Test TypeErrors are raised for invalid model params
        '''

        test_model2 = pk.Model()
        test_model2.number_of_compartments = -1
        test_model2.number_of_peripheral_compartments = -1

        with self.assertRaises(expected):
            test_model = pk.Model(clearance_rate = input)
        with self.assertRaises(expected):
            test_model = pk.Model(vol_c = input)
        with self.assertRaises(expected):
            test_model = pk.Model(dose = input)
        #with self.assertRaises(expected):
        #    test_model2 = pk.Model()
        #    test_model2.number_of_compartments = -1
        #    test_model2.number_of_compartments = input
        #with self.assertRaises(expected):
        #    test_model2.number_of_peripheral_compartments = input
    
        #missing a couple of initial parameters (None and list)


