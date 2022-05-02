num = int(input())

d = {}
for num in range(1, num+1):
    d[f"name{num}"] = input().split() 

names = []
for key in d:
    names.append(d.get(key))

for name in names:
    print(name[0][0]+name[1][0], end=' ')