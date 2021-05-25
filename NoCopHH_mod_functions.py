import pyomo.environ as py


def return_time_series_and_constants(file):

    _time_series = file["Time series"].set_index("Time")
    _constants = file["Constants"]
    # scenario analysis
    return _time_series, _constants


def init_spot(m, t):
    return m.time["Spot"][t]


def init_gen(m, t):
    return m.time["Generation"][t]


def init_load(m, t):
    return m.time["Load"][t]


def init_fossil(m, t):
    return m.time["Fossil"][t]


def init_co2(m, t):
    return m.time["CO2"][t]


def create_and_initialize_the_model(time, con):

    m = py.ConcreteModel()
    m.set_time = py.Set(initialize=time.index)
    m.time = time
    m.con = con

    # add time series data to framework
    m.ts_spot = py.Param(m.set_time, initialize=init_spot)
    m.ts_gen = py.Param(m.set_time, initialize=init_gen)
    m.ts_load = py.Param(m.set_time, initialize=init_load)
    m.ts_fossil = py.Param(m.set_time, initialize=init_fossil)
    m.ts_CO2 = py.Param(m.set_time, initialize=init_co2)

    # add constants/parameters to framework
    m.c_future = py.Param(initialize=con["Future"][0])
    m.c_base = py.Param(initialize=con["Base"][0])
    m.c_alpha_fossil = py.Param(initialize=con["Alpha_fossil"][0])

    m.big_M = py.Param(initialize=10e7)

    return m


def add_decision_variables(m):

    # upper level
    # Implicit definition of inequality constraint (G1)
    m.v_q_spot = py.Var(m.set_time, domain=py.NonNegativeReals)
    # Implicit definition of inequality constraint (G2)
    m.v_q_future = py.Var(m.set_time, domain=py.NonNegativeReals)
    # Implicit definition of inequality constraint (G3)
    m.v_q_curtail = py.Var(m.set_time, domain=py.NonNegativeReals)
    # Implicit definition of inequality constraint (g2)
    m.v_p_H2 = py.Var(m.set_time, domain=py.NonNegativeReals)

    m.v_H2_snake = py.Var(domain=py.NonNegativeReals)
    m.v_future_snake = py.Var(domain=py.NonNegativeReals)

    # lower level (primal)
    m.v_q_fossil = py.Var(m.set_time, domain=py.NonNegativeReals)
    m.v_q_H2 = py.Var(m.set_time, domain=py.NonNegativeReals)
    m.v_q_CO2 = py.Var(m.set_time, domain=py.NonNegativeReals)

    # lower level (dual)
    # equality constraints (lambda)
    m.dual_lambda_load = py.Var(m.set_time)
    m.dual_lambda_CO2 = py.Var(m.set_time)

    # inequality constraints (mhu)
    m.dual_mhu_fossil = py.Var(m.set_time, domain=py.NonNegativeReals)
    m.dual_mhu_H2 = py.Var(m.set_time, domain=py.NonNegativeReals)
    m.dual_mhu_CO2 = py.Var(m.set_time, domain=py.NonNegativeReals)

    # Big M method (binary variables)
    m.u_fossil = py.Var(m.set_time, domain=py.Binary)
    m.u_H2 = py.Var(m.set_time, domain=py.Binary)
    m.u_CO2 = py.Var(m.set_time, domain=py.Binary)

    # add cost types
    m.revenues_spot = py.Var()
    m.revenues_future = py.Var()
    m.revenues_H2 = py.Var()

    return m


def revenues_spot(m):
    _revenues = 0
    for t in m.set_time:
        _revenues += m.v_q_spot[t] * m.ts_spot[t]
    return _revenues == m.revenues_spot


def revenues_future(m):
    _revenues = 0
    for t in m.set_time:
        _revenues += m.v_q_future[t] * m.c_future
    return _revenues == m.revenues_future


def revenues_hydrogen(m):
    return m.revenues_H2 == -sum(
        m.dual_lambda_load[t] * m.ts_load[t]
        + m.v_q_fossil[t] * m.ts_fossil[t]
        + m.v_q_CO2[t] * m.ts_CO2[t]
        for t in m.set_time
    )


def objective_function_maximize_revenues(m):
    return m.revenues_spot + m.revenues_future + m.revenues_H2


def add_objective_function(m):
    m.rev_spot = py.Constraint(rule=revenues_spot)
    m.rev_future = py.Constraint(rule=revenues_future)
    m.rev_hydrogen = py.Constraint(rule=revenues_hydrogen)

    m.objective = py.Objective(
        expr=objective_function_maximize_revenues(m), sense=py.maximize
    )
    return m
