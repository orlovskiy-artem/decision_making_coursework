import numpy as np
import pandas as pd

from solution import DepSolution, Solution

def drop_missing(department_data, key_colname, value_colname, missing="___"):
    return department_data[department_data[value_colname]!="___"][[key_colname,value_colname]]

department_1 = pd.read_excel("./data/data.xlsx",sheet_name=0)
department_2 = pd.read_excel("./data/data.xlsx",sheet_name=1)
department_3 = pd.read_excel("./data/data.xlsx",sheet_name=2)
department_4 = pd.read_excel("./data/data.xlsx",sheet_name=3)

department_1_p_v = drop_missing(department_1,"v","P_1_v").set_index("v")["P_1_v"].to_dict()
department_1_q_w = drop_missing(department_1,"w","Q_1_w").set_index("w")["Q_1_w"].to_dict()
department_1_r_x = drop_missing(department_1,"x","R_1_x").set_index("x")["R_1_x"].to_dict()

department_2_p_v = drop_missing(department_2,"v","P_2_v").set_index("v")["P_2_v"].to_dict()
department_2_q_w = drop_missing(department_2,"w","Q_2_w").set_index("w")["Q_2_w"].to_dict()
department_2_r_x = drop_missing(department_2,"x","R_2_x").set_index("x")["R_2_x"].to_dict()

department_3_p_v = drop_missing(department_3,"v","P_3_v").set_index("v")["P_3_v"].to_dict()
department_3_q_w = drop_missing(department_3,"w","Q_3_w").set_index("w")["Q_3_w"].to_dict()
department_3_r_x = drop_missing(department_3,"x","R_3_x").set_index("x")["R_3_x"].to_dict()

department_4_p_v = drop_missing(department_4,"v","P_4_v").set_index("v")["P_4_v"].to_dict()
department_4_q_w = drop_missing(department_4,"w","Q_4_w").set_index("w")["Q_4_w"].to_dict()
department_4_r_x = drop_missing(department_4,"x","R_4_x").set_index("x")["R_4_x"].to_dict()

department_1_p_v_investments = np.array(sorted(department_1_p_v.keys()))
department_1_q_w_investments = np.array(sorted(department_1_q_w.keys()))
department_1_r_x_investments = np.array(sorted(department_1_r_x.keys()))

department_2_p_v_investments = np.array(sorted(department_2_p_v.keys()))
department_2_q_w_investments = np.array(sorted(department_2_q_w.keys()))
department_2_r_x_investments = np.array(sorted(department_2_r_x.keys()))

department_3_p_v_investments = np.array(sorted(department_3_p_v.keys()))
department_3_q_w_investments = np.array(sorted(department_3_q_w.keys()))
department_3_r_x_investments = np.array(sorted(department_3_r_x.keys()))

department_4_p_v_investments = np.array(sorted(department_4_p_v.keys()))
department_4_q_w_investments = np.array(sorted(department_4_q_w.keys()))
department_4_r_x_investments = np.array(sorted(department_4_r_x.keys()))


department_1_investments = [department_1_p_v_investments,
                            department_1_q_w_investments,
                            department_1_r_x_investments]

department_2_investments = [department_2_p_v_investments,
                            department_2_q_w_investments,
                            department_2_r_x_investments]

department_3_investments = [department_3_p_v_investments,
                            department_3_q_w_investments,
                            department_3_r_x_investments]

department_4_investments = [department_4_p_v_investments,
                            department_4_q_w_investments,
                            department_4_r_x_investments]

department_1_profits = [department_1_p_v,
                        department_1_q_w,
                        department_1_r_x]
department_2_profits = [department_2_p_v,
                        department_2_q_w,
                        department_2_r_x]
department_3_profits = [department_3_p_v,
                        department_3_q_w,
                        department_3_r_x]
department_4_profits = [department_4_p_v,
                        department_4_q_w,
                        department_4_r_x]

department_max_profits = [30, 30, 30, 30]
budget = 100

profits_list = [department_1_profits,
                department_2_profits,
                department_3_profits,
                department_4_profits]

investments_list = [department_1_investments,
                    department_2_investments,
                    department_3_investments,
                    department_4_investments]


# solver = Solution(profits_list[0],investments_list[0],30)
# solution = solver.solve(
# print(solution)
# print(solver._argmax_list)
solver = DepSolution(profits_list, investments_list, department_max_profits, budget)
solution = solver.solve()
print(solution)