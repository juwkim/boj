for _ in range(int(input())):
    nums = [[*map(int, input().split())] for _ in range(int(input()))]
    l = [*map(int, input().split())]
    l[1] = -l[1]
    
    ans = 0
    for num in nums:
        ans += max(0, sum(s * t for s, t in zip(num, l)))
    print(ans)