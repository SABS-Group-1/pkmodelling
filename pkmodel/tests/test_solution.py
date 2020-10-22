from unittest import TestCase
from unittest.mock import patch
import pkmodel as pk


class SolutionTest(TestCase):
    """
    Tests the :class:`Solution` class.
    """

    def test_worksForBothModels(self):
        """
        Checks whether the pkmodel.solution.Solution.system_of_equation method
        works for both intravenous and subcutaneous models.
        :return:
        """
        with patch.object(pk.Model, 'subcutaneous_compartment') as mock_subcutaneous_model:







