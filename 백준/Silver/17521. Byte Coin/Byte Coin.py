N, W = map(int, input().split())
prev = int(input())
for _ in range(N-1):
    cur = int(input())
    W += W//prev * max(0, cur - prev)
    prev = cur
print(W)