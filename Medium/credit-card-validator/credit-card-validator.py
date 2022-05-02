num = input()
num = [int(i) for i in num]
num = num[::-1]

double_second_nums = [i*2 for i in num[1::2]]

i = 1
j = 0
while i < len(num):
    num[i] = double_second_nums[j]
    i += 2
    j += 1

def minus_nine(num):
    for i in num:
        if i > 9:
            num[num.index(i)] = i - 9
    return num
         
num = minus_nine(num)

if sum(num) % 10 == 0 and len(num) == 16:
    print("valid")
else:
    print("not valid")