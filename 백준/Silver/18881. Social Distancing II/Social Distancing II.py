g = lambda: [*map(int, input().split())]

N = int(input())
cows = sorted(g() for _ in range(N))

R = 1e7
for i in range(N-1):
    if cows[i][1] + cows[i+1][1] == 1:
        R = min(R, cows[i+1][0] - cows[i][0])
if R == 1e7:
    print(cows[0][1])
else:
    ans = 0    
    cur = 0
    prev = -R
    for i in range(N):
        if cows[i][1] == 1:
            if cur == 0:
                cur = 1
                ans += 1
            elif cows[i][0] - prev >= R:
                ans += 1
            prev = cows[i][0]
        else:
            if cur == 1:
                cur = 0
    print(ans)