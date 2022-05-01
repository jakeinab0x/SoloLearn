word = input()

x = []
for i in word:
    x.append(word.count(i))

def is_isogram(x):
    for i in x:
        if i == 1:
            continue
        elif i > 1:
            return 'false'
    return 'true'
    
print(is_isogram(x))