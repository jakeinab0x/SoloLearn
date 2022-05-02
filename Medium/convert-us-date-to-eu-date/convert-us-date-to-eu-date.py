import datetime
date = input()
date_digits = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}

def get_eu_date(date):
    if "/" in date:
        date = date.split("/")
        date[0], date[1] = date[1], date[0]
        date = [int(i) for i in date]
        date = date[::-1]
        return date
    else:
        date = date.replace(",", "")
        date = date.split(" ")
        monthdigit = date_digits.get(date[0])
        date[0] = str(monthdigit)
        date[0], date[1] = date[1], date[0]
        date = [int(i) for i in date]
        date = date[::-1]
        return date

date = get_eu_date(date)

x = datetime.datetime(date[0],date[1],date[2])

day_name = x.strftime("%A")

print(day_name)