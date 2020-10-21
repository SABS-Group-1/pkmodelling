#
# Model class
#

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
