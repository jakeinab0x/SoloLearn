sentence = input()
vowels = 'AEIOUaeiou'
num_vowels = 0
for i in sentence:
    if i in vowels:
        num_vowels += 1
    else:
        continue
print(num_vowels)