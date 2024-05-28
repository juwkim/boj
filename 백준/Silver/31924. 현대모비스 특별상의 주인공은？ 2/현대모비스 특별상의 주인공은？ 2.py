from itertools import product

N = int(input())
A = [input() for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(N):
        for dx, dy in product(range(-1, 2), repeat=2):
            nx, ny = i + 4 * dx, j + 4 * dy
            if 0 <= nx < N and 0 <= ny < N and all(A[i + k * dx][j + k * dy] == "MOBIS"[k] for k in range(5)):
                ans += 1
print(ans)