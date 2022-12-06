n, m, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]
def solve():
    x, y = 0, 0
    a = 0
    for b in range(m):
        k = int(input())
        while k:
            if nums[a] > k:
                x += k
                y += k * (a + b + 2)
                nums[a] -= k
                k = 0
            else:
                x += nums[a]
                y += nums[a] * (a + b + 2)
                k -= nums[a]
                a += 1
                if a == n:
                    return x, y
    return x, y
print(*solve())