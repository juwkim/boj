def seive(n):
    prime = [True]*(n+1)
    p = 2
    while p*p <= n:
        if prime[p]:
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1
    return prime

prime = seive(32000)
for x in map(int, [*open(0)][1:]):
    ans = []
    if prime[2] and prime[x - 2]:
        ans.append((2, x - 2))
    for a in range(3, x//2+1, 2):
        if prime[a] and prime[x-a]:
            ans.append((a, x-a))
    print(f"{x} has {len(ans)} representation(s)")
    for a, b in ans:
        print(f"{a}+{b}")
    print()