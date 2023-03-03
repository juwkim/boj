n, c = map(int, input().split())
cur = [0] * n
for num in map(int, input().split()):
    idx = min(range(n), key=lambda x: (cur[x], x))
    cur[idx] += num
    print(idx + 1, end=' ')