a, b = zip(*[sorted(map(int, input().split())) for _ in range(int(input()))])
print(max(a) * max(b))