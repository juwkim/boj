g = lambda: [*map(int, input().split())]
while sum(l:= g()):
    player = [0] * 10001
    N, M = l
    for _ in range(N):
        for num in g():
            player[num] += 1
    num = sorted(player)[-2]
    ans = [i for i in range(1, 10000) if player[i] == num]
    print(*ans)