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
        q_c, q_p1 = y
        transition = self.model.Q_p1 * (q_c / self.model.V_c - q_p1 / self.model.V_p1)
        dqc_dt = self.model.X - q_c / self.model.V_c * self.model.CL - transition
        dqp1_dt = transition
        return [dqc_dt, dqp1_dt]

    def solve(self):
        """
        Uses the scipy library to solve the initial value problem for the system of
        equations specified in the system_of_equations function,
        (we currently assume that the initial drug concentrations are zero)

        :return: scipy bunch object
        """
        t_eval = np.linspace(0, 1, 10)
        y0 = np.array([0.0, 0.0])

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
            plt.plot(self.solution.t, self.solution.y[i, :], label=name+"- cmpt"+str(i))
        plt.legend()
        plt.ylabel('drug mass [ng]')
        plt.xlabel('time [h]')
        plt.show()


if __name__ == "__main__":
    dummy_model = Model()
    solver = Solution(dummy_model)
    solution = solver.solve()
    solver.plot("Test")

