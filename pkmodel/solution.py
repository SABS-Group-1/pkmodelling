#
# Solution class
#

import matplotlib.pylab as plt


class Solution:
    """A Pharmokinetic (PK) model solution

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self):
        pass

    def plot(self, sol, name):
        fig = plt.figure()
        plt.plot(sol.t, sol.y[0, :], label=name + '- q_c')
        plt.plot(sol.t, sol.y[1, :], label=name + '- q_p1')
        plt.legend()
        plt.ylabel('drug mass [ng]')
        plt.xlabel('time [h]')
        plt.show()
