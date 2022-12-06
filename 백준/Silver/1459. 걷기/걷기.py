X, Y, W, S = map(int, input().split())
X, Y = sorted([X, Y])

if S < W:
    if (Y - X) % 2:
        ans = S * (Y - 1) + W
    else:
        ans = S * Y
elif S < 2 * W:
    ans = S * X + W * (Y - X)

else:
    ans = W * (X + Y)

print(ans)