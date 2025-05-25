N = int(input())
px = [0] * (N + 1)
for i, c in enumerate(input()):
    px[i + 1] = px[i] + (c == 'B')
print(min(i + px[N] - 2 * px[i] for i in range(N + 1)))