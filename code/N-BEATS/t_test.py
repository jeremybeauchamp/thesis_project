from scipy import stats
import numpy as np
import json

nbeats_files = {
    "carbs": "carbs/nbeats_inertial.json",
    "bolus": "bolus/nbeats_inertial.json",
    "combo": "combo/nbeats_inertial.json",
    "carbs_wo_bolus": "carbs_wo_bolus/nbeats_inertial.json",
}

lstm_files = {
    "carbs": "carbs/lstm_inertial.json",
    "bolus": "bolus/lstm_inertial.json",
    "combo": "combo/lstm_inertial.json",
    "carbs_wo_bolus": "carbs_wo_bolus/lstm_inertial.json",
}
baseline_files = {
    "carbs": "carbs/baselines_inertial.json",
    "bolus": "bolus/baselines_inertial.json",
    "combo": "combo/baselines_inertial.json",
    "carbs_wo_bolus": "carbs_wo_bolus/baselines_inertial.json",
}

best = {"carbs": "AVG", "bolus": "AVG", "combo": "BEST", "carbs_wo_bolus": "AVG"}

patient_lists = {
    "carbs": ["540", "544", "552", "559", "563", "575", "584", "588", "591", "596"],
    "bolus": ["540", "552", "559", "563", "570", "575", "584", "588", "591", "596"],
    "combo": ["540", "544", "552", "559", "563", "575", "584", "588", "591"],
    "carbs_wo_bolus": ["559", "575", "588", "591"],
}

p_values = {}

for s in ["carbs", "bolus", "combo", "carbs_wo_bolus"]:
    p_values[s] = {}
    fd1 = open(nbeats_files[s], "r")
    fd2 = open(lstm_files[s], "r")
    fd3 = open(baseline_files[s], "r")

    nbeats = json.load(fd1)
    lstm = json.load(fd2)
    baselines = json.load(fd3)

    fd1.close()
    fd2.close()
    fd3.close()

    nbeats_rmse = []
    nbeats_mae = []

    lstm_rmse = []
    lstm_mae = []

    global_rmse = []
    global_mae = []

    time_rmse = []
    time_mae = []

    for p in patient_lists[s]:
        nbeats_rmse.append(nbeats["by_patient"][best[s]][p]["RMSE"])
        nbeats_mae.append(nbeats["by_patient"][best[s]][p]["MAE"])

        lstm_rmse.append(lstm["by_patient"][best[s]][p]["RMSE"])
        lstm_mae.append(lstm["by_patient"][best[s]][p]["MAE"])

        global_rmse.append(baselines["by_patient"]["GLOBAL"][p]["RMSE"])
        global_mae.append(baselines["by_patient"]["GLOBAL"][p]["MAE"])

        time_rmse.append(baselines["by_patient"]["TIME"][p]["RMSE"])
        time_mae.append(baselines["by_patient"]["TIME"][p]["MAE"])

    nbeats_rmse = np.array(nbeats_rmse)
    nbeats_mae = np.array(nbeats_mae)

    lstm_rmse = np.array(lstm_rmse)
    lstm_mae = np.array(lstm_mae)

    global_rmse = np.array(global_rmse)
    global_mae = np.array(global_mae)

    time_rmse = np.array(time_rmse)
    time_mae = np.array(time_mae)

    nbeats_lstm_p_rmse = stats.ttest_rel(
        nbeats_rmse, lstm_rmse, alternative="less"
    ).pvalue
    nbeats_global_p_rmse = stats.ttest_rel(
        nbeats_rmse, global_rmse, alternative="less"
    ).pvalue
    nbeats_time_p_rmse = stats.ttest_rel(
        nbeats_rmse, time_rmse, alternative="less"
    ).pvalue

    nbeats_lstm_p_mae = stats.ttest_rel(nbeats_mae, lstm_mae, alternative="less").pvalue
    nbeats_global_p_mae = stats.ttest_rel(
        nbeats_mae, global_mae, alternative="less"
    ).pvalue
    nbeats_time_p_mae = stats.ttest_rel(nbeats_mae, time_mae, alternative="less").pvalue

    p_values[s]["nbeats_lstm"] = {"RMSE": nbeats_lstm_p_rmse, "MAE": nbeats_lstm_p_mae}
    p_values[s]["nbeats_global"] = {
        "RMSE": nbeats_global_p_rmse,
        "MAE": nbeats_global_p_mae,
    }
    p_values[s]["nbeats_time"] = {"RMSE": nbeats_time_p_rmse, "MAE": nbeats_time_p_mae}

fd = open("p_values.json", "w")
json.dump(p_values, fd, indent=4)
