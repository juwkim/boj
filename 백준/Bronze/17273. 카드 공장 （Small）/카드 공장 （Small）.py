g = lambda: map(int, input().split())
N, M = g()
card = [[*g()] for _ in range(N)]
now = [0] * N
for _ in range(M):
    K = int(input())
    for i in range(N):
        if card[i][now[i]] <= K:
            now[i] = 1 - now[i]
print(sum(card[i][now[i]] for i in range(N)))