length = int(input())
x = []

while len(x) < length:
    x.append(int(input())) 

y = [i for i in x if i % 2 == 0]

print(sum(y))