a = input()

def to_snake_case(a):
    for i in a:
        if i == a[0] and i == i.upper():
            a = a.replace(i, i.lower())
        elif i == i.upper():
            a = a.replace(i, '_'+i.lower())
    return a

print(to_snake_case(a))