q = int(input())
ans = "no"
if q == 1:
    ans = "no"
else:
    for i in range(2, int(q ** 0.5) + 1):
        cur = q
        if cur % i == 0:
            while cur % i == 0:
                cur //= i
            if cur == 1:
                ans = "yes"
            else:
                ans = "no"
            break
    else:
        ans = "yes"
print(ans)