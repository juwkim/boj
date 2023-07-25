from datetime import date, timedelta

d = date(2020, 1, 1)
for _ in range(int(input())):
    nums = [str(i) for i, num in enumerate(input().split()) if num == '1']
    cnt = 0
    for delta in range(366):
        t = d + timedelta(days=delta)
        day = f"{t.month}{t.day}"
        cnt += all(num not in day for num in nums)
    print(cnt)