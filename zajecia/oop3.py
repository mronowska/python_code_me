import datetime

today = datetime.date.today()
print(today)
print(type(today))
print(today.day)
print(today.month)
print(today.year)

now = datetime.datetime.now()
print(now)

print(f"Teraz jest {now.hour}:{now.minute}")
utc_now = datetime.datetime.utcnow()
print(f"Teraz jest w UTC {utc_now.hour}:{utc_now.minute}")

my_datetime = datetime.date(2024, 12, 24)
print(my_datetime)

difference = my_datetime - today
print(difference.days)
