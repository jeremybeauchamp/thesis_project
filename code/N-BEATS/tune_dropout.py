from run import run
import json
import argparse


def tune_dropout(
    data_file,
    default_hyper_parameters,
    scenario,
    case,
    patient_list,
    unrestricted=True,
    runs=2,
    combined=False,
    tensorboard=True,
):

    hyper_parameters = default_hyper_parameters

    dropout_rates = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]

    if args.scenario == "combo":
        combo = True
    else:
        combo = False

    results = {}
    for dr in dropout_rates:
        hyper_parameters["dropout"] = dr
        results[str(dr)] = run(
            data_file,
            hyper_parameters,
            patient_list,
            unrestricted=unrestricted,
            combined=combined,
            runs=runs,
            tensorboard=tensorboard,
            combo=combo,
        )

    fd = open("dropout_tuning_results_" + scenario + "_" + case + ".json", "w")
    json.dump(results, fd)
    fd.close()

    return results


def best_parameters_architecture(hyper_parameters, results):
    dropout_rates = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]

    best_rmse = float("inf")
    best_parameters = None
    for dr in dropout_rates:
        rmse = results[str(dr)]["overall"]["AVG"]["RMSE"]
        if rmse < best_rmse:
            best_rmse = rmse
            best_parameters = dr

    best_dr = best_parameters
    hyper_parameters["dropout"] = best_dr

    return hyper_parameters


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", type=str)
    parser.add_argument("--case", type=str)
    args = parser.parse_args()

    filename = args.scenario + "_data.pkl"

    if args.case == "unrestricted":
        unrestricted = True
    else:
        unrestricted = False

    scenario = args.scenario
    if scenario == "carbs":
        patient_list = [
            "540",
            "544",
            "552",
            "559",
            "563",
            "575",
            "584",
            "588",
            "591",
            "596",
        ]
    elif scenario == "combo":
        patient_list = ["540", "544", "552", "559", "563", "575", "584", "588", "591"]
    else:
        patient_list = [
            "540",
            "552",
            "559",
            "563",
            "570",
            "575",
            "584",
            "588",
            "591",
            "596",
        ]

    fd = open("default_hyper_parameters.json", "r")
    default_hyper_parameters = json.load(fd)
    fd.close()

    results = tune_dropout(
        filename,
        default_hyper_parameters,
        args.scenario,
        args.case,
        patient_list,
        unrestricted=unrestricted,
        runs=5,
        combined=False,
        tensorboard=False,
    )

    new_hyper_parameters = best_parameters_architecture(
        default_hyper_parameters, results
    )

    fd = open(
        "tuned_dropout_hyper_parameters_" + args.scenario + "_" + args.case + ".json",
        "w",
    )
    json.dump(new_hyper_parameters, fd, indent=4)
    fd.close()
