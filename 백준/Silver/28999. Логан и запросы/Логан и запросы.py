import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

n, q = g()
A = g()
cnt = [0] * (n + 1)
for _ in range(q):
    l, r = g()
    cnt[l - 1] += 1
    cnt[r] -= 1
for i in range(n - 1):
    cnt[i + 1] += cnt[i]
A.sort(reverse=True)
cnt.sort(reverse=True)
print(sum(a*c for a, c in zip(A, cnt)))