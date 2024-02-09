ans, cur, last = 0, 0, 0
for c in input():
    cur += (c == 'R') - (c == 'L')
    if cur - last == 4:
        last = cur
        ans += 1
    elif cur % 4 == 0:
        last = cur
print(ans)