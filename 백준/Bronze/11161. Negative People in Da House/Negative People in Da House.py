for _ in range(int(input())):
    M = int(input())
    min_home, now = 0, 0
    for _ in range(M):
        p1, p2 = map(int, input().split())
        now += p1 - p2
        if now < min_home:
            min_home = now
    print(-min_home)