import sys
input = lambda: sys.stdin.readline().rstrip()


g = lambda: [*map(int, input().split())]



chain = g()
back = g()

buf = []
for i in range(3):
    for j in range(7):
        ratio = round(chain[i] / back[j], 2)
        buf.append([ratio, i+1, j+1])
buf.sort()
for r, a, b in buf:
    print(f'{r:.2f} {a} {b}')