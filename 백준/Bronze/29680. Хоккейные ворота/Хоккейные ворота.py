H, W, w1, w2 = map(float, input().split())
ans = W * ((H * H + (w2 - w1) ** 2) ** .5 + w1) + H * (w1 + w2)
print(ans)