from itertools import combinations
K, N = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(K)]
print(sum(sum(line.index(i) > line.index(j) for line in board) % K == 0 for i, j in combinations(range(1, N+1), 2)))