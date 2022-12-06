N, M = map(int, input().split())
nums = sorted(map(int, input().split()))
def solve(M, buf):
    if M == 0:
        print(*buf)
        return
    M -= 1
    for num in nums:
        solve(M, buf + [num])
solve(M, [])