N = int(input())
ans, cnt, prv, d = 0, 0, 0, 0
for p in map(int, input().split()):
    if p == prv:
        continue
    if d == 0 and p > prv or d == 1 and p < prv:
        cnt += 1
    else:
        d ^= 1
        cnt = 2
    ans = max(ans, cnt)
    prv = p
print(ans)