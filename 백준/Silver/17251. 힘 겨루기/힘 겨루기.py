N, *nums = map(int, open(0).read().split())
a = [0] * (N + 1)
b = [0] * (N + 1)
for i in range(N - 1):
    a[i + 1] = max(a[i], nums[i])
for i in range(N, 1, -1):
    b[i - 1] = max(b[i], nums[i - 1])
cnt = [0, 0, 0]
for i in range(1, N):
    cnt[(a[i] > b[i]) - (a[i] < b[i])] += 1
print('XRB'[(cnt[1] > cnt[2]) - (cnt[1] < cnt[2])])