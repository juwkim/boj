import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

l, w, n = g()

if l * w % n:
    print("impossible")
else:
    d = l * w // n
    p, q = None, None
    for i in range(1, d + 1):
        if d % i:
            continue
        j = d // i
        if l % i == 0 and w % j == 0:
            p, q = i, j
            break
    if p == None:
        print("impossible")
    else:
        buf = [[' '] * w for _ in range(l)]
        cur = ord('A')
        for i in range(0, l, p):
            for j in range(0, w, q):
                for s in range(i, i + p):
                    for t in range(j, j + q):
                        buf[s][t] = chr(cur)
                cur += 1
        for l in buf:
            print(''.join(l))