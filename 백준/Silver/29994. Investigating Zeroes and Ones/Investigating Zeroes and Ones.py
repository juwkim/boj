N = int(input())
px = [0, *map(int, input().split())]
for i in range(N):
    px[i + 1] += px[i]
ans = 0
cnt = [0, 0]
for i in range(N):
    cnt[0] += (px[i] & 1)
    cnt[1] += ((px[i] + 1) & 1)
    ans += cnt[px[i+1]&1]
print(ans)