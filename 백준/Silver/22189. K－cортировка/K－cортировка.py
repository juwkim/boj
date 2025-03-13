def solve():
    n, *a, k = map(int, open(0).read().split())
    b = sorted(a)
    ans = 0
    for i in range(k):
        p, q = a[i::k], b[i::k]
        for j in range(len(p)):
            if p[j] == q[j]:
                continue
            if q[j] not in p[j:]:
                return -1
            idx = p[j:].index(q[j]) + j
            p.insert(j, p.pop(idx))
            ans += idx - j                
    return ans
print(solve())