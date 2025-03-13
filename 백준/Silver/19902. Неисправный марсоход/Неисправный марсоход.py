a, b, c = map(int, open(0))
ans = 0
while a + 1 < b:
    if a % c:
        a += 2
    else:
        a += 1
    ans += 1
if a + 1 == b:
    ans += 1
print(ans)