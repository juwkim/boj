g = lambda: [*map(int, input().split())]
from collections import Counter
input()
print(max(Counter(a - b for a, b in zip(g(), g())).values()))