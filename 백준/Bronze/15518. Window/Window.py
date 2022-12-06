N, H, W = map(int, input().split())
x = [*map(int, input().split())]
area = sum(min(x[i] + x[i+1], 2 * W - x[i] - x[i+1]) for i in range(0, N, 2))
print(area * H)