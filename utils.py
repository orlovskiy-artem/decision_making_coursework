import numpy as np
import pandas as pd

def parse_data(path):
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

    profits_list = [department_1_profits,
                    department_2_profits,
                    department_3_profits,
                    department_4_profits]

    investments_list = [department_1_investments,
                        department_2_investments,
                        department_3_investments,
                        department_4_investments]

    return profits_list, investments_list

def drop_missing(department_data:pd.DataFrame, key_colname:str, value_colname:str, missing="___"):
    return department_data[department_data[value_colname]!="___"][[key_colname,value_colname]]

def write_report_to_file(report:str, path:str):
    with open(path,"w") as f:
        f.write(report)

def get_report(profits_list, investments_list, department_max_investments, budget, solution):
    report = ""
    report+=f"Загальна сума асигнувань на всі проекти = {budget}"+"\n"
    max_investments_string = " ".join([f"L_{i+1}={max_investment}" for i,max_investment in enumerate(department_max_investments)])
    report+=f"Верхні межі асигнувань відділів: "+max_investments_string+"\n"
    result, argmax = solution
    report+=f"Максимальний результат = {result}"+"\n"
    indexes_strings = []
    functions_strings = []
    cases_names = ["P","Q","R"]
    cases_args_numbers = ["V","W","X"]
    overall_score = 0
    overall_investment = 0
    for department_id in argmax:
        indexes_string = ""
        functions_string = ""
        department_profit = 0
        department_investment = 0
        for case_id in solution[1][department_id]:
            investment = solution[1][department_id][case_id]
            profit = profits_list[department_id][case_id][investment]
            department_profit += profit
            department_investment += investment
            functions_string+="{}({}) = {}    ".format(cases_names[case_id], investment, profit)
            indexes_string+=f"{cases_args_numbers[case_id]}={investment} "
        functions_string += "| Sum={}".format(department_profit)
        indexes_string += "| Sum={}".format(department_investment)
        indexes_strings.append(indexes_string)
        functions_strings.append(functions_string)
        overall_score+=department_profit
        overall_investment += department_investment
    report += "\n"
    report += "\n".join(indexes_strings)+"\n"
    report += f"Сума всіх інвестицій = {overall_investment}"+"\n\n"
    report += "\n".join(functions_strings)+"\n"
    report += f"Сума всіх доходів = {overall_score}"
    return report