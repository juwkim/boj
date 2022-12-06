import sys
input = lambda: sys.stdin.readline().rstrip()

g = lambda: [*map(int, input().split())]
for _ in range(1, 1 + int(input())):
    N, X = g()
    
    
    nums = sorted(g())
    l, r = 0, N - 1
    ans = 0
    while l <= r:
        if l == r:
            ans += 1
            break
        if nums[l] + nums[r] <= X:
            ans += 1
            l += 1
            r -= 1
        else:
            ans += 1
            r -= 1    
    print(f'Case #{_}:', ans)