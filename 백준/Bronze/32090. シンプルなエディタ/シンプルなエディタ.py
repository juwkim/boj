import sys
input = lambda: sys.stdin.readline().rstrip()

while n:=int(input()):
    l, cur = [], 0
    for _ in range(n):
        cmd, c = input().split()
        if cmd[0] == 'I':
            l.insert(cur, c)
            cur += 1
        elif cmd[0] == 'L':
            cur = max(0, cur - 1)
        elif cmd[0] == 'R':
            cur = min(len(l), cur + 1)
    print(*l, sep='')