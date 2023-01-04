check = set()
ans = 'No two snowflakes are alike.'
for _ in range(int(input())):
    l = 2 * tuple(map(int, input().split()))
    flag = True
    for i in range(6):
        a, b = l[i:i+6], l[i+6:i:-1]
        if a in check or b in check:
            break
        check.add(a)
        check.add(b)
    else:
        continue
    ans = 'Twin snowflakes found.'
    break
print(ans)