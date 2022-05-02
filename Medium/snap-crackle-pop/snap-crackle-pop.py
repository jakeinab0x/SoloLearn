a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

bowls = [a, b, c, d, e, f]

for i in bowls:
    if i % 3 == 0:
        print("Pop", end=" ")
    elif i % 2 == 1:
        print("Snap", end=" ")
    else:
        print("Crackle", end=" ")