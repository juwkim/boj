import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

n, m = g()
k = int(input())
_, _, w = zip(*[g() for _ in range(m)])
print(min(w) * (k - 1))