g = lambda: [*map(int, input().split())]

N, H, W = g()
ans = ['?'] * N
for _ in range(H):
    s = input()
    for i in range(0, N * W, W):
        for j in range(W):
            if s[i + j] != '?':
                ans[i // W] = s[i + j]
print(''.join(ans))