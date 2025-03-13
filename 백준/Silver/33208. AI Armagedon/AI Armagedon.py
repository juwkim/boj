N, K, *a = map(int, open(0).read().split())
ans, s = 0, set()
for num in a:
    if num not in s and len(s) == K - 1:
        ans += 1
        s = {num}
    else:
        s.add(num)
print(ans)