import re

password = input()
reg = "^(?=.{7,}$)(?=(?:.*?\w){0,})(?=(?:.*?\d){2})(?=(?:.*[!@#$%&*]){2}).*$"
match = re.compile(reg)
search = re.search(match, password)

if search:
    print("Strong")

else:
    print("Weak")