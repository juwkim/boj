a, b = int(input()), int(input())
ans = 0
i = 1
while i ** 6 <= b:
    if i ** 6 >= a:
        ans += 1
    i += 1
print(ans)