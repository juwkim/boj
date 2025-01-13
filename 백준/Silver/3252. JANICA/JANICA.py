import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
input()
score = [0] * N
for i in range(1, N):
    score[i] = min(score) + float(input())
input()
idxs = sorted(range(N), key=lambda x: score[x])[:M][::-1]
score = {idx: 0 for idx in idxs}
for idx in idxs[1:]:
    score[idx] += min(score.values()) + float(input())
ans = sorted(idxs, key=lambda x: score[x])[:3]
for idx in ans:
    print(idx + 1)