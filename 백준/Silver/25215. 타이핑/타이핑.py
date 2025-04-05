N = len(s:=input())
ans, cur = N, 0
for i in range(N - 1):
    if cur != s[i].isupper():
        ans += 1
        if cur != s[i + 1].isupper():
            cur ^= 1
ans += cur != s[-1].isupper()
print(ans)