import sys
input = lambda: sys.stdin.readline().rstrip()

a, b = 0, 0
for _ in range(int(input())):
    q, c, n = input().split()
    if c == '(':
        a += int(n)
    else:
        b += int(n)
    if a == b:
        print('Yes')
    else:
        print('No')