N = int(input())
px = [0] * (N + 1)
for i, c in enumerate(input()):
    px[i + 1] = px[i] + (c == 'O')
ans = 0
for l in range(3, int(N ** 0.5) + 1):
    a = 4 * (l - 1), (l - 2)**2
    ans += sum(px[i + l * l] - px[i] in a for i in range(N - l * l + 1))
print(ans)