Board = ('WB' * 4 + 'BW' * 4) * 4
ans = 9999
N, M = map(int, input().split())
S = [input() for _ in range(N)]

for i in range(N - 7):
    for j in range(M - 7):
        t = ''.join([line[j:j+8] for line in S[i:i+8]])
        p = sum(x != y for x, y in zip(Board, t))
        ans = min(ans, p, 64 - p)
print(ans)