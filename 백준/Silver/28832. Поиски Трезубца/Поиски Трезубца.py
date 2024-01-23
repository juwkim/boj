import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n, m = g()
a = [input() for i in range(n)]
x, y = 0, 0
ans = []
for i in range(n + m - 1):
    if i & 1:
        ans.append("DU")
        while x > 0 and y < m - 1:
            ans.append("R")
            y += 1
            if y < m - 1:
                ans.append("U")
                x -= 1
        if y < m - 1:
            ans.append("R")
            y += 1
        if (x + y) & 1 == i & 1:
            ans.append("D")
            x += 1
    else:
        ans.append("RL")
        while x < n - 1 and y > 0:
            ans.append("D")
            x += 1
            if x < n - 1:
                ans.append("L")
                y -= 1
        if x < n - 1:
            ans.append("D")
            x += 1
        if (x + y) & 1 == i & 1:
            ans.append("R")
            y += 1
print(*ans, sep="")