num = int(input())
nums = input().split()
intnums = [int(i) for i in nums]

def divisible(num, intnums):
    is_divisible = 0
    for i in intnums:
        if num % i == 0:
            is_divisible += 1
    if is_divisible == len(intnums):
        print('divisible by all')
    else:
        print('not divisible by all')
        
divisible(num, intnums)