k = int(input())
cnt = 0
line = []
for l in input().split():
    if cnt + len(line) + len(l) <= k:
        line.append(l)
        cnt += len(l)
    else:
        print(*line)
        cnt = len(l)
        line = [l]
print(*line)