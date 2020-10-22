#
# Solution class
#

import matplotlib.pylab as plt
from pkmodel.model import Model
import numpy as np
import scipy.integrate


class Solution:
    """Accepts a pharmacokinetic model and solves it,
    either returning a plot or arrays of the drug concentrations over time
    """

    def __init__(self, model):
        """

        :param model: model object containing all relevant initial values
        :arg solution: serves as the variable to which solutions are saved
        """
        self.model = model
        self.solution = None

    def system_of_equations(self, t, y):
        """
        Implements the algebraic ODE formula from the project description in python
        and evaluates it at a specific time point

        :param t: point in time, only relevant if you have a continuous dosing protocol
        :param y: value from which the ODE expression is calculated
        :return: derivative of drug concentrations with respect to time
        """

        # we initialize concentrations and derivatives for each compartment
        # the notation goes as follows:
        # 0 is the central compartment
        # if we have a subcutaneous compartment, it goes last
        # the peripheral components go [1,last-1) (or [1,last), if there's no subcutaneous compartment)
        # this way we can reuse the code to calculate the transitions of the peripheral compartments

        qi = y  # we initialize all concentrations to y
        dqi_dt = np.zeros(self.model.number_of_compartments)  # and all derivatives to zero

        # we then calculate the transitions for each peripheral compartment
        # CAUTION: be aware of the the slightly awkward situation where we loop from
        # 0 through the parameters of the peripheral compartments, but from 1 through the
        # concentration array

        transitions = np.zeros(self.model.number_of_peripheral_compartments)
        for i in range(0, self.model.number_of_peripheral_compartments):
            transitions[i] = self.model.peripheral_compartments[i]['q_p'] * \
                             (qi[0] / self.model.vol_c -
                              qi[i + 1] / self.model.peripheral_compartments[i]['vol_p'])

        # depending on the model type, we calculate the derivative of the central compartment

        if self.model.subcutaneous_compartment:
            dqi_dt[0] = self.model.subcutaneous_compartment * qi[self.model.number_of_compartments - 1] \
                        - qi[0] / self.model.vol_c - np.sum(transitions)
        else:
            dqi_dt[0] = self.model.dose - qi[0] / self.model.vol_c - np.sum(transitions)

        # we now set the derivatives of the peripheral compartments as the transitions calculated above
        # and check whether we have to calculate the last derivative differently, in case of
        # a subcutaneous model

        for i in range(1, self.model.number_of_compartments):
            if self.model.subcutaneous_compartment and i == self.model.number_of_compartments-1:
                dqi_dt[i] = self.model.dose - self.model.subcutaneous_compartment \
                                 * qi[self.model.number_of_compartments-1]
            else:
                dqi_dt[i] = transitions[i - 1]

        return dqi_dt

    def solve(self, y0=None, t_eval=np.linspace(0, 1, 1000)):
        """
        Uses the scipy library to solve the initial value problem for the system of
        equations specified in the system_of_equations function,
        (we currently assume that the initial drug concentrations are zero)

        :return: scipy bunch object
        """

        if y0 is None:
            y0 = np.zeros(self.model.number_of_compartments)

        if not np.greater(y0, 0.0):
            raise ValueError("The initial concentration cannot be larger than zero.")

        sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: self.system_of_equations(t, y),
            t_span=[t_eval[0], t_eval[-1]],
            y0=y0, t_eval=t_eval)

        self.solution = sol

    def plot(self, name):
        """
        Plots the concentrations in the different compartments over time

        :param sol: the bunch object returned by the scipy ODE solver
        :param name: the name of the model in question, e.g. IV, 2 peripheral compartments
        :return: ---
        """
        fig = plt.figure()

        for i in range(0, self.solution.y.shape[0]):
            plt.plot(self.solution.t, self.solution.y[i, :], label=name + "- cmpt" + str(i))
        plt.legend()
        plt.ylabel('drug mass [ng]')
        plt.xlabel('time [h]')
        plt.show()


if __name__ == "__main__":
    dummy_model = Model()
    dummy_model.add_peripheral_compartment()
    solver = Solution(dummy_model)
    solver.solve()
    solver.plot("Test")
