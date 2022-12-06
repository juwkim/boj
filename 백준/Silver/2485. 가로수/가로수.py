from math import gcd
N = int(input())
buf = sorted(int(input()) for _ in range(N))
diff = []

GCD = None
for i in range(N-1):
    num = buf[i+1] - buf[i]
    diff.append(num)
    if GCD:
        GCD = gcd(GCD, num)
    else:
        GCD = num
ans = sum(num // GCD for num in diff) - (N - 1)
print(ans)