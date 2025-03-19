from collections import Counter

N, K = map(int, input().split())
ans = 0
for _ in range(N): ans += sum(v - 1 for v in Counter(input().split()).values() if v > 1)
print(ans)