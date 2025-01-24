def define_persona(performance):
    if float(performance["accuracy"].strip('%')) > 90:
        return "Accuracy Achiever"
    elif float(performance["speed"]) > 100:
        return "Speedster"
    elif performance["score_trend"] == "improving":
        return "Consistent Improver"
    else:
        return "Needs More Practice"
