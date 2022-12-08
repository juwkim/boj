g = lambda: [*map(int, input().split())]

dic = {}
for _ in range(int(input())):
    e, n = g()
    dic[e] = n
for _ in range(int(input())):
    n, *nums = g()
    ans = []
    for num in nums:
        if num in dic:
            ans.append(dic[num])
    if len(ans) == n:
        print(*ans)
    else:
        print('YOU DIED')