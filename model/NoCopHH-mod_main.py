import pandas as pd
import NoCopHH_mod_functions as Functions
import NoCopHH_constraints as Constraints
import NoCopHH_KKT_conditions as KKT
import NoCopHH_mod_write_IAMC as to_IAMC
import pyomo.environ as py
import numpy as np
from datetime import datetime
import os
import numpy as np


# read in input data and parameters
_str_inputs = "inputs.xlsx"
_inputs = pd.read_excel(_str_inputs, sheet_name=None)
_time, _constants = Functions.return_time_series_and_constants(_inputs)

# create and initialize concrete pyomo model
model = Functions.create_and_initialize_the_model(_time, _constants)

# add decision variables (upper, lower, and dual problem)
model = Functions.add_decision_variables(model)

# add objective function (upper level problem)
model = Functions.add_objective_function(model)

# add constraints
model = Constraints.add_upper_level_constraints(model)  # leader constraints
model = KKT.add_KKT_conditions_from_lower_level(model)  # KKT conditions

# model.con_upper_sum_hydrogen_and_future.deactivate()
# model.con_upper_constant_hydrogen_production.deactivate()

# solve model
solver = py.SolverFactory("gurobi")
solution = solver.solve(model)

print("Total revenues: %s" % np.round(model.objective(), 0))

_now = datetime.now().strftime("%Y%m%dT%H%M")
_results_name = "45Future-100CO2"
result_dir = os.path.join("result", "{}-{}".format(_results_name, _now))
if not os.path.exists(result_dir):
    os.makedirs(result_dir)

to_IAMC.write_results_to_ext_iamc_format(model, result_dir)
total_revenues = model.revenues_spot() + model.revenues_future() + model.revenues_H2() 
print(model.revenues_spot())
print(np.round(model.revenues_spot() / total_revenues * 100, 2))
print(np.round(model.revenues_future() / total_revenues * 100, 2))
print(np.round(model.revenues_H2() / total_revenues * 100, 2))

# print(model.revenues_spot.get_values())
# print(model.revenues_future.get_values())
# print(model.revenues_H2())
# print(sum(model.v_q_H2.get_values().values()))
