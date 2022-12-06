max_num, now = 0, 0
for _ in range(4):
    a, b = map(int, input().split())
    now += b - a
    if now > max_num:
        max_num = now
print(max_num)