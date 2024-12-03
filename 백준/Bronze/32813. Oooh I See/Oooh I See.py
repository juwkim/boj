import sys
input = lambda: sys.stdin.readline().rstrip()

r, c = map(int, input().split())
a = [input() for _ in range(r)]
def solve():
    p, q = None, None
    cnt = 0
    for i in range(1, r - 1):
        for j in range(1, c - 1):
            if a[i][j] == '0' and all((s, t) == (i, j) or a[s][t] == 'O' for s in range(i - 1, i + 2) for t in range(j - 1, j + 2)):
                cnt += 1
                if p is None:
                    p, q = i + 1, j + 1
    if cnt == 0:
        return "Oh no!"
    if cnt == 1:
        return f"{p} {q}"
    return f"Oh no! {cnt} locations"
print(solve())