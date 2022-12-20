g = lambda: map(int, input().split())

N = int(input())
check = set()
for i, num in enumerate(g(), 1):
    if num > i:
        check.add(N + i - num)
    else:
        check.add(i - num)
ans = 0
while ans in check:
    ans += 1
if ans == N:
    ans = -1
print(ans)