N = int(input())
p = [*map(float, input().split())]
print(sum(p) + sum(p[i] + p[i + 1] - 2 * p[i] * p[i + 1] for i in range(N - 1)))