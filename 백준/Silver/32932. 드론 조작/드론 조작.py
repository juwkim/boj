import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: map(int, input().split())

N, K = g()
P = {tuple(g()) for _ in range(N)}
x, y = 0, 0
for c in input():
    match c:
        case 'U':
            if (x, y + 1) not in P:
                y += 1
        case 'D':
            if (x, y - 1) not in P:
                y -= 1
        case 'R':
            if (x + 1, y) not in P:
                x += 1
        case 'L':
            if (x - 1, y) not in P:
                x -= 1
print(x, y)