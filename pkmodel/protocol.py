#
# Protocol class
#

class Protocol:
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    value: numeric, optional
        an example paramter

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

    def make_continuous(self,time_start, time_finish):
        self.continuous = True
        self.continuous_period[0] = time_start
        self.continuous_period[1] = time_finish
    
    def add_instantaneous(self, time):
        self.dose_times.append(time)
        self.dose_times.sort()
    
    def change_dose(self, dose_amount):
        self.dose_amount = dose.amount
    
    def dose_at_time(self, t):
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



