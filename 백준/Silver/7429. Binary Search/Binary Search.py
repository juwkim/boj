i, L = map(int, input().split())
nums = []
for N in range(i + 1, 10001):
    p, q, cnt = 0, N - 1, 0
    while p <= q:
        idx = p + q >> 1
        cnt += 1
        if idx == i:
            if cnt == L:
                nums.append(N)
            break
        elif i < idx:
            q = idx - 1
        else:
            p = idx + 1
ans = []
s, e = 0, 0
for num in nums:
    if e:
        if num == e + 1:
            e = num
        else:
            ans.append((s, e))
            s, e = num, num
    else:
        s, e = num, num
if e:
    ans.append((s, e))
print(len(ans))
for s, e in ans:
    print(s, e)