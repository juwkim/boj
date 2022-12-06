N, M = map(int, input().split())
nums = sorted(map(int, input().split()))
check = {num: 0 for num in nums}
def solve(M, check, buf):
    if M == 0:
        print(*buf)
        return
    M -= 1
    for k, v in check.items():
        if v:
            continue
        s = check.copy()
        s[k] = 1
        solve(M, s, buf + [k])
solve(M, check, [])