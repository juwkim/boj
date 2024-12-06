N, *a = map(int, open(0).read().split())
b = []
ans = []
for num in range(N, 0, -1):
    if num in a:
        while a[-1] != num:
            b.append(a.pop())
            ans.append("1 2")
        a.pop()
        ans.append("1 3")
    else:
        while b[-1] != num:
            a.append(b.pop())
            ans.append("2 1")
        b.pop()
        ans.append("2 3")
print(len(ans))
print(*ans, sep="\n")