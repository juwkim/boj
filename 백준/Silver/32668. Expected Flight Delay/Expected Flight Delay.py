day, *l = map(int, input().split())
pwday, pwend, pimp = map(lambda x: x / 100, l)
day -= 1
p = pwend, pwday, pwday, pwday, pwday, pwday, pwend
cur, i = 0, 1
while True:
    cur = p[(day - i) % 7] * (1 - cur) + cur
    if cur > pimp:
        break
    i += 1
day_name = "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
print(f"Try to leave on {day_name[(day - i) % 7]}, {i} day{('s', '')[i == 1]} before the {day_name[day]} meeting.")