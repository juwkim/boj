input = __import__('sys').stdin.readline
g = lambda: [*map(int, input().split())]
N, C = g()

home = sorted(int(input()) for _ in range(N))

left, right = 0, home[-1]
while left <= right:
    cnt, prev, mid = 1, 0, (left + right) // 2
    for i in range(1, N):
        if home[i] - home[prev] >= mid:
            prev = i
            cnt += 1
    if cnt < C:
        right = mid - 1
    else:
        left = mid + 1
print(right)