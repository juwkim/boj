A, B = map(int, input().split())
if A & 1:
    ans = (B - A) % 4 < 2
else:
    ans = (B - A) % 4 in (1, 2)
for i in range(1, 60):
    num = 1 << i
    cur = 0
    if A & num:
        cur += num - A % num
    if B & num:
        cur += B % num + 1
    if cur & 1:
        ans += num
print(int(ans))