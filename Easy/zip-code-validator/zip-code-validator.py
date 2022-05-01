x = input()

def is_zip(x):
    if x.isalpha() or len(x) != 5:
        print('false')
    else:
        print('true')

is_zip(x)