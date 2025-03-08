n = int(input())
ans, num = 0, 5
while n >= num:
    ans += n // num
    num *= 5
print(ans)