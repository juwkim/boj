import sys
input = lambda: sys.stdin.readline().rstrip('\n')

g = lambda: [*map(int, input().split())]

left, right = 0, 100001
for _ in range(int(input())):
    s, e = g()
    left = max(left, s)
    right = min(right, e)
print(max(0, left - right))