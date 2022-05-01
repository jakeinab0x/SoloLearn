a = input().split(',')
b = input().split(',')

a[0] = int(a[0])
a[1] = int(a[1])

def make_int(x, i):
    x[i] = int(x[i])
    
make_int(a, 0)
make_int(a, 1)
make_int(b, 0)
make_int(b, 1)

def larger_area(a, b):
    if a[0]*a[1] > b[0]*b[1]:
        print("Apartment A")
    else:
        print("Apartment B")

larger_area(a, b)