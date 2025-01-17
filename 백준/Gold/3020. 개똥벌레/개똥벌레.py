N, H, *nums = map(int, open(0).read().split())
a, b = [0] * H, [0] * H
for i, num in enumerate(nums):
    if i & 1:
        b[num] += 1
    else:
        a[num] += 1
cnt1, cnt2 = [0] * (H + 1), [0] * (H + 1)
for i in range(H - 1, 0, -1):
    cnt1[i] = cnt1[i + 1] + a[i]
for i in range(2, H + 1):
    cnt2[i] = cnt2[i - 1] + b[H + 1 - i]
cnt = [cnt1[i] + cnt2[i] for i in range(1, H + 1)]
Min = min(cnt)
print(Min, cnt.count(Min))