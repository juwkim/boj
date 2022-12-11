N, K = map(int, input().split())
ans = []
t, dt, idx = 900, (180, 180, 1080 + K), 0
while N >= 0:
    if N == 0:
        ans.append(t)
    q, t = divmod(t + dt[idx], 1440)
    N -= (q != 0)
    if idx == 2:
        idx = 0
    else:
        idx += 1
ans.sort()
print(len(ans))
for num in ans:
    print("%02d:%02d" % divmod(num, 60))