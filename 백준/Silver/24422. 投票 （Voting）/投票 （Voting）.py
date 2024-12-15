import sys
input = sys.stdin.readline

ans, px = 0, [0]
for i in range(int(input())):
    X, Y = map(int, input().split())
    if px[i] - px[i - X] >= Y:
        ans += 1
        px.append(px[i] + 1)
    else:
        px.append(px[i])
print(ans)