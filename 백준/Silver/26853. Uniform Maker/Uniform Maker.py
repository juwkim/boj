from collections import Counter

N, M = map(int, input().split())
ans = N * M - sum(Counter(l).most_common(1)[0][1] for l in zip(*[input() for _ in range(N)]))
print(ans)