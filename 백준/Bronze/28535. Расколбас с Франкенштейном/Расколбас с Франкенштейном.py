import sys
input = lambda: sys.stdin.readline().rstrip()

ch = "NZQR"
a, op, b = input().split()
if a == 'N' and b == 'N' and op == '-':
    print('Z')
else:
    idx = max(ch.index(a), ch.index(b))
    print(ch[idx])