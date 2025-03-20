import sys
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
d = {}
for _ in range(n):
    s = input()
    d[s[:k+1]] = s
print(len(d))
print(*d.values(), sep='\n')