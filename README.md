![Unit tests on multiple python versions (3.6-3.8)](https://github.com/SABS-Group-1/pkmodelling/workflows/Run%20unit%20tests%20with%20all%20supported%20python%20versions%20(3.6-3.8)/badge.svg)
![Unit tests on multiple operating systems](https://github.com/SABS-Group-1/pkmodelling/workflows/Unit%20tests%20(OS%20versions)/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/pkmodelling/badge/?version=latest)](https://pkmodelling.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/SABS-Group-1/pkmodelling/branch/master/graph/badge.svg?token=05UPUHBXCN)](undefined)
[![BCH compliance](https://bettercodehub.com/edge/badge/SABS-Group-1/pkmodelling?branch=master)](https://bettercodehub.com/)

# PK Modelling (SABS:R3 2020)

This is a package that allows the user to calculate drug pharmacokinetics for two different non-physiological models:
- Intravenous Bolus dosing (dose administered directly to a central compartment)
- Subcutaneous dosing (dose administered to a separate compartment from which it is absorbed into the central one)

## Modelling Assumptions

For both of the above-mentioned models, 
we assume that the organism can be divided in kinetically homogeneous compartments.
After the drug enters the central compartment (either by direct infusion or through the 
subcutaneous compartment), it is both cleared at a constant rate and
diffuses into an arbitrary number of peripheral compartments. This is meant to model the 
circulatory concentration of a drug to check whether it exceeds certain toxicity and efficacy thresholds.

In the case of a simple instance with only one peripheral compartment,
the models are described by the following systems of equations.

 intravenous dosing              |  subcutaneous dosing
:-------------------------:|:-------------------------:
![image](docs/pictures/iv_ODE.png)  |  ![image](docs/pictures/sc_ODE.png)

The case for more than one peripheral compartment is calculated accordingly.

## Installing the Package

The latest release of the package can be installed directly through by opening a console and typing:
```
$ pip3 install -i https://test.pypi.org/simple/ pkmodelling-sabs-group1
```
The model is maintained for python 3.6 and newer.

## Using the Package

When initialising the Model class, the package creates a model
that consists solely of the central compartment. Note that in this version
the dose is only implemented as a constant addition at every time step.

``` 
import pkmodelling_sabs_group1 as pk

model = pk.model.Model(clearance_rate=1, vol_c=1, dose=1)
```

You are then able to add one subcutaneous 
and/or arbitrarily many peripheral compartments.

```
model.add_subcutaneous_compartment(absorption_rate=2)
model.add_peripheral_compartment(pc_name="Compartment 1", vol_p=2, q_p=3)
model.add_peripheral_compartment(pc_name="Compartment 2", vol_p=4, q_p=5)
```

In order to solve the model you specified above, you initialise a
Solution class and run the solve method. The standard initial values are 0 for the drug 
concentration in each compartment and a timespan of [0,1) divided into 1000 time steps.

```
sol = pk.solution.Solution(model=model)
sol.solve()
```

You are then able to generate a plot that shows you the change in concentration
for each compartment over time.

```
sol.plot("MyModel")
```