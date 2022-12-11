N, K = map(int, input().split())
time = 900
while N > 0:
    time += K
    if time >= 1440:
        time -= 1440
        N -= 1
    N -= 1
ans = []
if N == 0:
    ans.append(time)
    if time + 180 < 1440:
        ans.append(time + 180)
    if time + 360 < 1440:
        ans.append(time + 360)
    if time - (1080 + K) >= 0:
        ans.append(time - (1080 + K))
    if time - (1260 + K) >= 0:
        ans.append(time - (1260 + K))
    if time - (1440 + K) >= 0:
        ans.append(time - (1440 + K))
elif N == -1:
    time -= K
    if time + 180 < 1440:
        ans.append(time + 180)
    if time + 360 < 1440:
        ans.append(time + 360)
ans.sort()
print(len(ans))
for num in ans:
    print("%02d:%02d" % divmod(num, 60))