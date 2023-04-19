from math import isqrt

ans, cnt = 0, 0
for i in range(1, 1 + int(input())):
    num = 0
    for j in range(1, 1 + isqrt(i)):
        q, r = divmod(i, j)
        if r:
            continue
        if j == q:
            num += 1
        else:
            num += 2
    if num > cnt:
        cnt = num
        ans = i
print(ans)
print(cnt)