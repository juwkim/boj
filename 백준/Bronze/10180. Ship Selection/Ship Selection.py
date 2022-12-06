for _ in range(int(input())):
    N, D = map(int, input().split())
    starfleets = [list(map(int, input().split())) for _ in range(N)]
    total = sum([i[0]*i[1]/i[2] >= D for i in starfleets])
    print(total)