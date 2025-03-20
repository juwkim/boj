a, b, c, S = map(int, open(0).read().split())
ans = 0
while a | b | c:
    ans += 1
    cnt3 = min(c, S // 3)
    cnt2 = min(b, S - 3 * cnt3 >> 1)
    cnt1 = min(a, S - 2 * cnt2 - 3 * cnt3)
    if cnt3 and b - cnt2 >= 2 and (cnt1 or S > 2 * cnt2 + 3 * cnt3):
        cnt1 = max(0, cnt1 - 1)
        cnt2 += 2
        cnt3 -= 1
    a, b, c = a - cnt1, b - cnt2, c - cnt3
print(ans)