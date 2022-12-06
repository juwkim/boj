g = lambda: map(int, input().split())
n, *nums = g()
while n:
    res = [''] * 20
    num = ord('A')
    for i in range(20):
        if not res[i]:
            res[i] = chr(num)
            num += 1
        Next = i + nums[i % n]
        if Next < 20:
            if res[Next]:
                res = 'CRASH'
                break
            else:
                res[Next] = res[i]
    print(*res, sep='')
    n, *nums = g()