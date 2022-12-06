g = lambda: [*map(int, input().split())]

N, P = g()
nums = [g() for _ in range(N)]
minmax = [[min(l), max(l)] for l in nums]

buf = []
for i in range(P):
    mins, maxs = 0, 0
    for j in range(N):
        mins += (nums[j][i] == minmax[j][0])
        maxs += (nums[j][i] == minmax[j][1])
    if mins > N // 2 and maxs == 0:
        buf.append(i+1)

if buf:
    print(*buf)
else:
    print(0)