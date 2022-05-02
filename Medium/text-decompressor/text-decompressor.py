text = input()
text = [i * int(text[text.index(i)+1]) for i in text if text.index(i) % 2 == 0]
for i in text:
    print(i, end='')