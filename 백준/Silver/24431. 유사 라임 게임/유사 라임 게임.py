def g(): return [*map(int, input().split())]

from collections import Counter
for _ in range(int(input())):
    n, L, F = g()
    cnt = Counter(word[-F:] for word in input().split())
    ans = sum(val // 2 for val in cnt.values())
    print(ans)