from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
import pkmodel as pk
import numpy as np
from parameterized import parameterized


class SolutionTest(TestCase):
    """
    Tests the :class:`Solution` class.
    """

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
        ('model1', 1.0, 1.0, 1.0, 1.0, 1.0),
        ('model2', 2.0, 1.0, 1.0, 1.0, 1.0)
    ])
    def prototypeResults(self, name, Q_p1, V_c, V_p1, CL, X):
        """
        Inputs the parameter sets from the prototype class and checks whether
        our programme produces the same output.
        :param name: name of our model
        :param Q_p1: transfer rate
        :param V_c: volume of the central compartment
        :param V_p1: volume of the peripheral compartment
        :param CL: clearance rate
        :param X: drug dosing
        :return:
        """
        from pkmodel.model import Model
        from pkmodel.solution import Solution

        model = Model(clearance_rate=CL, vol_c=V_c, dose=X)
        model.add_peripheral_compartment(vol_p=V_p1, q_p=Q_p1)

        solution = Solution(model)
        result = solution.solve(y0=np.array([0.0, 0.0]), t_eval=np.linspace(0, 1, 1000))




