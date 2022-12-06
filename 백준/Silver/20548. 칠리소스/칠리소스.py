c = int(input())
ans, i = 0, 1
while c:
    c, r = divmod(c, 7)
    ans += r * i
    i *= 3
print(ans)