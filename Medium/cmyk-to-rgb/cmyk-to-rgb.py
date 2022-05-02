c = float(input())
m = float(input())
y = float(input())
k = float(input())

r = round(255 * (1-c) * (1-k))
g = round(255 * (1-m) * (1-k))
b = round(255 * (1-y) * (1-k))
print(f"{r},{g},{b}")