g = lambda: [*map(int, input().split())]

def solve(p, q):
    if q == 0:
        print()
        return
    elif q == 1:
        print(p)
        return
    else:
        print(p // q, end=' ')
        solve(q, p % q)
        

cnt = 0
while sum(s:= g()):
    r1, r2 = s
    nums = g()
    if r1 == 1:
        p1, q1 = 1, nums[0]
    else:
        n1, p1, q1 = nums[0], nums[-1], 1
        for i in range(r1 - 2, 0, -1):
            p1, q1 = nums[i] * p1 + q1, p1
        q1 += p1 * n1

    nums = g()
    if r2 == 1:
        p2, q2 = 1, nums[0]
    else:
        n2, p2, q2 = nums[0], nums[-1], 1
        for i in range(r2 - 2, 0, -1):
            p2, q2 = nums[i] * p2 + q2, p2
        q2 += p2 * n2
    
    cnt += 1
    print(f'Case {cnt}:')
    p, q = p1 * p2, q1 * p2 + q2 * p1
    print(q // p, end=' ')
    solve(p, q % p)
    
    p, q = p1 * p2, q1 * p2 - q2 * p1
    print(q // p, end=' ')
    solve(p, q % p)
    
    p, q = p1 * p2, q1 * q2
    print(q // p, end=' ')
    solve(p, q % p)
    
    p, q = p1 * q2, q1 * p2
    if p < 0:
        p = -p
        q = -q
    print(q // p, end=' ')
    solve(p, q % p)