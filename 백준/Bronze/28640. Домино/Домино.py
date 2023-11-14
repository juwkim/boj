import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

a1, b1 = map(len, input().split('|'))
a2, b2 = map(len, input().split('|'))
if a1 in (a2, b2) or b1 in (a2, b2):
    print('Yes')
else:
    print('No')