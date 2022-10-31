import pickle as pkl

for d in ["carbs", "bolus", "combo"]:
    # for d in ['carbs']:
    fd = open("num_examples_" + d + ".txt", "w")
    for c in ["1", "3"]:
        fd.write("CASE: " + c + "\n")
        for s in ["training", "validation", "testing"]:
            fd.write(s + "\n")
            fd2 = open(d + "_data.pkl", "rb")
            data = pkl.load(fd2)
            fd2.close()
            for p in [
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
            ]:
                fd.write(p + ": " + str(len(data[0][s][1][p][c])) + "\n")

fd.close()
