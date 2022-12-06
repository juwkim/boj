g = lambda: [*map(int, input().split())]

N = int(input())
Map = [g() for _ in range(N)]
Not_find = True
def solve(i, j):
    global Not_find
    if Not_find:
        if i == N - 1 and j == N - 1:
            Not_find = False
            return
        if i >= N or j >= N:
            return
        if Map[i][j]:
            solve(i + Map[i][j], j)
            solve(i, j + Map[i][j])

solve(0, 0)
print("Hing" if Not_find else "HaruHaru")