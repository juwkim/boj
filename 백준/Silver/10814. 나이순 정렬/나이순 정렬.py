s = sorted([input().split() for _ in range(int(input()))], key = lambda x: int(x[0]))
for line in s:
    print(*line)