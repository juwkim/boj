g = lambda: [*map(int, input().split())]


for _ in range(1, 1 + int(input())):
    N, B = g()
    nums = sorted(g())
    
    ans = N
    for i in range(N):
        B -= nums[i]
        if B < 0:
            ans = i
            break
    print(f'Case #{_}: {ans}')