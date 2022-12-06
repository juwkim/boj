g = lambda: [*map(int, input().split())]

from statistics import Counter
n, k = g()
nums = Counter(g())

buf = [*nums]
if k <= len(buf):
    print(*buf[:k])
else:
    print(*buf, end=' ')
    k -= len(buf)
    for key, val in nums.items():
        cnt = min(k, val - 1)
        print(*[key for _ in range(cnt)], end=' ')
        k -= cnt
        if k == 0:
            break