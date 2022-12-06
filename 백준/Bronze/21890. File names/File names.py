ans = 0
for _ in range(int(input())):
    l = input().split('.')
    if len(l) == 2:
        a, b = l
        if 1 <= len(a) <= 8 and 1 <= len(b) <= 3:
            ans += 1
print(ans)