import math
h = int(input())
w = int(input())

door = (h*w)*2
roll = (60*(1/6)) * 2

print(math.ceil(door/roll)*2)