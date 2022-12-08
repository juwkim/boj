cnt = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
n = int(input()) - 4
ans = 'impossible'
if 17 < n < 41:
    for i in range(100):
        for j in range(100 - i):
            k = i + j
            num = sum(cnt[c//10] + cnt[c%10] for c in (i, j, k))
            if num == n:
                ans = "%02d+%02d=%02d" % (i, j, k)
                break
        if ans[0] != 'i':
            break
print(ans)