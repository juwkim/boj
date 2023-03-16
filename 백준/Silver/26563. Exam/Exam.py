for _ in range(int(input())):
    k = int(input())
    me, friend = input(), input()
    n = len(me) - k
    ans = 0
    for a, b in zip(me, friend):
        if a == b:
            if k:
                k -= 1
                ans += 1
        else:
            if n:
                n -= 1
                ans += 1
    print(ans)