import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n, m = g()
a = [input() for i in range(n)]
x, y = 0, 0
ans = ""
for i in range(1, n + m - 1):
    if i % 2:
        ans += "RL"
        while x < n - 1 and y > 0:
            ans += "D"
            x += 1
            if x < n - 1:
                ans += "L"
                y -= 1
        if x < n - 1:
            ans += "D"
            x += 1
        if (x + y) % 2 != i % 2:
            ans += "R"
            y += 1
    else:
        ans += "DU"
        while x > 0 and y < m - 1:
            ans += "R"
            y += 1
            if y < m - 1:
                ans += "U"
                x -= 1
        if y < m - 1:
            ans += "R"
            y += 1
        if (x + y) % 2 != i % 2:
            ans += "D"
            x += 1
print(ans)
