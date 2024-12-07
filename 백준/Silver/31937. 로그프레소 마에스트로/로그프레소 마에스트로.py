import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, M, K = g()
nums = sorted(g())
log = sorted(g() for _ in range(M))
start = [0] * (N + 1)
for idx, (_, a, _) in enumerate(log):
    if start[a] == 0:
        start[a] = idx

for num in nums:
    idx = start[num]
    time = [0] * (N + 1)
    time[num] = 1
    for i in range(idx, M):
        t, a, b = log[i]
        if time[a] and time[a] <= t:
            time[b] = t + 1
    if [i for i in range(1, N + 1) if time[i]] == nums:
        print(num)
        break