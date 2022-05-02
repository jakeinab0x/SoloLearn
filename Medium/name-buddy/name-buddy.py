names = input().split()
myname = input()
first_chars = [i[0] for i in names]
if myname[0] in first_chars:
    print('Compare notes')
else:
    print('No such luck')