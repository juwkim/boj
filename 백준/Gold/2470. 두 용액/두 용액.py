N = int(input())
values = sorted(map(int, input().split()))
base, acid = values[0], values[-1]
check = base + acid
left, right = 0, N - 1
while left != right:
    now = values[left] + values[right]
    if abs(now) < abs(check):
        check = now
        base, acid = values[left], values[right]
    if now > 0:
        right -= 1
    elif now < 0:
        left += 1
    else:
        base, acid = values[left], values[right]
        break

print(base, acid)