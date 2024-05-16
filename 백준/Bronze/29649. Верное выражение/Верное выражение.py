a, op, b, eq, c = input().split()
ans = []
for i in range(max(2, int(max(a + b + c)) + 1), 11):
    p, q, r = int(a, i), int(b, i), int(c, i)
    if eval(f"{p}{op}{q}=={r}"):
        ans.append(i)
print(len(ans), *ans)