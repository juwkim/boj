while (s:=input())[0] != 'E':
    n = len(s)
    ans, max_cnt, max_l = (n - 1, 1), s[-1] == '.', n - 1
    for i in range(n - 2, -1, -1):
        for d in range(1, n - i):
            cnt, l = 0, i
            while l < n and s[l] == '.':
                cnt += 1
                l += d
            if l >= n:
                l -= d
            if (cnt, l) > (max_cnt, max_l):
                ans, max_cnt, max_l = (i, d), cnt, l
    print(*ans)