def solve():
    cnt, Sum = 0, 0
    for num in input().split():
        if num == 'X':
            continue
        cnt += 1
        Sum += int(num)
    return cnt, Sum

t, p = map(int, input().split())
cnt, Sum = solve()
ans = 0
for _ in range(t - 1):
    cnt1, Sum1 = solve()
    if cnt1 > cnt or (cnt1 == cnt and Sum1 <= Sum):
        ans += 1
print(ans)