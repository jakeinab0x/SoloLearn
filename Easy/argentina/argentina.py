peso_price = int(input())
dollar_price = int(input())

def exchangeRate(num):
    return round(num * 0.02)

if exchangeRate(peso_price) < dollar_price:
    print("Pesos")
else:
    print("Dollars")