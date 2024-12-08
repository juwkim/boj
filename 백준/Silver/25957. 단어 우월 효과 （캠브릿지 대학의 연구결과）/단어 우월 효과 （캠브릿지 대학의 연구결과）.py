import sys
input = lambda: sys.stdin.readline().rstrip()

d = {}
for _ in range(int(input())):
    s = input()
    if len(s) <= 3:
        d[s] = s
    else:
        d[s[0] + ''.join(sorted(s[1:-1])) + s[-1]] = s
input()
for s in input().split():
    if len(s) <= 3:
        print(s, end=' ')
    else:
        print(d[s[0] + ''.join(sorted(s[1:-1])) + s[-1]], end=' ')