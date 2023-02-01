from math import gcd
def isprime(num):
    
    for i in range(2, int(num**.5) + 1):
        if num % i == 0:
            return False
    return True

x, l, r = map(int, [input() for _ in range(3)])
ans = []
for num in range(l, r + 1):
    if x!= num and isprime(gcd(num, x)):
        ans.append(num)
print(len(ans))
print(*ans)