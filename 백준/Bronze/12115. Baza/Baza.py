import sys
I = sys.stdin.readline
N, M = map(int, I().split())
s = [*zip(*[[*map(int, I().split())] for _ in range(N)])]
for _ in range(int(I())):
    k = {i:0 for i in range(N)}
    count = 0
    for i, num in enumerate(map(int, I().split())):
        if num != -1:
            count += 1
            for j in range(N):
                k[j] += (s[i][j] == num)
    print(sum(i >= count for i in k.values()))