from collections import Counter
N, M = map(int, input().split())
nums = dict(Counter(sorted(input().split(), key=int)))
def solve(M, check, buf):
    if M == 0:
        print(*buf)
        return
    M -= 1
    for k, v in check.items():
        if v:
            s = check.copy()
            s[k] -= 1
            solve(M, s, buf + [k])
solve(M, nums, [])