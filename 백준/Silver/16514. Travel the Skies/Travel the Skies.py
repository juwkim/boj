import sys
g = lambda: map(int, sys.stdin.readline().split())

k, n, m = g()
flights = [[] for _ in range(n + 1)]
passengers = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, d, z = g()
    flights[d].append((u, v, z))
for _ in range(k * n):
    a, b, c = g()
    passengers[b].append((a, c))

ans = "optimal"
nums = [0] * (k + 1)
for i in range(1, n + 1):
    for a, c in passengers[i]:
        nums[a] += c
    new_nums = [0] * (k + 1)
    for u, v, z in flights[i]:
        if nums[u] < z:
            ans = "suboptimal"
            break
        new_nums[v] += z
        nums[u] -= z
    if ans == "suboptimal":
        break
    for j in range(1, k + 1):
        new_nums[j] += nums[j]
    nums = new_nums
print(ans)