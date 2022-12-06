import sys
input = sys.stdin.readline
N, M = map(int, input().split())
array = [[0 for _ in range(M+1)] for _ in range(N+1)]
for i in range(1, N+1):
    temp = [*map(int, input().split())]
    for j in range(1, M):
        temp[j] += temp[j-1]
    for j in range(1, M+1):
        array[i][j] = array[i-1][j] + temp[j-1]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(array[x][y] + array[i-1][j-1] - array[i-1][y] - array[x][j-1])