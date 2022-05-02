import re, math

string = input()

words = float(len(re.sub('\W+',' ',string).split()))

letters = float(len(re.sub('\W+','',string)))

print(math.ceil(letters/words))