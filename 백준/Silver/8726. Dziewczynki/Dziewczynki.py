g = lambda: [*map(int, input().split())]

n, k = g()
nums = g()

buf = []
for i in range(n):
    if nums[i] == 0:
        buf.append(i)

if len(buf) < k:
    print('NIE')
else:
    ans = min(buf[i+k-1] - buf[i] for i in range(len(buf) - k + 1)) - k + 1
    print(ans)