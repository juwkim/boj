ans = 0
L, R = input().split()
if len(L) != len(R):
    ans = 0
else:
    for a, b in zip(L, R):
        if a != b:
            break
        ans += a == '8'
print(ans)