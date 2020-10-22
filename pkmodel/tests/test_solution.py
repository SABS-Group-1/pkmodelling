import unittest
import pkmodel as pk
import numpy


class SolutionTest(unittest.TestCase):
    """
    Tests the :class:`Solution` class.
    """
    def test_central_compartment(self):
        """
        Tests that system of equations works for a single (central) compartment.
        """
        solution=pk.Solution(pk.Model())
        differentials=solution.system_of_equations(1, ([0.]))
        assert(differentials == ([1.]))

    