g = lambda: [*map(int, input().split())]


N = int(input())
nums = sorted(g())
M = int(input())

px = [0]
for i in range(N):
    px.append(px[-1] + nums[i])

idx = None
for i in range(N):
    num = px[i] + nums[i] * (N - i)
    if num > M:
        idx = i
        break

if idx == None:
    print(nums[-1])
else:
    print((M - px[idx]) // (N - idx))