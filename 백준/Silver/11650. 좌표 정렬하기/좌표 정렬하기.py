s = sorted([[*map(int, input().split())] for _ in range(int(input()))])
for line in s:
    print(*line)