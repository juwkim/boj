a, b = int(input()), int(input())
print(a)
print(b)
nums = []
ans, mul = 0, 1
while b:
    b, r = divmod(b, 10)
    print(a * r)
    ans += a * r * mul
    mul *= 10
print(ans)