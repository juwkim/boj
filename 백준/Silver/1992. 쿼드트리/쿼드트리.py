def solve(N, x, y):
    if N == 1:
        return text[x][y]
    N //= 2
    lt = solve(N, x, y)
    rt = solve(N, x, y+N)
    lb = solve(N, x+N, y)
    rb = solve(N, x+N, y+N)
    res = [lt, rt, lb, rb]
    if all(ans == '0' for ans in res):
        return '0'
    elif all(ans == '1' for ans in res):
        return '1'
    else:
        return '(' + "".join(res) + ")"

N = int(input())
text = [input() for _ in range(N)]
print(solve(N, 0, 0))