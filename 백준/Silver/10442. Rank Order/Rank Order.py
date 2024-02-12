s = lambda l: [*zip(*sorted(enumerate(l), key=lambda x: -x[1]))][0]
nums = [*map(int, open(0).read().split())]
i = 0
tc = 1
while i < len(nums):
    N = nums[i]
    i += 1
    ans = "agree"
    for t, (p, q) in enumerate(zip(s(nums[i:i+N]), s(nums[i+N:i+2*N])), 1):
        if p != q:
            ans = t
            break
    print(f"Case {tc}: {ans}")
    tc += 1
    i += 2 * N