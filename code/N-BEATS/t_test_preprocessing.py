from scipy import stats
import numpy as np
import json

with_files = {
    "carbs": "./carbs_pre_processing_nbeats.json",
    "bolus": "./bolus_pre_processing_nbeats.json",
}

without_files = {
    "carbs": "./carbs_no_pre_processing_nbeats.json",
    "bolus": "./bolus_no_pre_processing_nbeats.json",
}

with_no_added_meals_files = {
    "carbs": "./carbs_pre_processing_no_added_meals_nbeats.json"
}

best = {
    "carbs": "AVG",
    "bolus": "AVG",
}

patient_lists = {
    "carbs": ["540", "544", "552", "559", "563", "575", "584", "588", "591", "596"],
    "bolus": ["540", "552", "559", "563", "570", "575", "584", "588", "591", "596"],
}

p_values = {}

for s in ["carbs", "bolus"]:
    p_values[s] = {}
    fd1 = open(with_files[s], "r")
    fd2 = open(without_files[s], "r")
    if s == "carbs":
        fd3 = open(with_no_added_meals_files[s], "r")

    yes = json.load(fd1)
    no = json.load(fd2)
    if s == "carbs":
        yes_no_added = json.load(fd3)

    fd1.close()
    fd2.close()
    if s == "carbs":
        fd3.close()

    yes_rmse = []
    yes_mae = []

    no_rmse = []
    no_mae = []

    yes_no_added_rmse = []
    yes_no_added_mae = []

    for p in patient_lists[s]:
        yes_rmse.append(yes["by_patient"][best[s]][p]["RMSE"])
        yes_mae.append(yes["by_patient"][best[s]][p]["MAE"])

        no_rmse.append(no["by_patient"][best[s]][p]["RMSE"])
        no_mae.append(no["by_patient"][best[s]][p]["MAE"])

        if s == "carbs":
            yes_no_added_rmse.append(yes_no_added["by_patient"][best[s]][p]["RMSE"])
            yes_no_added_mae.append(yes_no_added["by_patient"][best[s]][p]["MAE"])

    yes_rmse = np.array(yes_rmse)
    yes_mae = np.array(yes_mae)

    no_rmse = np.array(no_rmse)
    no_mae = np.array(no_mae)

    if s == "carbs":
        yes_no_added_rmse = np.array(yes_no_added_rmse)
        yes_no_added_mae = np.array(yes_no_added_mae)

    yes_no_p_rmse = stats.ttest_rel(yes_rmse, no_rmse, alternative="less").pvalue
    yes_no_p_mae = stats.ttest_rel(yes_mae, no_mae, alternative="less").pvalue
    if s == "carbs":
        yes_no_added_no_p_rmse = stats.ttest_rel(
            yes_no_added_rmse, no_rmse, alternative="less"
        ).pvalue
        yes_no_added_no_p_mae = stats.ttest_rel(
            yes_no_added_mae, no_mae, alternative="less"
        ).pvalue

    p_values[s]["yes_no"] = {"RMSE": yes_no_p_rmse, "MAE": yes_no_p_mae}
    if s == "carbs":
        p_values[s]["yes_wo_imputed_meals_no"] = {
            "RMSE": yes_no_added_no_p_rmse,
            "MAE": yes_no_added_no_p_mae,
        }

fd = open("p_values_preprocessing.json", "w")
json.dump(p_values, fd, indent=4)
