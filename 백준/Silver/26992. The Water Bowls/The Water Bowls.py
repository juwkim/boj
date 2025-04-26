bowls = [1] + [*map(int, input().split())] + [0]
def solve(s, l):
    cnt = 0
    for i in range(s, 20):
        if l[i]:
            cnt += 1
            l[i] ^= 1
            l[i + 1] ^= 1
            l[i + 2] ^= 1
    if any(l[1:21]):
        return float('inf')
    return cnt
print(min(solve(0, bowls[:]), solve(1, bowls[:])))