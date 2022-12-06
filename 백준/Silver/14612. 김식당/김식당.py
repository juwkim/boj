g = lambda: [*map(int, input().split())]
N, M = g()
buf = []
for i in range(N):
    s = input()
    if s[0] == 'o':
        _, n, t = s.split()
        buf.append((int(t), int(n)))
    elif s[0] == 's':
        buf.sort()
    else:
        _, n = s.split()
        n = int(n)
        for j in range(len(buf)):
            if buf[j][1] == n:
                del buf[j]
                break
    if buf:
        print(*[*zip(*buf)][1])
    else:
        print('sleep') 