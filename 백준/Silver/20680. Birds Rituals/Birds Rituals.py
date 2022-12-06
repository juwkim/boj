import sys
input = lambda: sys.stdin.readline().rstrip()

g = lambda: [*map(int, input().split())]

n, s = g()
buf = input().split()
for _ in range(s):
    cmd, *l = input().split()
    if cmd[0] == 'i':
        buf.insert(int(l[1]), l[0])
    elif cmd[0] == 'r':

        move = int(l[1])
        if move == 0:
            continue
        else:
            idx = buf.index(l[0])
            del buf[idx]
            buf.insert(idx + move, l[0])
    else:
        buf.remove(l[0])

print(*buf)