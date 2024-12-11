import sys
input = sys.stdin.readline

N, M = map(int, input().split())
score = [[0, 0, 0] for _ in range(N + 1)]
freeze = [[] for _ in range(N + 1)]
for i in range(M):
    time, *l = input().split()
    id, p, s = map(int, l)
    h, m = map(int, time.split(':'))
    t = h * 60 + m
    if t <= 180:
        score[id][0] -= 1
        score[id][1] += t + (s - 1) * 20
        score[id][2] = (t, i)
    else:
        freeze[id].append((p, t + (s - 1) * 20, (t, i)))

def rank(x):
    for i in range(N):
        if nums[i][2] == x:
            return i
    assert False

nums = sorted((score[i], sorted(freeze[i], reverse=True), i) for i in range(1, N + 1))
point = [0] * (N + 1)
idx = N - 1
while True:
    while idx >= 0 and not nums[idx][1]:
        idx -= 1
    if idx < 0:
        break
    _, panalty, submit_time = nums[idx][1].pop()
    id = nums[idx][2]
    nums[idx][0][0] -= 1
    nums[idx][0][1] += panalty
    nums[idx][0][2] = max(nums[idx][0][2], submit_time)
    nums.sort()
    point[id] += idx - rank(id)
ans = max(range(1, N + 1), key=lambda x: (point[x], -rank(x)))
print(ans)