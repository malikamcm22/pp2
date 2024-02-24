import datetime as dt

a = dt.datetime(2024,2,20,21,59,59)
b = dt.datetime(2024,2,22,23,59,59)

print((b-a).total_seconds())