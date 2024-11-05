N, *nums = map(int, open(0).read().split())
s = set()
def solve(i, cur):
    if i == N:
        s.add(cur)
        return
    solve(i + 1, cur + nums[i])
    solve(i + 1, cur)
solve(0, 0)
print(sum(nums) + 1 - len(s))