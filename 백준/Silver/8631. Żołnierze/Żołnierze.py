from collections import Counter

n = int(input())
cnt = Counter(map(int, input().split()))
ans, big = 1, False
for v in cnt.values():
    for i in range(2, v + 1):
        ans *= i
        if ans >= 10000:
            ans %= 10000
            big = True
if len(cnt) > 1:
    ans *= 2
    if ans >= 10000:
        ans %= 10000
        big = True
if big:
    print("%04d" % ans)
else:
    print(ans)