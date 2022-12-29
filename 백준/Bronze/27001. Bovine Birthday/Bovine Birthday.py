import calendar
year, month, day = map(int, input().split())
day_of_week = calendar.weekday(year, month, day)
print(calendar.day_name[day_of_week].lower())