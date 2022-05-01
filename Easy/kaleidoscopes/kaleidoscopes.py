prc = 5
qty = int(input())
dsc = prc * 0.1
tax = 1.07

def calcTotal(qty):
    if qty == 1:
        return round(prc * tax, 2)
    else:
        return round(((qty * (prc - dsc)) * tax), 2)
        
print(calcTotal(qty))