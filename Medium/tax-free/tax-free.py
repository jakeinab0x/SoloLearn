prices = [int(i) for i in input().split(',')]
total = round(sum([price * 1.07 for price in prices if price < 20.00]), 2) + round(sum([price for price in prices if price >= 20.00]))
print(total) 