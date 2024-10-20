k = int(input())
ans = []
i = 2
while i * i <= k:
    if k % i == 0:
        ans.append(i)
        k //= i
    else:
        i += 1
if k > 1:
    ans.append(k)
print(len(ans))
print(*ans)