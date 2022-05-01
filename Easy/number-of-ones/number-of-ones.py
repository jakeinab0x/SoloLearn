temp = format(int(input()), "b") 
zeros = []

for i in str(temp):
    if i == '1':
        zeros.append(i)

print(len(zeros))