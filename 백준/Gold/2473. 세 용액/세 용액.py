N = int(input())
values = sorted(map(int, input().split()))
def solve(i):
    a = values[i]
    base, acid = values[i+1], values[-1]
    check = abs(base + acid + a)
    left, right = i+1, N - 1
    while left != right:
        now = values[left] + values[right] + a
        if abs(now) < check:
            check = abs(now)
            base, acid = values[left], values[right]
        if now > 0:
            right -= 1
        elif now < 0:
            left += 1
        else:
            base, acid = values[left], values[right]
            break
    return check, a, base, acid

minn = 10000000000
ans1, ans2, ans3 = 0, 0, 0
for i in range(N-2):
    val, a, b, c = solve(i)
    if val < minn:
        minn = val
        ans1, ans2, ans3 = a, b, c
print(ans1, ans2, ans3)