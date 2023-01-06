from day_2 import minutes_to_midnight
import datetime as dt


today = dt.datetime.now()

d = '2018-01-01 00:00:00'
d = dt.datetime(today.year, today.month, today.day, 23, 22, 31)
assert minutes_to_midnight(d) == "38 minutes"

d = dt.datetime(today.year, today.month, today.day, 12, 15, 29)
assert minutes_to_midnight(d) == "705 minutes"
