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
