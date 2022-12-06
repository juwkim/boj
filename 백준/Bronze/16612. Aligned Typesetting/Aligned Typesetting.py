import sys
input = lambda: sys.stdin.readline().rstrip('\n')
g = lambda: [*map(int, input().split())]

n, L = g()
for _ in range(n):
    L -= len(input())
if n == 1:
    print('No' if L else 'Yes')
else:
    print('No' if L < n-1 or L % (n-1) else 'Yes')