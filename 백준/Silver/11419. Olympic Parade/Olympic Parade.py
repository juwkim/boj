g = lambda: [*map(int, input().split())]

from collections import Counter
N, K = g()
for key, val in Counter(int(input()) for _ in range(N)).items():
    if val % K:
        print(key)
        break