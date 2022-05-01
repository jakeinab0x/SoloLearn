order = input().split()
sum = 0

for i in order:
    if "Pizza" == i:
        sum+=6.0
    elif "Nachos" == i:
        sum+=6.0
    elif "Cheeseburger" == i:
        sum+=10.0
    elif "Water" == i:
        sum+=4.0
    elif "Coke" == i:
        sum+=5.0      
    else:
        sum+=5.0

res = round(sum*1.07, 2)
print(f'{res:.2f}')