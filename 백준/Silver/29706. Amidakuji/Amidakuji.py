g = lambda: [*map(int, input().split())]

def solve(line, i):
    for j in range(i, m):
        if line == x[j]:
            line += 1
        elif line == x[j] + 1:
            line -= 1
    return line == q

while True:
    n, m, p, q = g()
    if n == 0:
        break
    x = g()
    ans = "NG"
    if solve(p, 0):
        ans = "OK"
    else:
        line = p
        for i in range(m + 1):
            if line < n and solve(line + 1, i):
                ans = f"{line} {i}"
                break
            elif line > 1 and solve(line - 1, i):
                ans = f"{line - 1} {i}"
                break
            if i == m:
                break
            if line == x[i]:
                line += 1
            elif line == x[i] + 1:
                line -= 1
    print(ans)