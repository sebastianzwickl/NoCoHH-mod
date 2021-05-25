import pyomo.environ as py


def upper_load(m, t):
    # Equality constraint (H1)
    _hydrogen_efficiency = 0.5
    _production = (
        m.v_q_spot[t]
        + m.v_q_curtail[t]
        + m.v_q_future[t]
        + m.v_q_H2[t] / _hydrogen_efficiency
    )
    return _production - m.ts_gen[t] == 0


def upper_constant_hydrogen_production(m, t):
    # Equality constraint (H2)
    return m.v_q_H2[t] - m.v_H2_snake == 0


def upper_constant_future_production(m, t):
    # Equality constraint (H3)
    return m.v_q_future[t] - m.v_future_snake == 0


def upper_sum_hydrogen_and_future(m):
    # Equality constraint (H4)
    _hydrogen_efficiency = 0.5
    return m.v_H2_snake / _hydrogen_efficiency + m.v_future_snake - m.c_base == 0


def add_upper_level_constraints(m):

    m.con_upper_load = py.Constraint(m.set_time, rule=upper_load)
    m.con_upper_constant_hydrogen_production = py.Constraint(
        m.set_time, rule=upper_constant_hydrogen_production
    )
    m.con_upper_constant_future_production = py.Constraint(
        m.set_time, rule=upper_constant_future_production
    )
    m.con_upper_sum_hydrogen_and_future = py.Constraint(
        rule=upper_sum_hydrogen_and_future
    )

    return m
