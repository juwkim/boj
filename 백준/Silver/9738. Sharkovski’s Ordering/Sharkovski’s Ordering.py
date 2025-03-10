for _ in range(int(input())):
    *nums, _ = map(int, input().split())
    a, b = [], []
    for num in nums:
        cur, cnt = num, 0
        while cur % 2 == 0:
            cur >>= 1
            cnt += 1
        if cur == 1:
            b.append(num)
        else:
            a.append((cnt, cur, num))
    ans = [p[2] for p in sorted(a)] + sorted(b, reverse=True)
    print(*ans)