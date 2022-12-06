for _ in range(int(input())):
    N = int(input())
    Map = [input() for _ in range(N)]
    ans = 0
    for s in range(N, 0, -1):
        if any(all(Map[k][j:j+s] == '.' * s for k in range(i, i+s)) for i in range(N-s+1) for j in range(N-s+1)):
            ans = s
            break
    print(ans)