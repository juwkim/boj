from math import isqrt
A, B = int(input()), int(input())
s = isqrt(A-1) + 1
t = isqrt(B) + 1

ans = 0
for i in range(s, t):
    num = str(i * i)[::-1]
    
    if num[0] == '0':
        continue
    
    num = int(num)
    if isqrt(num) ** 2 == num:
        ans += 1
print(ans)