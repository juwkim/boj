dic = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}
N = int(input())
Map = [[0] * (N + 1)] + [[0] + input().split() for _ in range(N)][::-1]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        Map[i][j] = max(Map[i-1][j], Map[i][j-1]) + dic[Map[i][j][0]]
print(Map[-1][-1])