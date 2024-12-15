n = int(input())
st, i, m = [[] for _ in range((n + 1) // 2)], 0, 10**9 + 7
for c in input().split():
    if c == '(':
        i += 1
    elif c == ')':
        if i & 1:
            num = 1
            while st[i]:
                num = (num * st[i].pop()) % m
            i -= 1
            st[i].append(num)
        else:
            num = 0
            while st[i]:
                num = (num + st[i].pop()) % m
            i -= 1
            st[i].append(num)
    else:
        st[i].append(int(c))
ans = 0
while st[i]:
    ans = (ans + st[i].pop()) % m
print(ans)