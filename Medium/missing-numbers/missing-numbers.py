length = int(input())
nums = []
i = 1
while i <= length:
    nums.append(int(input()))
    i += 1

numbers = [i for i in range(nums[0], nums[-1]+1)]

missing = []

for i in numbers:
    if i not in nums:
        missing.append(i)

for i in missing:
    print(i, end=' ')