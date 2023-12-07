import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, K = g()
S = input()

if (N - K + 1) & 1:
    ans = S[K-1:] + S[:K-1][::-1]
else:
    ans = S[K-1:] + S[:K-1]
print(ans)