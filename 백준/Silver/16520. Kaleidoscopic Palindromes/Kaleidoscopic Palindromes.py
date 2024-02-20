a, b, k = map(int, input().split())
if k == 2:
    ans = 0
    for i in range(a, b + 1):
        b = bin(i)[2:]
        if b == b[::-1]:
            ans += 1
elif k == 3:
    ans = 0
    for num in (0, 1, 6643, 1422773):
        if a <= num <= b:
            ans += 1
else:
    ans = 0
    for num in (0, 1):
        if a <= num <= b:
            ans += 1    
print(ans)