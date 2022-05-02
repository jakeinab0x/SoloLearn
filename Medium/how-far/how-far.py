letters = input()

positionH = letters.index("H")
positionP = letters.index("P")
way = abs(positionP - positionH ) - 1

print(way)