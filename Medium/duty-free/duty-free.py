items = list(input().split(' '))
exchanged = [float(i) * 1.1 for i in items]

def dutyfree(exchanged):
    for i in exchanged:
        if i > 20.00:
            return "Back to the store"
    return "On to the terminal"

print(dutyfree(exchanged))