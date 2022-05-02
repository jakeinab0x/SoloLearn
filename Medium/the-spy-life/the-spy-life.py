import re

str = input()

reverse_str = str[::-1]

decoded = re.findall(r"[A-Za-z]|\s", reverse_str)

for i in decoded:
    print(i, end="")