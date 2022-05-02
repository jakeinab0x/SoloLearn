nums = input().split()
ints = [int(i) for i in nums]
evens = [i for i in ints if i % 2 == 0]
strevens = [str(i) for i in evens]
print(' '.join(strevens))