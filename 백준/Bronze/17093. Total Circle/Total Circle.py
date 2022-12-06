N, M = map(int, input().split())
P = [[*map(int, input().split())] for _ in range(N)]
Q = [[*map(int, input().split())] for _ in range(N)]
print(max(max((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2 for j in P) for i in Q))