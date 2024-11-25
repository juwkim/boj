a, b = input(), input()
ans = len(b)
if len(a) == len(b):
    i = 0
    while i < len(a) and a[i] == b[i]:
        ans += a[i] == '1'
        i += 1
    ans -= i
print(ans)