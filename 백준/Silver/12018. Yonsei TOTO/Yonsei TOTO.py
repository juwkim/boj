g = lambda: [*map(int, input().split())]

N, M = g()
buf = []
for _ in range(N):
    P, L = g()
    nums = sorted(g(), reverse=True)
    if P < L:
        buf.append(1)
    else:
        buf.append(nums[L-1])
buf.sort()
for i in range(N):
    M -= buf[i]
    if M < 0:
        N = i
        break
print(N)