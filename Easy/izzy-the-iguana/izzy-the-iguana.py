snacks = input().split()
points = 0

for i in snacks:
    if i == 'Lettuce':
        points += 5
    elif i == 'Carrot':
        points += 4
    elif i == 'Mango':
        points += 9
    elif i == 'Cheeseburger':
        points += 0

if points >= 10:
    print('Come on Down!')
else:
    print('Time to wait')