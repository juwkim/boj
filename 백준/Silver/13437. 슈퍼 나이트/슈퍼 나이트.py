*l, N, M, k = map(int, input().split())
a, b = sorted(l)
match k:
    case 0 | 1 | 5 | 7:
        ans = 0
    case 2:
        ans = 4 * a ** 2
    case 3:
        ans = 8 * a * (b - a)
    case 4:
        ans = 2 * a * (N + M - 4 * b) + 4 * (b - a) ** 2
    case 6:
        ans = 2 * (b - a) * (N + M - 4 * b)
    case 8:
        ans = (N - 2 * b) * (M - 2 * b)
print(ans)