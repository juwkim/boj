k = int(input())
if k == 0:
    print(0)
else:
    ans = 1e18
    K = abs(k)
    for d in range(1, int(K**.5) + 1):
        q, r = divmod(K, d)
        if r:
            continue
        for D in d, q:
            for u in D, -D:
                v = k // u
                if u > v or u + v & 1:
                    continue
                m = v + u >> 1
                n = v - u >> 1
                if m >= 0 and n >= 0:
                    ans = min(ans, m)
    if ans == 1e18:
        print("none")
    else:
        print(ans)