N, W, H = map(int, input().split())
D = (W**2 + H**2)**.5
for _ in range(N):
    print('DA' if int(input()) <= D else 'NE')