H, W = map(int, input().split())
s = [input() for _ in range(H)]

def solve(i, j):
    if s[i][j].isdigit():
        return int(s[i][j])
    r = i + 1
    c1 = j - 1
    while c1 and s[r][c1] == '.':
        c1 -= 1
    c2 = j + 1
    while c2 < W and s[r][c2] == '.':
        c2 += 1
    left, right = solve(r, c1), solve(r, c2)
    if s[i][j] == '*':
        return left * right
    if s[i][j] == '+':
        return left + right
    return left - right
j = 0
while j < W and s[0][j] == '.':
    j += 1
print(solve(0, j))