from collections import Counter
g = lambda: [*map(int, input().split())]

n, m = g()
A = [g() for _ in range(n)]
ans = 0
for i in range(n + 1 >> 1):
    for j in range(m + 1 >> 1):
        cells = [A[i][j]]
        if n - i - 1 != i:
            cells.append(A[n - i - 1][j])
        if m - j - 1 != j:
            cells.append(A[i][m - j - 1])
        if n - i - 1 != i and m - j - 1 != j:
            cells.append(A[n - i - 1][m - j - 1])
        ans += len(cells) - Counter(cells).most_common(1)[0][1]
print(ans)