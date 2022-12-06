N, M = map(int, input().split())
nums = sorted(map(int, input().split()))
def solve(M, buf):
    if M == 0:
        print(*buf[1:])
        return
    M -= 1
    for num in nums:
        if num > buf[-1]:
            solve(M, buf + [num])
solve(M, [0])