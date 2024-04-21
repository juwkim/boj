from math import isqrt
while r:=int(input()):
    ans = 0
    for i in range(r):
        ans += isqrt(r * r - i * i)
    ans = ans * 4 + 1
    print(ans)