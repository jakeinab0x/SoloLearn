word = input()
num = int(input())
number = num
word = [i for i in word]

while num < len(word):
    word.insert(num, '-')
    num += number + 1
    
for i in word:
    print(i, end='')