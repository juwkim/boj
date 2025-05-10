for _ in range(int(input())):
    n = int(input())
    s1 = [*map(int, input())]
    s2 = [*map(int, input())]
    ans = 0
    for i in range(n - 1):
        if s1[i] != s2[i]:
            ans += 1
            s1[i+1] ^= 1
    if s1[-1] != s2[-1]:
        ans = -1
    print(ans)