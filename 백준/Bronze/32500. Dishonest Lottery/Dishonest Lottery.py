from collections import Counter

n = int(input())
cnt = sum([Counter(map(int, input().split())) for _ in range(10 * n)], Counter())
ans = [k for k, v in cnt.items() if v > 2 * n]
if ans:
    print(*sorted(ans))
else:
    print(-1)