from datetime import date

x = input()
y = input()

def worddate_to_numdate(date):
    date_digits = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}
    date = date.replace(",", "")
    date = date.split(" ")
    monthdigit = date_digits.get(date[0])
    date[0] = str(monthdigit)
    date[0], date[1] = date[1], date[0]
    date = [int(i) for i in date]
    date = date[::-1]
    return date

def get_days_between(x, y):
    x = worddate_to_numdate(x)
    y = worddate_to_numdate(y)
    d0 = date(x[0], x[1], x[2])
    d1 = date(y[0], y[1], y[2])
    delta = d1 - d0
    return delta.days
    
print(get_days_between(x, y))