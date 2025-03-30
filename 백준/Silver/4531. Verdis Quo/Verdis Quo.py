for _ in range(int(input())):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans, prv = 0, 0
    for c in input()[::-1]:
        v = dic[c]
        if v < prv:
            ans -= v
        else:
            ans += v
        prv = v
    print(ans)