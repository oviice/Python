import time, datetime as t, calendar

# returns the formatted time

print(time.asctime(time.localtime(time.time())))
print(t.datetime.now())
cal = calendar.month(2020, 11)
print(cal)

cal=calendar.prcal(2020)
print (cal)