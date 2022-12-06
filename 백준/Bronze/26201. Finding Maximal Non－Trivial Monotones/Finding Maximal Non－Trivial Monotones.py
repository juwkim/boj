input()
ans, cur = 0, 1
c, *l = input()
for alpha in l:
    if alpha == c:
        cur += 1
    else:
        ans += cur * (c == 'a') * (cur > 1)
        cur = 1
        c = alpha
ans += cur * (c == 'a') * (cur > 1)
print(ans)