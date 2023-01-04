def g(): return [*map(int, input().split())]

C, N = g()
check, ans = set(), []
for num in g()[::-1]:
    if num not in check:
        check.add(num)
        ans.append(num)
print(len(ans))
print(*ans[::-1])