g = lambda: [*map(int, input().split())]

N = int(input())
Map = [g() for _ in range(N)]
check = [[0] * N for _ in range(N)]
Not_find = True
def solve(i, j):
    global Not_find
    if Not_find:
        if i == N - 1 and j == N - 1:
            Not_find = False
            return
        if i >= N or j >= N:
            return
        if check[i][j] == 0 and Map[i][j]:
            check[i][j] = 1
            solve(i + Map[i][j], j)
            solve(i, j + Map[i][j])

solve(0, 0)
print("Hing" if Not_find else "HaruHaru")