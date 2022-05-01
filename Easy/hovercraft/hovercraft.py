sales = int(input())

costs = 2000000
sell = 3000000
insurance = 1000000

total_costs = costs * 10 + insurance
total_sales = sell * sales

if total_costs < total_sales:
    print("Profit")
elif total_costs > total_sales:
    print("Loss")
elif total_costs == total_sales:
    print("Broke Even")