layout = input()

money = layout.index("$")

guards = [i for i, x in enumerate(layout) if x == "G"]
thieves = [i for i, x in enumerate(layout) if x == "T"]

# get guard distances away from money

guard_dists = []
for guard in guards:
    guard_dists.append(abs(guard - money))

# get thief distances away from money

thief_dists = []
for thief in thieves:
    thief_dists.append(abs(thief - money))

# compare guard and thief distances 

def compare_distances(guard_dists, thief_dists):
    quiets = 0
    alarms = 0
    for i in guard_dists:
        for j in thief_dists:
            if j > i:
                quiets += 1
            else:
                alarms += 1
    if quiets > alarms:
        return "quiet"
    else:
        return "ALARM"

print(compare_distances(guard_dists, thief_dists))