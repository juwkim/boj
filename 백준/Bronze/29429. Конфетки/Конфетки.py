a, b = input(), input()
if len(a) < len(b) or a == b:
    ans = "Bad luck"
elif len(a) > len(b) or a > b:
    ans = 0
else:
    for i in range(len(b)):
        if a[i] < b[i]:
            ans = f"1\n{i + 1}"
            break
print(ans)