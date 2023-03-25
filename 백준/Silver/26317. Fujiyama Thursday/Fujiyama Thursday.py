g = lambda: [*map(int, input().split())]

for case in range(1, 1 + int(input())):
    c = int(input())
    d = sorted(g())
    nums = sorted(g(), reverse=True)
    ans = max(d[i] + max(nums[4*i:4*i+4]) for i in range(c))
    print(f'Trip #{case}: {ans}')