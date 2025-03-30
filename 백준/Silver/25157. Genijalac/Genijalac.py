import sys
input = sys.stdin.readline

N = int(input())
P = [int(input()) for _ in range(N)]
K = int(input())
Z = [[*map(int, input().split())] for _ in range(K)]

def solve(l, score=None, flag=False):
    if score is None: score = [0] * N
    prv, num = -1, N + 1
    for i, p in sorted(enumerate(l), key=lambda x: x[1], reverse=True):
        if flag or p != prv: num -= 1
        score[i] += num
        prv = p
    return score

score1 = solve(P)
score2 = solve([sum(l) for l in zip(*Z)], score1[:])
star_rank = solve(score2, flag=True)
judge = [0] * K
for i in range(K):
    judge_rank = solve(Z[i])
    judge[i] = sum(abs(star_rank[j] - judge_rank[j]) for j in range(N))
print(max(range(N), key=lambda i: P[i]) + 1)
print(min(score1))
print(max(range(N), key=lambda i: score2[i]) + 1)
print(min(range(K), key=lambda i: judge[i]) + 1)