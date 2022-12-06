N, M = map(int, input().split())
cost = [int(input()) for _ in [0]*N]
criteria = [int(input()) for _ in [0]*M]
vote = [0] * N
for criterion in criteria:
    i = 0
    while criterion < cost[i]:
        i += 1
    vote[i] += 1
print(1 + vote.index(max(vote)))