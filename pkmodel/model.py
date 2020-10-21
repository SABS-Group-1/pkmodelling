#
# Model class
#

import matplotlib.pylab as plt
import numpy as np
import scipy.integrate


def dose(t, X):
    return X


def rhs(t, y, Q_p1, V_c, V_p1, CL, X):
    q_c, q_p1 = y
    transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
    dqc_dt = dose(t, X) - q_c / V_c * CL - transition
    dqp1_dt = transition
    return [dqc_dt, dqp1_dt]


class Model:
    """A Pharmokinetic (PK) model

    Parameters: specifying the model type
    ----------
    value: numeric, optional
        an example paramter
    """

    def __init__(self, model_type="IB", compartment_no=1, CL=1.0, V_c=1.0, V_p1=1, Q_p1=1, X=1):
        """
        Initialisation of the model class, fixed for one compartment and a discrete initial dose for now

        :param model_type: type of PK model (either intravenous bolus or subcutaneous)
        :param compartment_no: number of peripheral compartments
        :param CL: clearance rate from the central compartment
        :param Vc: volume of the central compartment
        :param Vp1: volume of the peripheral compartment
        :param Qp1: diffusion rate beween the central and the peripheral compartment
        :param X: (one-time) dose
        """

        self.model_type = model_type  # one of two str (IB, SC)
        self.compartment_no = compartment_no # should be positive int
        self.CL = CL # should be >0
        self.V_c = V_c # should be >0
        # possible for loop / list for later
        self.V_p1 = V_p1 # should be >0
        self.Q_p1 = Q_p1 # should be >0
        self.X = X # should be >0


    def solve(self):
        t_eval = np.linspace(0, 1, 10)
        y0 = np.array([0.0, 0.0])

        sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: rhs(t, y, self.Q_p1, self.V_c, self.V_p1, self.CL, self.X),
            t_span=[t_eval[0], t_eval[-1]],
            y0=y0, t_eval=t_eval
        )

        return sol


if __name__ == "__main__":
    model = Model()
    print(model.solve())
