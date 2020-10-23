# import pkmodelling_sabs_group1 as pk  # if the package is installed through pip
import pkmodel as pk  # if the package is downloaded directly

# introduces a continuous dose of 1 for the first half of the
# simulated time

protocol = pk.protocol.Protocol(dose_amount=1)
protocol.make_continuous(time_start=0, time_finish=0.5)


model = pk.model.Model(clearance_rate=1, vol_c=1)

#the starting model only has a central compartment and assumes intravenous dosing
#to change this model use the functions below

model.add_subcutaneous_compartment(absorption_rate=2)  # needed if the dosing protocol is subcutaneous
model.add_peripheral_compartment(pc_name="Compartment 1", vol_p=2, q_p=3)  # adds a peripheral compartment
model.add_peripheral_compartment()

sol = pk.solution.Solution(model=model, protocol=protocol)
sol.solve()
sol.plot("MyModel")
