a, b, c = input().split()
if a == c:
    ans = a + b + c
elif b == c:
    ans = a + b + b + a
else:
    ans = a + b + c + b + a
print(ans)