T = int(input())
for _ in range(T):
    N, D = map(int, input().split())
    sh = [list(map(int, input().split())) for _ in range(N)]
    shuttle = [sh[i][0] * sh[i][1] / sh[i][2] >= D for i in range(N)]
    print(shuttle.count(True))