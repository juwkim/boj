g = lambda: [*map(int, input().split())]

from collections import Counter
n, k = g()
a = Counter(g())
if len(a) >= k:
    num = sum(i[1] for i in a.most_common(k))
    print(n - num)
else:
    print(k - len(a))