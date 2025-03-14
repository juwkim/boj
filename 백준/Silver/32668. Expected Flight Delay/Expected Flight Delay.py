day, *l = map(int, input().split())
pwday, pwend, pimp = map(lambda x: x / 100, l)
day -= 1
cur, i = 0, 0
while cur < pimp:
    i += 1
    cur += (pwend, pwday)[0 < (day - i) % 7 < 6] * (1 - cur)
day_name = "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
print(f"Try to leave on {day_name[(day - i) % 7]}, {i} day{('s', '')[i == 1]} before the {day_name[day]} meeting.")