input()
ans, cnt, freeze = 0, 0, -2
for day, num in enumerate(map(int, input().split())):
    if num:
        cnt += 1
    elif day - freeze >= 2:
        freeze = day
    else:
        ans = max(ans, cnt)
        cnt = 0
ans = max(ans, cnt)
print(ans)