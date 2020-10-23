#
# Protocol class
#

class Protocol:
    """A Pharmokinetic (PK) dosing protocol
    Allows for continuous or instantaneous (at one or more time points) dosing.
    Also allows to set up the dose X in ng.

    Parameters
    ----------
    dose_amount: numeric, optional, default=1
        This parameter takes in the amount of dose given - X ng
    continuous: logical, optional, default = False
        This parameter specifies whether or not the dose X ng is applied at
        a continuous rate of X ng per hour.
    continuous_period: numerical list, optional, default = [0, 0]
        This parameter specifies the time period over which continuous
        dosing is applied. The first number in the list is the time at which
        continuous dosing begins and the second number is when continuous
        dosing ends.
    instantaneous: logical, optional, default = True
        This parameter specifies whether any instantaneous doses of X ng
        take place.
    dose_times: numerical list, optional, default = [0]
        This parameter is a list of numerics that specify the times at which
        instantaneous doses of X ng are applied.

    """
    def __init__(self, dose_amount=1,
                 continuous=False, continuous_period=[0, 0],
                 instantaneous=True, dose_times=[0]):
        self.dose_amount = dose_amount
        self.continuous = continuous
        self.instantaneous = instantaneous
        self.dose_times = dose_times
        self.continuous_period = continuous_period
        self.dose_times.sort()

    def make_continuous(self, time_start, time_finish):
        """
        Paramater: time_start: The time that at which continuous dosing
        starts.
        Parameter: time_finish: The time at which continuous dosing
        finishes.
        This method modifies an object of class Protocol to convert the dosing
        protocol to continuous over a user specified time period.
        """
        self.continuous = True
        self.continuous_period[0] = time_start
        self.continuous_period[1] = time_finish

    def add_instantaneous(self, time):
        """
        Paramater: time: Additional time at which there will be added an
        instantaneous dose of X ng.
        This method modifies an object of class Protocol to add an additional
        user specified instantaneous dose time.
        """
        self.dose_times.append(time)
        self.dose_times.sort()

    def change_dose(self, dose_amount):
        """
        Paramater: dose_amount: The dosage given - X ng
        This method modfies the dose_amount parameter in the object of protocol
        class it is called on.
        """
        self.dose_amount = dose_amount

    def dose_at_time(self, t):
        """
        Paramater: t: time at which you want dose(t) to be returned.
        Returns: Dose(t) for the specific dosing protocol set up in the object
        of class Protocol.
        """
        dose_t_continuous, dose_t_instantaneous = 0, 0
        if self.instantaneous:
            if t in self.dose_times:
                dose_t_instantaneous = self.dose_amount

        if self.continuous:
            if t < self.continuous_period[1] and \
               t >= self.continuous_period[0]:
                dose_t_continuous = self.dose_amount

        dose_t = dose_t_continuous + dose_t_instantaneous
        return dose_t
