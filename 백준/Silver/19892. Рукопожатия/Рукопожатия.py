n, *h = map(int, open(0).read().split())
ans, Max, cnt = 0, 0, sum(num > 0 for num in h)
for num in h:
    Max = max(Max, num)
    cnt -= num != 0
    ans = max(ans, Max + cnt)
print(ans)