a, b, c = int(input()), int(input()), int(input())

ans = -1
if a + b == c:
    ans = 1
elif a * a + b * b == c * c:
    ans = 2
print(ans)