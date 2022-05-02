reg_time = input()

if "AM" in reg_time:
    x = reg_time.replace(" AM", "")
    print(x)
if "PM" in reg_time:
    y = reg_time.replace(" PM", "")
    z = y.split(":")
    a = [int(z[0])]
    a[0] += 12
    print(f'{a[0]}:{z[1]}')