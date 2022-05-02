import re
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

backwards = alphabet[::-1]

phrase = input()

#make list of individual chars within phrase
for i in phrase.split(', '):
    chars = []
    for j in i:
        chars.append(j.lower())

#make list of index numbers of each char
indexes = []
for i in chars:
    if i == ' ':
        indexes.append(len(alphabet) + 1)
    else:
        indexes.append(alphabet.index(i))

#print index of backwards alphabet list
for i in indexes:
    if i == 27:
        print(' ', end='')
    else:
        print(backwards[i], end='')