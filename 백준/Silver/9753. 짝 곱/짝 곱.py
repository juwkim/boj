import sys
input = sys.stdin.readline
from bisect import bisect_left

def seive(n):
    prime = [True] * (n + 1)
    prime[0], prime[1] = False, False
    for i in range(2, int(n**.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
    return prime, [i for i in range(2, n + 1) if prime[i]]

isprime, prime = seive(50021)
for _ in range(int(input())):
    K = int(input())
    ans = 1e9
    for num1 in range(2, int(K**.5) + 1):
        if isprime[num1] == False:
            continue
        idx = bisect_left(prime, (K + num1 - 1) // num1)
        num2 = prime[idx]
        ans = min(ans, num1 * num2)
    print(6 if ans == 1e9 else ans)