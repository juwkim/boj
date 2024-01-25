def solve(N):
    l = 1
    ans = 0
    while N > 2 * l:
        ans += l
        l <<= 1
    if N > l:
        ans += (N + 1) // 2
    return ans
print(solve(int(input())))