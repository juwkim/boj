ans = 0
for _ in range(int(input())):
    a, d, g = map(int, input().split())
    num = a * (d + g)
    if a == d + g:
        num <<= 1
    
    ans = max(ans, num)
print(ans)