input = __import__('sys').stdin.readline
N, C = map(int, input().split())
home = sorted(int(input()) for _ in range(N))

left, right = 1, home[-1] + 1
while left + 1 < right:
    cnt, prev, mid = 1, 0, (left + right) // 2
    for i in range(1, N):
        if home[i] - home[prev] >= mid:
            prev = i
            cnt += 1
    if cnt < C:
        right = mid
    else:
        left = mid
print(left)