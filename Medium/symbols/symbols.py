import re

str = input()

decoded = re.findall(r"[A-Za-z]|\s|[0-9]", str)

for i in decoded:
    print(i, end="")