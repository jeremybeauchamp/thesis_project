from load import *

patients = [
    "540",
    "544",
    "552",
    "559",
    "563",
    "567",
    "570",
    "575",
    "584",
    "588",
    "591",
    "596",
]
# patients = ['559', '563', '570', '575', '588', '591']

training_files = [
    "/home/jeremy/EventPrediction/data/data/training/" + pID + "-ws-training-new.xml"
    for pID in patients
]
testing_files = [
    "/home/jeremy/EventPrediction/data/data/testing/" + pID + "-ws-testing.xml"
    for pID in patients
]
validation_files = [
    "/home/jeremy/EventPrediction/data/data/validation/" + pID + "-ws-validation.xml"
    for pID in patients
]
files = {
    "training": training_files,
    "testing": testing_files,
    "validation": validation_files,
}

combined = False

meal_stats = calculate_stats(
    patients,
    files,
    event_type="meal",
    time_res=5,
    meal_bolus_distance=10,
    use_bolus_carbs=True,
    combined=combined,
    save=True,
)

bolus_stats = calculate_stats(
    patients,
    files,
    event_type="bolus",
    time_res=5,
    meal_bolus_distance=10,
    use_bolus_carbs=True,
    combined=combined,
    save=True,
)

for t in [30, 45, 60, 75, 90]:
    carbs_data, _ = load_carbs_data(
        patients,
        files,
        stats_file="stats_meal.pkl",
        approach=2,
        times=[t],
        meal_bolus_distance=10,
        time_res=5,
        pred_horizon=60,
        use_bolus_carbs=True,
        combined=combined,
        max_time=90,
    )

    bolus_data, _ = load_bolus_data(
        patients,
        files,
        stats_file="stats_bolus.pkl",
        approach=2,
        times=[t],
        meal_bolus_distance=10,
        time_res=5,
        pred_horizon=60,
        use_bolus_carbs=True,
        combined=combined,
        max_time=90,
    )

    combo_data, _ = load_combo_data(
        patients,
        files,
        stats_file="stats_bolus.pkl",
        approach=2,
        times=[t],
        meal_bolus_distance=10,
        time_res=5,
        pred_horizon=60,
        use_bolus_carbs=True,
        combined=combined,
        max_time=90,
    )

    carb_file = "carbs_data" + str(t) + ".pkl"
    bolus_file = "bolus_data" + str(t) + ".pkl"
    combo_file = "combo_data" + str(t) + ".pkl"

    fd = open(carb_file, "wb")
    pickle.dump(carbs_data, fd)
    fd.close()

    fd = open(bolus_file, "wb")
    pickle.dump(bolus_data, fd)
    fd.close()

    fd = open(combo_file, "wb")
    pickle.dump(combo_data, fd)
    fd.close()
