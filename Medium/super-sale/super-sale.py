items = sorted(list(map(float, input().split(","))))
taxed = [i * 1.07 for i in items]
discounted = [i *.3 for i in taxed[:-1]]
savings = int(sum(discounted)//1)

print(savings)