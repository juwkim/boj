from itertools import chain

N, M = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(N)]

for _ in range(int(input())):
    Q, a, b = input().split()
    a, b = map(int, [a, b])
    if Q == 'row':
        for i in range(M):
            matrix[a-1][i] += b
    else:
        for i in range(N):
            matrix[i][a-1] += b
s = [*chain(*matrix)]
print(sum(s), min(s), max(s))