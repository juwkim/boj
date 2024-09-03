n = int(input())
day_name, isleap = input().split()
cur = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}[day_name]
days = 31, 28 + (isleap == 'yes'), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
month_name = 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'
ans = {}
for day, month in zip(days, month_name):
    for i in range(1, day + 1):
        day_name = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")[cur]
        s = f"first {day_name} of {month}"
        if s not in ans:
            ans[s] = i
        ans[f"last {day_name} of {month}"] = i
        cur = (cur + 1) % 7
for _ in range(n):
    print(ans[input()])