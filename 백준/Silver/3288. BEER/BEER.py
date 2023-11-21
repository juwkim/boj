dic = {'U': 0, 'L': 1, 'D': 2, 'R': 3}
N = int(input())
buf = [[]] + [[0] + list(map(dic.get, input())) + [0] for _ in range(N)][::-1]

for i in range(1, N + 1):
    for j in range(1, len(buf[i]) - 1):
        if i != N:
            buf[i+1][j-1] = (buf[i+1][j-1] + buf[i][j]) % 4
            buf[i+1][j] = (buf[i+1][j] + buf[i][j]) % 4
        for _ in range(buf[i][j]):
            print(i, j)