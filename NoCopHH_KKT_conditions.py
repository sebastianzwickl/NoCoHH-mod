import pyomo.environ as py


def lower_load_equality(m, t):
    # primary energy efficiency factor: 3.43/2.5=1.372
    # equals energy demand per km for hydrogen and conventioanl fuels
    return m.v_q_fossil[t] / 1.372 + m.v_q_H2[t] - m.ts_load[t] == 0


def lower_emisions(m, t):
    return m.v_q_CO2[t] - m.c_alpha_fossil * m.v_q_fossil[t] == 0


def lower_langrange_1(m, t):
    return (
        m.ts_fossil[t]
        + m.dual_lambda_load[t] / 1.372
        - m.c_alpha_fossil * m.dual_lambda_CO2[t]
        - m.dual_mhu_fossil[t]
        == 0
    )


def lower_langrange_2(m, t):
    return m.v_p_H2[t] + m.dual_lambda_load[t] - m.dual_mhu_H2[t] == 0


def lower_lagrange_3(m, t):
    return m.ts_CO2[t] + m.dual_lambda_CO2[t] - m.dual_mhu_CO2[t] == 0


def lower_complementarity_1_1(m, t):
    return m.dual_mhu_fossil[t] <= m.big_M * m.u_fossil[t]


def lower_complementarity_1_2(m, t):
    return m.v_q_fossil[t] <= m.big_M * (1 - m.u_fossil[t])


def lower_complementarity_2_1(m, t):
    return m.dual_mhu_H2[t] <= m.big_M * m.u_H2[t]


def lower_complementarity_2_2(m, t):
    return m.v_q_H2[t] <= m.big_M * (1 - m.u_H2[t])


def lower_complementarity_3_1(m, t):
    return m.dual_mhu_CO2[t] <= m.big_M * m.u_CO2[t]


def lower_complementarity_3_2(m, t):
    return m.v_q_CO2[t] <= m.big_M * (1 - m.u_CO2[t])


def add_KKT_conditions_from_lower_level(m):

    # add equality constraints
    m.lower_load_equality = py.Constraint(
        m.set_time, rule=lower_load_equality, doc="Fossil+Hydrogen=Load (h1)"
    )

    m.lower_emisions = py.Constraint(
        m.set_time, rule=lower_emisions, doc="CO2 emissions = Alpha x Fossil (h2)"
    )

    # add inequality constraints (g1-g6)
    # implicit, see "add_decision_variables"

    # add KKT conditions

    # Lagrange conditions
    m.lower_langrange_1 = py.Constraint(
        m.set_time, rule=lower_langrange_1, doc="dL/d(q_Fossil,t) (L1)"
    )

    m.lower_langrange_2 = py.Constraint(
        m.set_time, rule=lower_langrange_2, doc="dL/d(q_H2,t) (L2)"
    )

    m.lower_lagrange_3 = py.Constraint(
        m.set_time, rule=lower_lagrange_3, doc="dL/d(q_CO2,t) (L3)"
    )

    # complementarity conditions
    m.lower_complementarity_1_1 = py.Constraint(
        m.set_time,
        rule=lower_complementarity_1_1,
        doc="Complementarity condition (C1.1)",
    )

    m.lower_complementarity_1_2 = py.Constraint(
        m.set_time,
        rule=lower_complementarity_1_2,
        doc="Complementarity condition (C1.2)",
    )

    m.lower_complementarity_2_1 = py.Constraint(
        m.set_time,
        rule=lower_complementarity_2_1,
        doc="Complementarity condition (C2.1)",
    )

    m.lower_complementarity_2_2 = py.Constraint(
        m.set_time,
        rule=lower_complementarity_2_2,
        doc="Complementarity condition (C2.2)",
    )

    m.lower_complementarity_3_1 = py.Constraint(
        m.set_time,
        rule=lower_complementarity_3_1,
        doc="Complementarity condition (C3.1)",
    )

    m.lower_complementarity_3_2 = py.Constraint(
        m.set_time,
        rule=lower_complementarity_3_2,
        doc="Complementarity condition (C3.2)",
    )

    return m
