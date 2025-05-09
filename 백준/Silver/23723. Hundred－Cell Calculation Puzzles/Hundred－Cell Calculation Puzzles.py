import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

def solve(w, h, constraints):
    col = [1e9] * (w + 1)
    row = [1e9] * (h + 1)
    col[1] = 0

    for x, y, val in constraints:
        if col[x] != 1e9 and row[y] != 1e9:
            if col[x] + row[y] != val:
                return "NO"
        elif col[x] != 1e9:
            row[y] = val - col[x]
        elif row[y] != 1e9:
            col[x] = val - row[y]

    changed = True
    while changed:
        changed = False
        for x, y, val in constraints:
            if col[x] != 1e9 and row[y] == 1e9:
                row[y] = val - col[x]
                changed = True
            elif row[y] != 1e9 and col[x] == 1e9:
                col[x] = val - row[y]
                changed = True
            elif col[x] != 1e9 and row[y] != 1e9:
                if col[x] + row[y] != val:
                    return "NO"

    known = 0
    for i in range(2, w + 1):
        if col[i] != 1e9:
            known += 1
    for i in range(1, h + 1):
        if row[i] != 1e9:
            known += 1

    if known == w + h - 1:
        return "YES"
    else:
        return "NO"

while (l:=g())[0]:
    w, h = l
    k = w + h - 1
    constraints = [g() for _ in range(k)]
    print(solve(w, h, constraints))