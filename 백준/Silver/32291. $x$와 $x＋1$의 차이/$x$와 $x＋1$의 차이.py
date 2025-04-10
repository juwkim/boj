n = int(input()) + 1
ans = [1]
for k in range(2, int(n**.5) + 1):
    if n % k == 0:
        ans.append(k)
        if k != n // k:
            ans.append(n // k)
ans.sort()
print(*ans)