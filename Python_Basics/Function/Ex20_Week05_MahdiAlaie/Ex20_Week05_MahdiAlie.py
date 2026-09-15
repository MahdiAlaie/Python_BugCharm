machines = {
    "M01":38,
    "M02":52,
    "M03":34,
    "M04":55,
    "M05":43
}

def contorller (dict):
    HighTemp=[]
    for m ,t in dict.items():
        if t >= 40:
            HighTemp.append(m)
    return HighTemp
MachineTempControll= contorller(machines)
print(MachineTempControll)