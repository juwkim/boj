N = int(input())
px = [0, *map(int, input().split())]
ans, cur = 0, 0
cnt = [0, 0]
for i in range(N):
    cnt[0] += cur & 1
    cnt[1] += ((cur + 1) & 1)
    cur += px[i+1]
    ans += cnt[cur&1]
print(ans)