num = int(input())

sum = 0
i = 1
while i < num:
    if i % 3 and i % 5 == 0:
        sum += i
        i += 1
        continue
    elif i % 3 == 0 or i % 5 == 0:
        sum += i
        i += 1
    else:
        i += 1
        
print(sum)