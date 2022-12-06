from collections import Counter
N, M = map(int, input().split())
nums = dict(Counter(sorted(map(int, input().split()))))
def solve(M, check, buf):
    if M == 0:
        print(*buf[1:])
        return
    M -= 1
    for k, v in check.items():
        if k >= buf[-1] and v:
            s = check.copy()
            s[k] -= 1
            solve(M, s, buf + [k])
solve(M, nums, [0])