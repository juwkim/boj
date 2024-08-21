n = int(input())
a = sorted(map(int, input().split()))
p = (n - 1) // 2
ans = [a[p]]
for i in range(1, n):
    if n + i & 1:
        p += i
    else:
        p -= i
    ans.append(a[p])
print(*ans)