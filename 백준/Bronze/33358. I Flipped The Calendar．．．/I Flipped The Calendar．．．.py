import calendar
import datetime

y = int(input())
day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
    day[1] = 29
ans, weekday = 0, calendar.weekday(y, 1, 1)
for d in day:
    q, weekday = divmod(d + weekday, 7)
    ans += q + (weekday != 0)
print(ans)