# add words of string to array
words = input().split()

# move first letter of word to another array (go over there = g o t)
first_chars = []
for word in words:
    first_chars.append(list(word).pop(0))

# remove first letter of word in words (go over there = o ver here)
no_first_letter = []
for word in words:
    no_first_letter.append(word[1:])

# join each element in array of first characters to end of each element in array of words with no first characters  (o ver here + g o t = og vero heret)

new_words = [''.join(i for i in j) for j in zip(no_first_letter, first_chars)]

# add 'ay' to each element in the new_words array created and print on the same line

for i in new_words:
    print(i + 'ay', end=' ')     