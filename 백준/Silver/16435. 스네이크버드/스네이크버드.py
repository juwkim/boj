g = lambda: [*map(int, input().split())]

N, L = g()
nums = sorted(g())
for i in range(N):
    if L >= nums[i]:
        L += 1
    else:
        break
print(L)