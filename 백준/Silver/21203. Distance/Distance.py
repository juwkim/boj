N = int(input())
a, s = map(sorted, zip(*[[*map(int, input().split())] for _ in range(N)]))
print(sum((a[i + 1] - a[i] + s[i + 1] - s[i]) * (i + 1) * (N - i - 1) for i in range(N - 1)))