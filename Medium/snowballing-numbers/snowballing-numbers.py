x = int(input())
y = []

for i in range(x):
    y.append(int(input()))

def snowball(y):
    i = 1
    while i < len(y):
        if y[-i] > sum(y[:-i]):
            i += 1
            return "true"
        else:
            return "false"
    
print(snowball(y))