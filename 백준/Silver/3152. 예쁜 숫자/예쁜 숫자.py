from collections import defaultdict
def solve(x):
    dic = defaultdict(int)
    while x:
        x, r = divmod(x, p)
        if r > 2:
            return 0
        dic[r] += 1
    return int(dic[1] == (2 - (dic[2] != 0)))
p, *nums = map(int, input().split())
print(*map(solve, nums))