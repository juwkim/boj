g = lambda: [*map(int, input().split())]

buf = []
N = int(input())
for _ in range(N):
    nums = g()
    res = []
    for i in range(3):
        for j in range(i+1, 4):
            for k in range(j+1, 5):
                tmp = (nums[i] + nums[j] + nums[k]) % 10
                res.append(tmp)
    buf.append(max(res))
ans = 0
for i in range(N):
    if buf[i] >= buf[ans]:
        ans = i
print(ans + 1)  