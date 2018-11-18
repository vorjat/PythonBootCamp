import datetime

# print(datetime.date(1989,4,14).weekday())
d0 = datetime.date(2018, 11, 18)
d1 = datetime.date(1989, 4, 14)
delta = d0 - d1

print(delta.days)
