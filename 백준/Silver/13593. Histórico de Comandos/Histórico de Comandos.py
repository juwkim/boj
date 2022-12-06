g = lambda: [*map(int, input().split())]

while N:= int(input()):
    
    nums = g()
    dic = {num: num for num in nums}

    cur = 0
    ans = 0
    for num in nums:
        ans += dic[num] - cur
        dic[num] = cur
        cur -= 1
    print(ans)