def solve():
    H, W, C, D = map(int, open(0).read().split())
    if min(H * W, 2 * C, 2 * D) < H * (H - 1):
        print(-1)
        return -1
    q, r = divmod(D - H * (H - 1) // 2, H)
    for i in range(H):
        num = i + q + (H - 1 - i < r)
        print(*[9] * num + [1] * (W - num))
solve()