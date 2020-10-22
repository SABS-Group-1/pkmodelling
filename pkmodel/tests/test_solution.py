from unittest import TestCase
import unittest.mock as mock
import pkmodel as pk
import numpy as np
from parameterized import parameterized

class SolutionTest(TestCase):
    """
    Tests the :class:`Solution` class.
    """

    @parameterized.expand([
        ("negative", np.array([-1, -2]), ValueError)
    ])
    def test_initialValuesSolve(self, name, y0, err):
        """
        Checks whether the pkmodel.solution.Solution.solve method raises an error when
        calling the function with negative initial values or a negative time span
        :return:
        """
        from pkmodel.solution import Solution
        from pkmodel.model import Model

        solution = Solution(model=mock.Mock(spec=Model))

        if err:
            with self.assertRaises(err):
                solution.solve(y0=y0)
