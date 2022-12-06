g = lambda: [*map(int, input().split())]

n = int(input())
d = [g()[1] for _ in range(6)]
d += d
area = max(d[i] * d[i+1] - d[i+3] * d[i+4] for i in range(6))
print(area * n)