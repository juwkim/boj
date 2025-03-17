import sys
input = sys.stdin.readline

for tc in range(1, 1 + int(input())):
    M = int(input())
    N = int(input())
    nums = [[*map(int, input().split())] for _ in range(M)]
    turns, forever = 0, False
    while True:
        for i in range(M):
            for j in range(N):
                if nums[i][j] < 12:
                    nums[i][j] = 0
                    continue
                friends = [(p, q) for p, q in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)) if 0 <= p < M and 0 <= q < N and nums[p][q] >= 12]
                if not friends:
                    nums[i][j] = 0
        if all(all(x == 0 for x in row) for row in nums):
            break
        a = [[0] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                if nums[i][j] == 0:
                    continue
                friends = [(p, q) for p, q in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)) if 0 <= p < M and 0 <= q < N and nums[p][q]]
                cnt = 12 // len(friends)
                for x, y in friends:
                    a[x][y] += cnt
                a[i][j] += nums[i][j] - 12
        turns += 1        
        if nums == a:
            forever = True
            break
        nums = a
    if forever:
        cnt = sum(sum(x != 0 for x in row) for row in nums)
        print(f"Case #{tc}: {cnt} children will play forever")
    else:
        print(f"Case #{tc}: {turns} turns")