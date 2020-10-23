from unittest import TestCase
from unittest.mock import MagicMock
import numpy as np
import numpy.testing as npt
from parameterized import parameterized


class SolutionTest(TestCase):
    """
    Tests the :class:`Solution` class.
    """
    def test_justCentralCompartment(self):
        """
        Checking whether a solution is calculated when the model is run solely with a central compartment
        :return:
        """

        from pkmodel.model import Model
        from pkmodel.solution import Solution

        model = Model()
        solution = Solution(model)
        solution.solve()

    def test_justSubcutaneousCompartment(self):
        """
        Checking whether a solution is calculated when the model is run with a subcutaneous,
        but no peripheral compartments
        :return:
        """

        from pkmodel.model import Model
        from pkmodel.solution import Solution

        model = Model()
        model.add_subcutaneous_compartment()
        solution = Solution(model)
        solution.solve()

    def test_complexModel(self):
        """
        Checking whether a solution is calculated when a complex model is run (subcutaneous + 5 peripheral compartments)
        :return:
        """

        from pkmodel.model import Model
        from pkmodel.solution import Solution

        model = Model()
        model.add_subcutaneous_compartment()
        for _ in range(0, 5):
            model.add_peripheral_compartment()
        solution = Solution(model)
        solution.solve()

    @parameterized.expand([
        ('zero', np.array([0.0, 0.0]), None),
        ('positive', np.array([1.0, 2.0]), None),
        ("negative", np.array([-1.0, -2.0]), ValueError),
        ("not_np", np.inf, TypeError),
        ("not_float", np.array([0, 0]), TypeError)
    ])
    def test_initialValuesSolve(self, name, y0, err):
        """
        Checks whether the pkmodel.solution.Solution.solve method raises an error when
        calling the function with negative or non-array/non-float initial values
        :return:
        """
        from pkmodel.solution import Solution
        from pkmodel.model import Model

        solution = Solution(model=MagicMock(spec=Model))
        solution.system_of_equations = MagicMock(return_value=1)

        if err:
            with self.assertRaises(err):
                solution.solve(y0=y0)
        else:
            solution.solve(y0=y0)

    @parameterized.expand([
        ('model1', 1.0, 1.0, 1.0, 1.0, 1.0,
         np.array([0., 0.2, 0.33, 0.42, 0.49]),
         np.array([0., 0.02, 0.08, 0.14, 0.21])),
        ('model2', 2.0, 1.0, 1.0, 1.0, 1.0,
         np.array([0., 0.18, 0.29, 0.37, 0.44]),
         np.array([0., 0.04, 0.12, 0.21, 0.29])
         )
    ])
    def test_prototypeResults(self, name, Q_p1, V_c, V_p1, CL, X, result_c, result_p):
        """
        Inputs the parameter sets from the prototype class and checks whether
        our programme produces the same output (for a reduced number of 5 timesteps)
        :param name: name of our model
        :param Q_p1: transfer rate
        :param V_c: volume of the central compartment
        :param V_p1: volume of the peripheral compartment
        :param CL: clearance rate
        :param X: drug dosing
        :param result_c: result for the central compartment from the prototype.py file
        :param result_p: result for the peripheral compartment from the prototype.py file
        :return:
        """
        from pkmodel.model import Model
        from pkmodel.solution import Solution

        model = Model(clearance_rate=CL, vol_c=V_c, dose=X)
        model.add_peripheral_compartment(vol_p=V_p1, q_p=Q_p1)

        solution = Solution(model)
        solution.solve(y0=np.array([0.0, 0.0]), t_eval=np.linspace(0, 1, 5))

        npt.assert_almost_equal(solution.solution.y[0], result_c, decimal=2)
        npt.assert_almost_equal(solution.solution.y[1], result_p, decimal=2)

    @parameterized.expand([
        (1, 1), (2, 1), (1, 2)
    ])
    def test_peripheralEquality(self, vol_p, q_p):
        """
        Check whether the concentrations in 2, and 3 peripheral compartments are identical if they are initialized
        with identical parameters.

        :param name: name of our model
        :param vol_p: volume of our compartments
        :param q_p: transfer rate of our compartments
        :return:
        """

        from pkmodel.model import Model
        from pkmodel.solution import Solution

        # check everything for two peripheral compartments

        model = Model()
        model.add_peripheral_compartment(vol_p=vol_p, q_p=q_p)
        model.add_peripheral_compartment(vol_p=vol_p, q_p=q_p)

        solution = Solution(model)
        solution.solve()

        npt.assert_array_equal(solution.solution.y[1], solution.solution.y[2])

        # checks the same for three peripheral compartments

        model.add_peripheral_compartment(vol_p=vol_p, q_p=q_p)

        solution = Solution(model)
        solution.solve()

        npt.assert_array_equal(solution.solution.y[1], solution.solution.y[2])
        npt.assert_array_equal(solution.solution.y[2], solution.solution.y[3])

    def test_central_compartment(self):
        """
        Tests that system of equations works for a single (central) compartment.
        """
        
        from pkmodel.model import Model
        from pkmodel.solution import Solution
        
        solution = Solution(Model())
        differentials = solution.system_of_equations(1, ([0.]))
        assert(differentials == ([1.]))


